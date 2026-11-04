#!/usr/bin/env python3
"""Собирает Skill «guide» из единого источника правды.

Источник:  guide/project/INSTRUCTIONS.md  (ядро правил — то же, что в инструкциях Проекта)
           .claude/skills/guide/references/*.md  (справочники)
           guide/tools/geo.py                   (скрипт)
Результат: .claude/skills/guide/SKILL.md      (для Claude Code в этом репозитории)
           .claude/skills/guide/scripts/geo.py
           guide/dist/guide-skill.zip         (загрузить в claude.ai → Customize → Skills)

Запуск: python3 guide/build.py
"""
from __future__ import annotations

import pathlib
import shutil
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "guide" / "project" / "INSTRUCTIONS.md"
SKILL_DIR = ROOT / ".claude" / "skills" / "guide"
DIST = ROOT / "guide" / "dist" / "guide-skill.zip"

FRONTMATTER = """---
name: guide
description: Персональный гид и построитель маршрутов. Используй, когда человек спрашивает, куда пойти или что поделать (сейчас, сегодня, на выходных), где поесть или выпить кофе, просит прогулку, маршрут, план дня или поездки на несколько дней, хочет «что-то новое» в своём городе, делится, где он сейчас и сколько у него времени, или рассказывает, как сходил куда-то.
---

<!-- Сгенерировано guide/build.py из guide/project/INSTRUCTIONS.md — правьте источник, а не этот файл. -->

# Гид

"""

FILES = """

<справочники>
Читай по необходимости (в Skill — папка references/, в Проекте — файлы знаний с теми же именами):
- references/sources.md — где и как искать по типам запросов и регионам, шаблоны запросов на местных языках, проверка статуса мест.
- references/routes.md — форматы ссылок (Google / Apple / Organic Maps, KML), арифметика времени, шаблон события календаря, артефакт-план, офлайн-пакет.
- references/memory.md — профиль, журнал, «Сейчас», правила записи в память, сведение журнала, знакомство.
- references/trip-planning.md — интервью и сборка плана поездки на несколько дней.
- scripts/geo.py — если можно выполнять код с доступом в сеть (Claude Code): погода и закат, места рядом из OSM, Википедия рядом, реальное пешее время, ссылки маршрута с разбивкой. Без ключей API. Если сервис недоступен из сети, скрипт печатает URL — открой его веб-фетчем.
</справочники>
"""


def main() -> None:
    body = SRC.read_text(encoding="utf-8").strip()
    SKILL_DIR.mkdir(parents=True, exist_ok=True)
    (SKILL_DIR / "SKILL.md").write_text(FRONTMATTER + body + FILES, encoding="utf-8")

    scripts = SKILL_DIR / "scripts"
    scripts.mkdir(exist_ok=True)
    shutil.copy2(ROOT / "guide" / "tools" / "geo.py", scripts / "geo.py")

    DIST.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(DIST, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(SKILL_DIR.rglob("*")):
            if f.is_file() and "__pycache__" not in f.parts:
                z.write(f, pathlib.Path("guide") / f.relative_to(SKILL_DIR))
    size = (SKILL_DIR / "SKILL.md").stat().st_size
    print(f"SKILL.md: {size} байт; zip: {DIST.relative_to(ROOT)} ({DIST.stat().st_size} байт)")


if __name__ == "__main__":
    main()
