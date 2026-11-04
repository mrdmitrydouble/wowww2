#!/usr/bin/env python3
"""Бесплатные гео-инструменты для ИИ-гида (без ключей API, только stdlib).

Используется из Claude Code (в приложении Claude сам строить URL к API нельзя).

Подкоманды:
  weather  LAT LON              погода сейчас, осадки по часам, восход/закат
  nearby   LAT LON [--kind K]   именованные места рядом из OpenStreetMap (Overpass)
  wiki     LAT LON              статьи Википедии рядом (что это за место/история)
  geocode  "запрос"             координаты по названию (Nominatim)
  walk     P1 P2 [P3 ...]       реальное пешее время/дистанция по OSM (FOSSGIS OSRM)
  links    P1 P2 [P3 ...]       ссылки маршрута: Google Maps (с разбивкой), Apple Maps, Organic Maps

Точка P = "lat,lon" или "lat,lon@Название" или просто "Название места, город".

Примеры:
  python3 guide/tools/geo.py weather 27.67 85.32
  python3 guide/tools/geo.py nearby 27.6727 85.3253 --kind view,sight --radius 1500
  python3 guide/tools/geo.py walk "27.6727,85.3253@Durbar Square" "27.6766,85.3133@Golden Temple"
  python3 guide/tools/geo.py links "Patan Durbar Square, Lalitpur" "Golden Temple, Patan" "Kumbheshwar Temple, Patan"

Лимиты бесплатных сервисов (соблюдайте): Nominatim — 1 запрос/сек; Overpass — ~10k/день;
Open-Meteo — некоммерческое использование; OSRM FOSSGIS — 1 запрос/сек.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "personal-travel-guide/1.0 (+https://github.com/mrdmitrydouble/wowww2)"
TIMEOUT = 40


class FetchError(Exception):
    pass


def _get(url: str, tries: int = 3) -> dict | list:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    last = None
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                return json.loads(r.read().decode("utf-8"))
        except (urllib.error.URLError, TimeoutError, ConnectionError, json.JSONDecodeError) as e:  # noqa: PERF203
            last = e
            if isinstance(e, urllib.error.HTTPError) and e.code in (400, 404):
                break
            time.sleep(1.5 * (attempt + 1))
    raise FetchError(f"{last}")


def _fail(url: str, err: Exception):
    """Сервис недоступен из этой сети (облачные IP часто режут) — отдаём URL агенту для WebFetch."""
    raise SystemExit(
        f"Не удалось получить данные ({err}).\n"
        f"Агенту: откройте этот URL своим инструментом WebFetch (у него другая сеть):\n{url}"
    )


def _haversine_m(lat1, lon1, lat2, lon2) -> float:
    r = 6371000.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = math.radians(lat2 - lat1), math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def gmaps_search(name: str, lat: float | None = None, lon: float | None = None) -> str:
    q = name if lat is None else f"{lat:.6f},{lon:.6f}"
    return "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote(q)


# ---------------------------------------------------------------- weather
WMO = {
    0: "ясно", 1: "в основном ясно", 2: "переменная облачность", 3: "пасмурно", 45: "туман", 48: "изморозь",
    51: "морось", 53: "морось", 55: "сильная морось", 61: "небольшой дождь", 63: "дождь", 65: "сильный дождь",
    71: "снег", 73: "снег", 75: "сильный снег", 80: "ливни", 81: "ливни", 82: "сильные ливни",
    95: "гроза", 96: "гроза с градом", 99: "гроза с градом",
}


def cmd_weather(a):
    q = urllib.parse.urlencode({
        "latitude": a.lat, "longitude": a.lon, "timezone": "auto", "forecast_days": a.days,
        "current": "temperature_2m,apparent_temperature,weather_code,wind_speed_10m,precipitation",
        "hourly": "precipitation_probability,temperature_2m,weather_code",
        "daily": "sunrise,sunset,temperature_2m_max,temperature_2m_min,precipitation_probability_max,uv_index_max",
    })
    url = "https://api.open-meteo.com/v1/forecast?" + q
    try:
        d = _get(url)
    except FetchError as e:
        _fail(url, e)
    c = d.get("current", {})
    print(f"Сейчас ({c.get('time')} местн.): {c.get('temperature_2m')}°C, ощущается {c.get('apparent_temperature')}°C, "
          f"{WMO.get(c.get('weather_code'), c.get('weather_code'))}, ветер {c.get('wind_speed_10m')} км/ч")
    dd = d.get("daily", {})
    for i, day in enumerate(dd.get("time", [])):
        print(f"{day}: {dd['temperature_2m_min'][i]}…{dd['temperature_2m_max'][i]}°C, дождь до {dd['precipitation_probability_max'][i]}%, "
              f"УФ {dd['uv_index_max'][i]}, восход {dd['sunrise'][i][-5:]}, закат {dd['sunset'][i][-5:]}")
    h = d.get("hourly", {})
    now = c.get("time", "")[:13]
    times = h.get("time", [])
    start = next((i for i, t in enumerate(times) if t[:13] >= now), 0)
    rows = []
    for i in range(start, min(start + 12, len(times))):
        rows.append(f"{times[i][11:16]} {h['temperature_2m'][i]:.0f}° {h['precipitation_probability'][i]}%")
    print("Ближайшие 12 ч (t°, вероятность осадков):", " | ".join(rows))


# ---------------------------------------------------------------- nearby (Overpass)
KINDS = {
    "food": ['nwr["amenity"~"^(restaurant|food_court|fast_food)$"]["name"]'],
    "cafe": ['nwr["amenity"~"^(cafe|ice_cream)$"]["name"]', 'nwr["shop"~"^(tea|coffee|bakery)$"]["name"]'],
    "bar": ['nwr["amenity"~"^(bar|pub|biergarten)$"]["name"]'],
    "view": ['nwr["tourism"="viewpoint"]', 'nwr["natural"="peak"]["name"]'],
    "sight": ['nwr["tourism"~"^(attraction|museum|gallery|artwork)$"]["name"]', 'nwr["historic"]["name"]'],
    "religious": ['nwr["amenity"="place_of_worship"]["name"]'],
    "nature": ['nwr["leisure"~"^(park|garden|nature_reserve)$"]["name"]', 'nwr["natural"~"^(water|wood|spring|waterfall)$"]["name"]', 'nwr["waterway"="waterfall"]["name"]'],
    "market": ['nwr["amenity"="marketplace"]', 'nwr["shop"~"^(craft|art|books|second_hand)$"]["name"]'],
    "wellness": ['nwr["leisure"~"^(sauna|spa)$"]', 'nwr["amenity"~"^(public_bath|spa)$"]', 'nwr["shop"="massage"]["name"]'],
}
OVERPASS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.private.coffee/api/interpreter",
    "https://maps.mail.ru/osm/tools/overpass/api/interpreter",
]
KIND_ALL = ["food", "cafe", "view", "sight", "religious", "nature", "market"]


def _osm_type(t: dict) -> str:
    for k in ("amenity", "tourism", "historic", "leisure", "natural", "shop", "waterway"):
        if k in t:
            return f"{k}={t[k]}" + (f" ({t['religion']})" if "religion" in t else "") + (f" [{t['cuisine']}]" if "cuisine" in t else "")
    return "?"


def cmd_nearby(a):
    kinds = KIND_ALL if a.kind == "all" else [k.strip() for k in a.kind.split(",")]
    parts = []
    for k in kinds:
        if k not in KINDS:
            raise SystemExit(f"Неизвестный --kind {k}. Доступно: {', '.join(KINDS)} или all")
        parts += [f"{sel}(around:{a.radius},{a.lat},{a.lon});" for sel in KINDS[k]]
    ql = f"[out:json][timeout:30];({''.join(parts)});out center tags {a.limit * 4};"
    d, url = None, ""
    for base in OVERPASS:
        url = base + "?" + urllib.parse.urlencode({"data": ql})
        try:
            d = _get(url, tries=1)
            break
        except FetchError as e:
            err = e
    if d is None:
        _fail(OVERPASS[0] + "?" + urllib.parse.urlencode({"data": ql}), err)
    items = []
    for e in d.get("elements", []):
        t = e.get("tags", {})
        lat = e.get("lat", e.get("center", {}).get("lat"))
        lon = e.get("lon", e.get("center", {}).get("lon"))
        if lat is None:
            continue
        name = t.get("name") or t.get("name:en") or t.get("description") or "(без названия)"
        items.append((_haversine_m(a.lat, a.lon, lat, lon), name, t, lat, lon))
    items.sort(key=lambda x: x[0])
    seen = set()
    n = 0
    for dist, name, t, lat, lon in items:
        if name in seen:
            continue
        seen.add(name)
        extra = []
        if t.get("name:en") and t.get("name:en") != name:
            extra.append(t["name:en"])
        if t.get("opening_hours"):
            extra.append("часы: " + t["opening_hours"])
        if t.get("check_date") or t.get("check_date:opening_hours"):
            extra.append("проверено OSM: " + (t.get("check_date:opening_hours") or t.get("check_date")))
        if t.get("website") or t.get("contact:website"):
            extra.append(t.get("website") or t.get("contact:website"))
        if t.get("wikipedia"):
            extra.append("wiki: " + t["wikipedia"])
        print(f"{dist:5.0f} м · {name} · {_osm_type(t)}" + (" · " + " · ".join(extra) if extra else ""))
        print(f"        pin: {gmaps_search(name, lat, lon)}")
        n += 1
        if n >= a.limit:
            break
    if n == 0:
        print("Ничего не найдено (OSM в этом районе может быть беден — ищите в вебе).")
    print("\nВажно: OSM не гарантирует, что место работает сейчас. Проверяйте свежие упоминания/отзывы.")


# ---------------------------------------------------------------- wiki
def cmd_wiki(a):
    out = []
    for lang in a.lang.split(","):
        q = urllib.parse.urlencode({"action": "query", "list": "geosearch", "gscoord": f"{a.lat}|{a.lon}",
                                    "gsradius": a.radius, "gslimit": a.limit, "format": "json"})
        url = f"https://{lang}.wikipedia.org/w/api.php?" + q
        try:
            d = _get(url, tries=2)
        except FetchError as e:
            _fail(url, e)
        for g in d.get("query", {}).get("geosearch", []):
            out.append((g["dist"], lang, g["title"]))
    for dist, lang, title in sorted(out):
        print(f"{dist:6.0f} м · [{lang}] {title} · https://{lang}.wikipedia.org/wiki/{urllib.parse.quote(title.replace(' ', '_'))}")
    if not out:
        print("Статей рядом нет.")


# ---------------------------------------------------------------- geocode
_last_nominatim = [0.0]


def geocode(query: str) -> tuple[float, float, str] | None:
    wait = 1.1 - (time.time() - _last_nominatim[0])
    if wait > 0:
        time.sleep(wait)
    _last_nominatim[0] = time.time()
    url = "https://nominatim.openstreetmap.org/search?" + urllib.parse.urlencode({"q": query, "format": "jsonv2", "limit": 1})
    try:
        d = _get(url)
    except FetchError as e:
        _fail(url, e)
    if not d:
        return None
    return float(d[0]["lat"]), float(d[0]["lon"]), d[0].get("display_name", query)


def cmd_geocode(a):
    url = "https://nominatim.openstreetmap.org/search?" + urllib.parse.urlencode({"q": a.query, "format": "jsonv2", "limit": a.limit})
    try:
        d = _get(url)
    except FetchError as e:
        _fail(url, e)
    for r in d:
        print(f"{float(r['lat']):.6f},{float(r['lon']):.6f} · {r.get('type')} · {r.get('display_name')}")
    if not d:
        print("Не найдено.")


# ---------------------------------------------------------------- points
def parse_point(s: str) -> tuple[float | None, float | None, str]:
    """'lat,lon@Name' | 'lat,lon' | 'Name' -> (lat, lon, name)."""
    name = s
    coord = s
    if "@" in s:
        coord, name = s.split("@", 1)
    try:
        la, lo = (float(x) for x in coord.split(","))
        return la, lo, (name if "@" in s else f"{la:.5f},{lo:.5f}")
    except ValueError:
        return None, None, s


def resolve(points: list[str], need_coords: bool):
    res = []
    for p in points:
        la, lo, name = parse_point(p)
        if la is None and need_coords:
            g = geocode(name)
            if not g:
                raise SystemExit(f"Не удалось геокодировать: {name}. Дайте координаты 'lat,lon@{name}'.")
            la, lo = g[0], g[1]
        res.append((la, lo, name))
    return res


# ---------------------------------------------------------------- walk (OSRM foot)
def cmd_walk(a):
    pts = resolve(a.points, need_coords=True)
    coords = ";".join(f"{lo},{la}" for la, lo, _ in pts)
    url = f"https://routing.openstreetmap.de/routed-foot/route/v1/foot/{coords}?overview=false&steps=false"
    try:
        d = _get(url)
    except FetchError as e:
        _fail(url, e)
    if d.get("code") != "Ok":
        raise SystemExit(f"Маршрут не построен: {d.get('code')} {d.get('message', '')}")
    r = d["routes"][0]
    total_min = r["duration"] / 60
    print(f"Итого: {r['distance'] / 1000:.1f} км, ~{total_min:.0f} мин чистой ходьбы по OSM "
          f"(реалистично ×1.3 с остановками/фото ≈ {total_min * 1.3:.0f} мин).")
    for i, leg in enumerate(r["legs"]):
        print(f"  {pts[i][2]} → {pts[i + 1][2]}: {leg['distance'] / 1000:.2f} км, ~{leg['duration'] / 60:.0f} мин")
    print("Учитывайте подъёмы/ступени и высоту: OSM-время их почти не учитывает.")


# ---------------------------------------------------------------- links
def _gm_point(la, lo, name):
    return f"{la},{lo}" if la is not None else name


def gmaps_dir(points, mode="walking"):
    o, dst, mid = points[0], points[-1], points[1:-1]
    q = {"api": "1", "origin": _gm_point(*o), "destination": _gm_point(*dst), "travelmode": mode}
    if mid:
        q["waypoints"] = "|".join(_gm_point(*p) for p in mid)
    return "https://www.google.com/maps/dir/?" + urllib.parse.urlencode(q, safe=",")


def cmd_links(a):
    pts = resolve(a.points, need_coords=False)
    if len(pts) < 2:
        raise SystemExit("Нужно минимум 2 точки.")
    mode = a.mode
    print("Google Maps (весь маршрут; в приложении до 9 промежуточных точек):")
    print("  " + gmaps_dir(pts, mode))
    if len(pts) - 2 > 3:
        print("Google Maps по частям (≤3 промежуточные точки — надёжно в мобильном браузере):")
        step = 4  # origin + 3 waypoints, next chunk starts at previous chunk's end
        i, part = 0, 1
        while i < len(pts) - 1:
            chunk = pts[i:i + step + 1]
            print(f"  Часть {part}: {chunk[0][2]} → {chunk[-1][2]}\n    {gmaps_dir(chunk, mode)}")
            i += step
            part += 1
    apple_mode = {"walking": "walking", "driving": "driving", "transit": "transit", "bicycling": "cycling"}[mode]
    aq = [("source", _gm_point(*pts[0])), ("destination", _gm_point(*pts[-1]))]
    aq += [("waypoint", _gm_point(*p)) for p in pts[1:-1]]
    aq.append(("mode", apple_mode))
    print("Apple Maps (iOS 18.4+):\n  https://maps.apple.com/directions?" + urllib.parse.urlencode(aq, safe=","))
    if all(p[0] is not None for p in pts):
        om = "om://map?v=1&" + "&".join(f"ll={la},{lo}&n={urllib.parse.quote(n)}" for la, lo, n in pts)
        print("Organic Maps (офлайн-карта с точками):\n  " + om)
    print("Отдельные точки (проверить часы/отзывы в один тап):")
    for la, lo, n in pts:
        is_coord_only = la is not None and n == f"{la:.5f},{lo:.5f}"
        print(f"  {n}: {gmaps_search(f'{la},{lo}') if is_coord_only else gmaps_search(n)}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)

    w = sp.add_parser("weather"); w.add_argument("lat", type=float); w.add_argument("lon", type=float)
    w.add_argument("--days", type=int, default=2); w.set_defaults(f=cmd_weather)

    n = sp.add_parser("nearby"); n.add_argument("lat", type=float); n.add_argument("lon", type=float)
    n.add_argument("--kind", default="all", help=f"через запятую: {', '.join(KINDS)} | all")
    n.add_argument("--radius", type=int, default=800); n.add_argument("--limit", type=int, default=25)
    n.set_defaults(f=cmd_nearby)

    k = sp.add_parser("wiki"); k.add_argument("lat", type=float); k.add_argument("lon", type=float)
    k.add_argument("--lang", default="ru,en"); k.add_argument("--radius", type=int, default=2000)
    k.add_argument("--limit", type=int, default=10); k.set_defaults(f=cmd_wiki)

    g = sp.add_parser("geocode"); g.add_argument("query"); g.add_argument("--limit", type=int, default=5)
    g.set_defaults(f=cmd_geocode)

    r = sp.add_parser("walk"); r.add_argument("points", nargs="+"); r.set_defaults(f=cmd_walk)

    li = sp.add_parser("links"); li.add_argument("points", nargs="+")
    li.add_argument("--mode", default="walking", choices=["walking", "driving", "transit", "bicycling"])
    li.set_defaults(f=cmd_links)

    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    sys.exit(main())
