# Data sources, search strategies and free tools for an AI local guide (Claude app + Claude Code), as of 2026-11-04

Notes on method: Besides web research, I ran **live test fetches on 2026-11-04 with Claude Code's WebFetch tool** against many candidate sources. These are cited as "[Test fetch](URL)". Caveat: Claude Code's WebFetch and the Claude mobile app's web fetch are related but not identical tools. Blocks, user agents and URL rules may differ, so treat the test results as strong hints, not guarantees, for the mobile app. Legend used below: **APP** = works with plain web search/fetch in the Claude app; **CODE** = needs Claude Code (scripts, curl, local MCP); **KEY** = needs an API key or account; **MCP** = needs an MCP server/connector.

## Key question 0 (cross-cutting): What can Claude actually reach from the mobile app vs Claude Code?

### Takeaway
In the Claude app, web fetch can only open URLs that already appeared in the conversation: in a user message, a search result or an earlier fetch. URLs are capped at 250 characters, and JavaScript is not rendered. So the app **cannot construct API calls itself** (Overpass, Open-Meteo, Wikipedia GeoSearch) unless the user pastes the URL. Claude Code has no such limit and can call open APIs directly. The app does have its own location tool and interactive map on iOS, plus official travel connectors (Tripadvisor, Booking.com, Expedia, AllTrails, Viator).

### Cited Findings
- Claude's web fetch "can only fetch URLs that have previously appeared in the conversation context": URLs in user messages, in client-side tool results, and in previous web search or web fetch results. It "cannot fetch URLs that appear only in Claude's own output or only in the system prompt." — [Anthropic web fetch docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)
- The same docs list error codes `url_too_long` ("URL exceeds maximum length (250 characters)") and `url_not_allowed` (blocked by domain rules, "robots.txt", or "URLs that appear to contain a credential you did not provide"). Web fetch "currently does not support websites dynamically rendered with JavaScript". Results are cached, so "content returned might not always reflect the latest version". — [Anthropic web fetch docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)
- Fetched URLs that contain an API key are refused "unless that credential appears in the system prompt or in the text of a user message". — [Anthropic web fetch docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)
- In Claude Code, WebFetch successfully called self-constructed open-API URLs: Overpass (OSM cafés within 500 m of Thamel), Wikipedia GeoSearch, and Open-Meteo (Kathmandu sunrise 06:16, sunset 17:18 on 2026-11-04). — [Test fetch Overpass](https://overpass-api.de/api/interpreter?data=[out:json][timeout:25];node["amenity"="cafe"](around:500,27.7149,85.3123);out%2010;), [Test fetch Wikipedia GeoSearch](https://en.wikipedia.org/w/api.php?action=query&list=geosearch&gscoord=27.7149|85.3123&gsradius=2000&gslimit=10&format=json), [Test fetch Open-Meteo](https://api.open-meteo.com/v1/forecast?latitude=27.71&longitude=85.31&daily=sunrise,sunset,precipitation_probability_max,temperature_2m_max&timezone=auto&forecast_days=3)
- Claude iOS app: "When Claude suggests locations, they can be displayed on an interactive map". You can "Select a location to open it in Apple Maps for navigation" and "Get turn-by-turn directions directly from the map". The location tool is "Current location only when relevant to your request". It is available on all plans, except that "Members of Team or Enterprise plans can't access the location tool at this time." — [Claude Help Center: Using Claude with iOS apps](https://support.claude.com/en/articles/11869619-using-claude-with-ios-apps)
- Claude mobile got location and calendar access on iOS and Android in September 2025. — [AlternativeTo news](https://alternativeto.net/news/2025/9/claude-for-mobile-launches-location-and-calendar-access-on-ios-and-android)
- A Japanese tech outlet (13 Mar 2026) reports that Claude added "Google Maps-based map display". With web search on, a place query can bring up an interactive map, and pins show directions, contact info and image links. The outlet says some visual features (weather, recipes) are web/desktop only and show as text on mobile. It does not say which platforms get the map. — [smhn.info](https://smhn.info/202603-claude-google-maps-interactive)
- Claude's connector directory includes travel connectors: Booking.com, Expedia, Tripadvisor, Trivago, Wyndham, lastminute.com, Turkish Airlines, Viator and AllTrails. Per this source, Tripadvisor offers "reviews and attractions" and AllTrails offers trail search with current conditions. Booking/Expedia/Tripadvisor/AllTrails are described as needing OAuth to an existing account, and purchases need confirmation. — [beginnersinai.org (30 Jun 2026)](https://beginnersinai.org/claude-connectors-for-travel-and-life/). Contradicting source: one roundup says Expedia, Booking.com, Tripadvisor, Zillow and AllTrails work without an account at the service. — [dirjournal Claude connectors list](https://www.dirjournal.com/blogs/claude-connectors-list)
- Booking.com and TripAdvisor were added to the Claude directory in an April 2026 batch, and the directory passed 200 connectors (counts vary by source). — [Tom's Guide](https://www.tomsguide.com/ai/claude-now-connects-to-more-everyday-apps-heres-what-you-can-do-now); [dirjournal](https://www.dirjournal.com/blogs/claude-connectors-list)
- claude.ai chat's code-execution sandbox has an "Allow network egress" toggle, which is separate from Claude Code. This is a secondary source; details were not verified against Anthropic docs. — [Classmethod (JP), June 2026](https://dev.classmethod.jp/articles/claude-chat-code-execution-misconceptions/)
- Users report that the Claude Code (web) "All domains" egress setting still enforced a hardcoded allowlist. Unconfirmed bug report. — [claudeissues.com](https://claudeissues.com/issue/34690-bug-allow-network-egress-all-domains-setting-not-reflected-in-session-proxy-jwt)

### Inferences
- **Practical rule for the app:** search first, then fetch pages that come up in search results. For API-style lookups (Overpass, Open-Meteo, GeoSearch), either (a) the user pastes a URL template once, or (b) use Claude Code or a connector. Long Overpass queries will exceed the 250-character URL cap anyway.
- The app's built-in location tool and map are the cheapest "here and now" path: Claude gets coordinates, suggests places and renders a map, and the user taps through to Apple Maps on iOS.
- Official connectors (Tripadvisor, AllTrails, Viator) are free to use with the Claude subscription, though some need an account at the service. They are the most reliable way to get structured reviews/attractions/trails inside the mobile app without running servers.

### Gaps
- I could not verify from an official Anthropic page whether the consumer Claude app's web fetch uses exactly the API's URL-validation rules. The API docs strongly suggest it does.
- I could not confirm whether the "Google Maps-based" map in chat appears on Android or iOS, or what data source it uses.
- Not verified: whether custom remote MCP connectors added on claude.ai web are usable from the mobile app, and on which plans.

## Key question 1: Community and editorial sources (Reddit, Wikivoyage, Atlas Obscura, Spotted by Locals, blogs, forums, Russian-language sources): signal quality and accessibility

### Takeaway
Reddit is the best "real people, recent" signal, but it is **blocked for direct fetch** and its API is closing to new users, so in the app it is only reachable through search snippets and mirrors. Wikivoyage is fully fetchable and has dated listings. Atlas Obscura and Spotted by Locals return 403 to the fetcher. Telegram public channels are fetchable through `t.me/s/<channel>` and are the strongest Russian-language live source. Tripster (Russian-speaking local guides, including Kathmandu) is fully fetchable.

### Cited Findings
- **Reddit (direct):** Claude Code WebFetch refused both `www.reddit.com` and `old.reddit.com` ("Claude Code is unable to fetch from www.reddit.com"), including the `.json` search endpoint. — [Test fetch reddit](https://www.reddit.com/r/Kathmandu/search/?q=momo&restrict_sr=1); [Test fetch old.reddit JSON](https://old.reddit.com/r/Nepal/search.json?q=kathmandu+cafe&restrict_sr=1&sort=new)
- **Reddit (via search):** A `site:reddit.com r/Kathmandu cafe` web search returned no reddit.com pages. The closest hit was a third-party mirror of a June 2026 r/Kathmandu thread recommending Petals Cafe (Thamel) and Kastha Vista (Nagarjun hill). The rest were SEO aggregators ("Reddit-backed" tabiji pages) and Foursquare lists. — [Search result: mirror snapshot](https://reddit.sentinel-team.org/posts/1u2kj8o/snapshots/2026-06-12T23%3A23%3A24.685022Z); [tabiji aggregator](https://tabiji.pages.dev/popular-picks/kathmandu-coffee-shops)
- **Reddit API:** The free tier is 100 queries/minute per OAuth client for approved non-commercial use, and approval is manual. Third-party sites report that new public API access requests stop on **31 Oct 2026**, with remaining public access ending March 2027. Not confirmed on Reddit's own docs. — [apiserpent](https://apiserpent.com/blog/free-reddit-api); [redditapis.com](https://www.redditapis.com/blogs/reddit-api-pricing-2026)
- **Reddit MCP:** `reddit-no-auth-mcp-server` (PyPI) needs no API key, is read-focused (search, search_subreddit, browse) and runs via `uvx`. A 2026 roundup (by a competing vendor) says Reddit's 2026 update broke most Reddit MCP servers. — [PyPI reddit-no-auth-mcp-server](https://pypi.org/project/reddit-no-auth-mcp-server/); [bigideasdb roundup](https://bigideasdb.com/best-reddit-mcp-servers)
- **Wikivoyage:** Fully fetchable. The Kathmandu article (~105k chars) has Eat/Drink/See/Do sections with prices (e.g., momo "Rs150–250 for a dozen") and per-listing "(updated Mar 2026)"-style markers, although the Kathmandu Eat section is generic and names few restaurants. — [Test fetch Wikivoyage Kathmandu](https://en.wikivoyage.org/wiki/Kathmandu)
- **Atlas Obscura:** HTTP 403 Forbidden to the fetcher. — [Test fetch](https://www.atlasobscura.com/things-to-do/kathmandu-nepal)
- **Spotted by Locals:** HTTP 403 Forbidden to the fetcher. — [Test fetch](https://www.spottedbylocals.com/)
- **Telegram public channels:** `t.me/s/<channel>` returns the web preview with recent posts. For example, @vandroukiru (~403K subs) showed its latest posts with message IDs and times, though without full calendar dates in the preview. `t.me/s/<user-or-bot>` only shows a "Contact @..." stub. — [Test fetch t.me/s/vandroukiru](https://t.me/s/vandroukiru); [Test fetch t.me/s/kathmandu](https://t.me/s/kathmandu)
- **TGStat (Telegram channel directory):** HTTP 403 to the fetcher. — [Test fetch tgstat search](https://tgstat.ru/search?q=Бали)
- **Tripster (Russian-language private tours by local Russian-speaking guides):** Fully fetchable. The Kathmandu page lists 16 excursions with prices ($40 transfer to $650 for a 10-hour tour), ratings, review counts and walking formats (e.g., "Нетуристический Катманду", 4 h walking). The page cites 109 reviews. — [Test fetch Tripster Kathmandu](https://experience.tripster.ru/experience/Kathmandu/)
- **Russian-language search results:** A Russian-language query ("Катманду куда сходить советы 2026 телеграм блог") returned almost entirely English results, with no Telegram blogs surfaced. — [Search: samokatus.ru minifaq among results](https://samokatus.ru/minifaq-katmandu)
- **English "hidden gems" queries surface SEO content:** "Bali hidden gems … reddit" returned mostly Agoda "Discover 10 Hidden Gems" listicles and no real r/bali or FB posts. — [Agoda listicle example](https://www.agoda.com/travel-guides/indonesia/bali/discover-10-hidden-gems-in-bali-unique-places-to-visit-in-bali-indonesia)
- **Local editorial in India:** LBB (lbb.in) Bangalore is fetchable and has neighbourhood-level guides ("10 Best Cafes In Indiranagar…"), but no visible publication dates. — [Test fetch LBB](https://lbb.in/bangalore/)
- **Local media in Nepal:** OnlineKhabar English publishes a street-food guide (e.g., Om Panipuri Chat Center on New Road; sekuwa in Basantapur). — [OnlineKhabar English](https://english.onlinekhabar.com/best-street-food-in-kathmandu-guide.html)

### Inferences
- **Signal ranking for "non-obvious and current":** (1) Telegram local channels and chats (RU expat communities in Bali, Nepal, Thailand, Vietnam), fetchable via `t.me/s/`. (2) Reddit city subs, reachable only through search snippets, mirrors or Claude Code MCP. (3) Local-language media and blogs. (4) Wikivoyage, for structure, logistics and dated listings. (5) Global editorial (Atlas Obscura, Spotted by Locals, Culture Trip), which is blocked or stale, so use search snippets only.
- **Reddit query templates for web search:** `site:reddit.com/r/<sub> <topic> <year>`, `"<neighbourhood>" reddit recommendations`, `<city> "underrated" reddit`. Useful subs include r/Nepal, r/Kathmandu, r/NepaliFood, r/bali, r/indonesia, r/india plus city subs (r/mumbai, r/bangalore, r/delhi), r/JapanTravel, r/Tokyo, r/koreatravel, r/seoul, r/travelchina, r/Thailand, r/ThailandTourism, r/VietNam, r/solotravel. Expect mirrors and aggregators rather than reddit.com itself in results. These subreddit names are my suggestions; I did not verify each one in this research.
- **Telegram tactic:** find channel handles by web search (e.g., `"t.me" Убуд кафе`, `телеграм канал Бали афиша`), then fetch `t.me/s/<handle>`. Do not try to scrape chats (groups): they have no `/s/` preview. Directories like TGStat are blocked.
- **Russian sources:** Tripster (tours, and guides' tips inside listings), Vandrouki (deals), Russian expat Telegram channels, and personal blogs found through search. Because web search skews to English/US, add Russian-specific terms ("отзыв", "живём на Бали", "чат", "лайфхак") or `site:` filters such as `site:t.me`, `site:pikabu.ru`, `site:vc.ru`, `site:dzen.ru`, `site:tripster.ru`.

### Gaps
- Could not verify which specific Russian-language Telegram channels for Kathmandu, Bali or Goa are active and high quality, because the directory (TGStat) is blocked and search surfaced none.
- Facebook groups: not tested. They are login-walled, so they are almost certainly not fetchable. No source checked.
- TripAdvisor forums and Lonely Planet's Thorn Tree successor: not tested in this pass.
- Yandex Travel journal, vc.ru and Pikabu fetchability: not tested.

## Key question 2: Region-specific platforms and local-language search: which are accessible to an AI via web fetch?

### Takeaway
Fetchable without tricks: **Tabelog** (Japan, with scores), **2GIS** (Russia/CIS, with ratings and review counts), **Afisha** (Russia, events), **Wongnai** (Thailand, ratings plus open/closed), **LBB** (India, editorial). Blocked or JS-only: **Naver search** (blocked), **Foody.vn** (JS shell), **Zomato** (503), **Google Maps place pages** (empty shell), and **Xiaohongshu** (redirects to rednote.com, untested). Local-language queries work well where local media is strong (for example, Indonesian "kuliner" queries return detik.com and katadata).

### Cited Findings
- **Japan, Tabelog:** The English listing page loaded with names and scores (e.g., Raa Menya Shima 4.07; Ginza Hachigo 3.92) out of 7,076 Tokyo ramen listings. — [Test fetch Tabelog](https://tabelog.com/en/tokyo/rstLst/ramen/)
- Tabelog's rating "is not a simple average"; users have different levels of influence, and over 4.00 is the top ~0.07%. Guides say 3.5+ is very good and Google ratings in Japan run higher than Tabelog's. — [Tabelog help: Ratings](https://tabelog.com/en/help/score); [Just One Cookbook](https://www.justonecookbook.com/tabelog-japan-restaurant-food-guide/); [real-japan-guide](https://real-japan-guide.com/?p=2285)
- **Korea, Naver:** `search.naver.com` blog search was blocked for the fetcher ("unable to fetch"). — [Test fetch Naver](https://search.naver.com/search.naver?where=blog&query=성수동+카페)
- Naver Map separates receipt-verified visitor reviews (방문자 리뷰) from blog reviews (블로그 리뷰), which "are often paid promotions". It can translate reviews via Papago. A government survey found 56.2% of foreign visitors used Naver Map vs 33.9% Google Maps. One guide claims Naver might show 600 reviews where Google shows 40. — [seoulstart guide](https://seoulstart.com/guides/finding-good-restaurants-korea-guide); [KED Global 2024](https://m.kedglobal.com/newsView/ked202410020014)
- Kakao Map is perceived to have fewer incentives for businesses to solicit positive reviews (opinion, not measured). — [haniseoul](https://www.haniseoul.com/travels/korea/map-app-korea)
- **China:** Guides recommend Amap for navigation and its English version (2025), Dianping for choosing restaurants, and Xiaohongshu/Rednote for recent photo-heavy tips, which "can be promotion-driven". Google Maps is generally not usable in China. — [chinaguidelines](https://chinaguidelines.com/en/posts/finding-good-restaurant); [wanderinchina Dianping guide 2026](https://www.wanderinchina.com/survival-guide/useful-mobile-apps/dazhong-dianping-meituan/)
- The Shanghai government (13 Jul 2026) says digital map services now support multiple languages, including English, Japanese, **Russian**, French, Spanish and Korean. — [english.shanghai.gov.cn](https://english.shanghai.gov.cn/en-EasyShanghai/20260713/379bcea6e1bd4defaa7db2451d68d3dd.html)
- `xiaohongshu.com/explore` 302-redirects to `rednote.com/explore`. Content was not tested beyond that. — [Test fetch](https://www.xiaohongshu.com/explore)
- **Russia/CIS, 2GIS:** A search page ("кофейня", Moscow) loaded with 4,925 places, ratings and review counts, with ads marked "Реклама". No captcha. — [Test fetch 2GIS](https://2gis.ru/moscow/search/кофейня)
- **Russia, Yandex Maps:** `yandex.ru/maps/...` 302-redirects to `yandex.com/maps/...`. The redirect was not followed, so the result is unknown. — [Test fetch](https://yandex.ru/maps/213/moscow/search/кофейня/)
- **Russia, Afisha:** Loaded with real events, dates, venues and prices. — [Test fetch Afisha](https://www.afisha.ru/msk/)
- **Thailand, Wongnai:** The listing loaded with names, ratings, "open/closed" status at capture time, and sponsored entries marked. — [Test fetch Wongnai](https://www.wongnai.com/restaurants?regions=9681)
- **Vietnam, Foody.vn:** A JavaScript shell with unrendered template placeholders and no listings. — [Test fetch Foody](https://www.foody.vn/ho-chi-minh)
- **India, Zomato:** HTTP 503 to the fetcher. — [Test fetch Zomato](https://www.zomato.com/kathmandu)
- **Indonesia, local-language search:** "kuliner enak Ubud warung lokal 2026" returned Indonesian media (Katadata, Jan 2026: "25 Destinasi Kuliner di Ubud"; detik Bali on Warung Kuah Pindang) and local-insider sites (ubudhood "Where Locals Eat"). — [Katadata](https://katadata.co.id/lifestyle/wisata-dan-kuliner/6965c1cdafcaf/25-destinasi-kuliner-di-ubud-yang-istimewa-wajib-dicoba); [detik Bali](https://www.detik.com/bali/kuliner/d-7727340/warung-kuah-pindang-pilihan-tepat-untuk-wisata-kuliner-di-ubud); [ubudhood](https://www.ubudhood.com/eat-drink/local-food-in-ubud)
- **Nepal:** A search for Kathmandu food via FB groups, Foodmandu or Reddit surfaced only blogs and guide sites, with no FB or Foodmandu content. — [OnlineKhabar](https://english.onlinekhabar.com/best-street-food-in-kathmandu-guide.html); [kimkim](https://kimkim.com/c/best-places-to-eat-in-kathmandu)

### Inferences
- **Per-region source map (my synthesis from the tests above):**

| Region | Best signal for food/places | AI reachability | Query tactic |
|---|---|---|---|
| Japan | Tabelog (+ Google Maps for hours) | APP (fetch tabelog.com/en and the JP pages) | `site:tabelog.com <area> <genre>`; JP keywords: 百名店, 食べログ, 地元民, 穴場 |
| Korea | Naver Map visitor reviews, Naver Blog, Kakao Map | Naver blocked for fetch, so use web search snippets or `site:blog.naver.com` | KR keywords: 맛집, 카페 추천, 현지인, 숨은 |
| China | Dianping, Xiaohongshu/Rednote, Amap | Mostly app-only and login-walled; use search snippets | CN keywords: 必吃, 攻略, 小众, 本地人推荐, `大众点评 <city>` |
| Russia/CIS | Yandex Maps, 2GIS, Afisha, Telegram | 2GIS and Afisha APP-fetchable; Yandex unclear | RU: "куда сходить", "атмосферное место", "не туристическое" |
| Thailand | Wongnai, Facebook pages | Wongnai APP-fetchable (shows open/closed) | TH: ร้านอร่อย, คาเฟ่, ลับ |
| Vietnam | Foody/ShopeeFood, FB groups | Foody is a JS shell, so search snippets only | VN: quán ngon, quán cà phê đẹp, ăn gì ở |
| Indonesia/Bali | Local media (detik, Katadata), Google Maps reviews, IG/TikTok, RU Telegram | Indonesian media APP-fetchable | ID: kuliner, warung enak, tempat nongkrong, hidden gem, viral |
| India | LBB, Zomato/District, city subreddits | LBB APP-fetchable; Zomato 503 | `site:lbb.in <city> <topic>`; Hindi: सबसे अच्छा, स्ट्रीट फूड |
| Nepal | Local media (OnlineKhabar, Kathmandu Post), r/Nepal, r/Kathmandu, Tripster (RU) | Media and Tripster APP-fetchable; Reddit only via snippets | Nepali: मिठो खाना, खाजा घर, घुम्ने ठाउँ; Newari: समय बजि (samay baji) |

- In regions where Google Maps is weak (Korea, China), the AI should state that the dominant local platform is not machine-readable. It should then fall back to search snippets plus Wikivoyage/OSM for logistics.

### Gaps
- Not tested: Retty, Kakao Map web, Dianping web, Amap web, ShopeeFood, District (Zomato), Swiggy, Kathmandu Post, Nepali-language sites, Instagram, and TikTok. IG and TikTok are almost certainly login-walled or JS-only, but I did not test them.
- Local-language keyword lists are my own suggestions, not sourced from usage studies.

## Key question 3: Events and "what's on now"

### Takeaway
Free, fetchable event sources exist but are fragmented: **allevents.in** (works for Kathmandu and broad Asian coverage), **Afisha** (Russia), and **Telegram channels**. **Resident Advisor** blocks the fetcher (403). **Eventbrite's public search API** has been dead since 2019, and **Meetup's API** is Pro-gated. Luma was not verified.

### Cited Findings
- allevents.in/kathmandu loaded with current events and dates (e.g., "Nhu da Bhintuna Cycle Rally Nepal Sambat 1147", Sat 07 Nov; AGRIMECH Expo, 20 Nov). — [Test fetch allevents](https://allevents.in/kathmandu)
- Resident Advisor (ra.co) returned HTTP 403. — [Test fetch RA](https://ra.co/events/id/bali)
- Afisha Moscow loaded with dated events and prices. — [Test fetch Afisha](https://www.afisha.ru/msk/)
- Eventbrite: "Access to the Eventbrite Event Search API will be shut down at 11:59 pm PT on Thursday, December 12, 2019". — [Eventbrite API group announcement](https://groups.google.com/g/eventbrite-api/c/FT2MsDswdrA); [Eventbrite changelog](https://www.eventbrite.co/platform/docs/changelog)
- Meetup: the legacy REST API was retired, and Meetup Pro is required for API event management. Sources conflict on whether free accounts can do basic search. — [logiover guide](https://logiover.pages.dev/guides/meetup-api-alternative-event-group-data/); [rapidevelopers](https://rapidevelopers.com/bolt-ai-integrations/meetup)
- Luma: `luma.com/kathmandu` returned 404 (wrong URL guess). City discovery URLs remain unverified. — [Test fetch](https://luma.com/kathmandu)

### Inferences
- "What's on" recipe for the app: web search `<city> events this week <month year>`, plus `site:allevents.in <city>`, plus `site:t.me <city> афиша` or `<city> events telegram`. For Russia use `site:afisha.ru`. For nightlife, search `"ra.co" <city>` and read snippets only. Add the local festival calendar: for Nepal, Nepal Sambat/Tihar dates are visible on allevents (e.g., the "Nepal Sambat 1147" event).
- Treat all event data as needing date re-confirmation. Event pages are often stale or recurring.

### Gaps
- Luma's public discover/city pages and their fetchability: not verified.
- Facebook Events: not tested, and almost certainly login-walled.
- Local Asian ticketing (BookMyShow, District, Ticketmelon, Klook) was not tested.

## Key question 4: Free APIs and open data (OSM/Overpass/Nominatim, Overture, Foursquare, OpenTripMap, Wikidata/Wikipedia, Open-Meteo, routing)

### Takeaway
Fully free, keyless and usable today: **Overpass** (≈10k requests/day guideline), **Nominatim** (1 req/s, no autocomplete, must cache), **Wikipedia GeoSearch**, **Open-Meteo** (<10k/day, non-commercial, CC BY 4.0), and the **OSRM/FOSSGIS demo** (1 req/s, non-commercial). These need a free key: **OpenRouteService** (2,000 directions/day), **GraphHopper** (500 credits/day, 5 points/request), **OpenTripMap** (≈5,000/day, ODbL), **Foursquare Places** (free Pro calls; the size is disputed at 10k vs 500) and **Tripadvisor Content API** (5,000/month, credit card required). Google Maps Platform has generous free caps per SKU but requires billing.

### Cited Findings
- **Overpass public instance:** users are expected to send ≲10,000 requests/day and ≲1 GB/day. Requests wait up to 15 s for a slot. Rate refusals return HTTP 429, and the default timeout is 180 s / 512 MiB. Heavy apps should run their own instance. — [Overpass API docs: commons](https://dev.overpass-api.de/overpass-doc/en/preface/commons.html)
- **Nominatim:** "absolute maximum of 1 request per second". Results "must be cached". Autocomplete is prohibited, systematic queries (e.g., downloading all POIs in an area) are prohibited, a non-stock User-Agent is required, and attribution is required. — [OSMF Nominatim policy](https://operations.osmfoundation.org/policies/nominatim/)
- **OSM data quality for verification (Thamel test):** of 10 cafés returned, only 2 had `opening_hours`, and none had `check_date`. The response timestamp showed the OSM DB was current (2026-11-04). — [Test fetch Overpass](https://overpass-api.de/api/interpreter?data=[out:json][timeout:25];node["amenity"="cafe"](around:500,27.7149,85.3123);out%2010;)
- **Wikipedia GeoSearch:** keyless JSON of articles near a coordinate with distances (e.g., Kaiser Library 284 m, Ikha Pokhari 754 m from Thamel). — [Test fetch](https://en.wikipedia.org/w/api.php?action=query&list=geosearch&gscoord=27.7149|85.3123&gsradius=2000&gslimit=10&format=json)
- **Open-Meteo:** free use is non-commercial only (sites with ads or subscriptions count as commercial). Limits are <10,000 calls/day, 5,000/hour, 600/minute and 300,000/month, applied per IP and per app, under CC BY 4.0. — [Open-Meteo terms](https://open-meteo.com/en/terms). The test call returned sunrise/sunset and precipitation probability without a key. — [Test fetch](https://api.open-meteo.com/v1/forecast?latitude=27.71&longitude=85.31&daily=sunrise,sunset,precipitation_probability_max,temperature_2m_max&timezone=auto&forecast_days=3)
- **OpenRouteService:** the Standard plan is free with a key. Directions are 2,000/day and 40/min, and commercial use is not allowed on free tiers. — [openrouteservice plans (via search)](https://openrouteservice.org/plans/)
- **GraphHopper:** free (non-commercial) plan of 500 daily credits, 5 routing locations and 1 optimization vehicle per request. It "strictly blocks" after credits run out. — [GraphHopper docs: plans and rate limits](https://docs.graphhopper.com/openapi/section/plans-and-rate-limits); [GraphHopper pricing](https://www.graphhopper.com/pricing/)
- **OSRM demo / FOSSGIS (routing.openstreetmap.de):** reasonable non-commercial use, ≤1 request/second, no guarantees, and a valid User-Agent is required. — [OSRM wiki: API usage policy](https://github.com/Project-OSRM/osrm-backend/wiki/Api-usage-policy); [routing.openstreetmap.de about](https://routing.openstreetmap.de/about.html)
- **OpenTripMap:** data under ODbL, built from OSM, Wikidata, Wikipedia and Russian Ministry of Culture data. — [OpenTripMap product page](https://dev.opentripmap.org/product). The free plan is reportedly 5,000 requests/day at 10 req/s, non-commercial, with the key as an `apikey=` parameter. This comes from a secondary catalog, not the official page. — [api-evangelist catalog](https://raw.githubusercontent.com/api-evangelist/opentripmap/refs/heads/main/rate-limits/opentripmap-rate-limits.yml)
- **Foursquare Places API:** the official pricing page says "Enjoy up to 10,000 free calls on Pro endpoints", while its table shows "0 – 500 Calls" at $0.00 CPM. That is a contradiction on the official page. Premium endpoints (tips, photos) have no free band, starting at $18.75 CPM. — [Foursquare pricing](https://foursquare.com/pricing/). A third party reports 500 free calls under a "June 2026 pricing update". — [agentdeals Foursquare](https://agentdeals.dev/vendor/foursquare)
- **Foursquare OS Places (open dataset):** Apache 2.0 licence. The Hugging Face dataset is now gated (contact info required), releases are dated e.g. 2026-01-12, and the data is also on Snowflake. Size claimed >100M POIs, but only by a vendor blog. — [Hugging Face fsq-os-places](https://huggingface.co/datasets/foursquare/fsq-os-places); [openplacesapi blog](https://openplacesapi.com/blog/fsq-os-places-free-place-search)
- **Overture Maps Places:** has `operating_status` ('open', 'permanently_closed', 'temporarily_closed') and `confidence` (0–1). The 2026-05-20 release changed the default `operating_status` to null instead of open. — [Earth Engine Overture catalog](https://developers.google.com/earth-engine/datasets/catalog/overture-maps_places_place); [Overture 2026-05-20 release notes](https://docs.overturemaps.org/blog/2026/05/20/release-notes/)
- **Google Maps Platform free monthly caps per SKU:** Places (New) Text Search is unlimited for Essentials (IDs only), 5,000 for Pro and 1,000 for Enterprise. Place Details is 10,000 for Essentials, 5,000 for Pro and 1,000 for Enterprise. Compute Routes is 10,000 for Essentials, 5,000 for Pro and 1,000 for Enterprise. Geocoding, Static Maps and Dynamic Maps are 10,000 each. **Maps Embed is unlimited.** — [Google Maps Platform pricing](https://developers.google.com/maps/billing-and-pricing/pricing)
- **Tripadvisor Content API:** "We offer the first 5000 API calls for free every month". "You do need a credit card to sign up", and a max daily budget is required. Attribution per the display requirements is mandatory. — [Tripadvisor Content API FAQ](https://tripadvisor-content-api.readme.io/reference/faq). A third party claims the legacy Content API sunsets 31 Aug 2026, replaced by a "Terra API" with 1,000 free calls. This is unverified and conflicts with the FAQ. — [socialcrawl](https://www.socialcrawl.dev/blog/best-tripadvisor-data-apis-2026)

### Inferences
- **Cheapest robust stack for Claude Code:** Overpass (POIs, trails, viewpoints, `natural=peak`, `tourism=viewpoint`, `historic=*`), Wikipedia GeoSearch plus Wikidata (story-worthy sites), Open-Meteo (weather, sunrise/sunset for golden-hour walks), and ORS or GraphHopper (walking times; foot-hiking profile). For a single user's personal use, all of these stay well inside the free terms.
- Foursquare and Tripadvisor are "free with a key", but Tripadvisor needs a credit card and Foursquare's free volume is ambiguous. For a zero-cost personal guide, prefer the official Claude Tripadvisor connector over the API.
- Overture/FSQ OS Places are bulk datasets (Parquet). They suit Claude Code with DuckDB for an offline "all cafés in Ubud with confidence ≥ x" query, but they are not usable from the mobile app.

### Gaps
- Exact OpenTripMap limits are not confirmed on the official page.
- Wikidata SPARQL limits were not checked in this pass.
- GTFS/transit feeds for Asian cities (Kathmandu has none known; Bali none) were not researched.
- A sunrise-sunset dedicated API was not checked; Open-Meteo covers sunrise and sunset.

## Key question 5: MCP servers for travel (Google Maps, OSM, Foursquare, Tripadvisor, Airbnb, weather, search, Reddit): cost, auth, maintenance

### Takeaway
The only **official Google** option is the **Maps Grounding Lite MCP** (`https://mapstools.googleapis.com/mcp`). It offers 10k free requests/month (Essentials), but it needs a billing-enabled Cloud project, forbids the LLM from caching Maps content, and requires attribution. The free and keyless path is the **OSM MCP servers** (Overpass + Nominatim). For search, hosted MCPs with free tiers include Tavily (1,000 credits/mo, no card), Exa ($10/mo credits, no card), Jina (Reader keyless at 20 RPM) and Brave ($5/mo credits, card required). Community Airbnb, Tripadvisor and Reddit servers exist but are fragile or need keys.

### Cited Findings
- **Google Maps Grounding Lite:** the tools are `search_places` (AI summaries, place IDs, coordinates, `googleMapsLinks.placeUrl`; Essentials up to 5 places, Pro up to 10 plus review insights), `lookup_weather`, `compute_routes` (distance and duration, no turn-by-turn; Pro allows up to 25 stops), and `resolve_names`/`resolve_maps_urls`. "You must enable billing", although a demo key works for prototyping. Essentials is 10,000 free/month then $7/1k; Pro is 5,000 free then $14/1k, and Pro is a restricted-GA allowlist. The LLM "must not store Google Maps Content, cache it, or use it for training". Attribute to Google Maps and link `placeUrl`. Quota is 300 QPM. — [Google: Grounding Lite](https://developers.google.com/maps/ai/grounding-lite)
- Grounding Lite authentication is an API key in the `X-Goog-Api-Key` header, or OAuth, over Streamable HTTP. — [Grounding Lite MCP reference](https://developers.google.com/maps/ai/grounding-lite/reference/mcp?hl=de)
- **OSM MCP servers:**
  - Rusty0508/overpass-mcp: Python, no keys, Overpass + Nominatim, MIT, 8,000-char query cap.
  - GRABOSM/osm-mcp (Grab): Node, about 30 tools including `execute_overpass_query`, routing and geocoding, MIT.
  - cyanheads/openstreetmap-mcp-server: Streamable HTTP, 6 tools, 1 star.
  - nervsystems/osmmcp: Go, geocoding, routing, map images.
  
  [Glama overpass-mcp](https://glama.ai/mcp/servers/Rusty0508/overpass-mcp); [Glama GRABOSM/osm-mcp](https://glama.ai/mcp/servers/GRABOSM/osm-mcp/tree); [Glama cyanheads](https://glama.ai/mcp/connectors/io.github.cyanheads/openstreetmap-mcp-server); [LobeHub osmmcp](https://lobehub.com/en/mcp/nervsystems-osmmcp)
- **Airbnb MCP (openbnb-org/mcp-server-airbnb):** respects robots.txt by default. There is an "Ignore robots.txt" toggle in Claude Desktop, or the `--ignore-robots-txt` flag. — [GitHub openbnb](https://github.com/openbnb-org/mcp-server-airbnb)
- **Tripadvisor MCP:** the community server `pab1it0/tripadvisor-mcp` wraps the Content API (needs a key, so a credit card). — [enterprisedna directory](https://enterprisedna.co/directories/mcp/pab1it0-tripadvisor-mcp). The official Tripadvisor connector in Claude's directory is covered under KQ0.
- **Foursquare MCP:** an MCP server for the Places API exists, but its official status is unclear (listed as "Community"). It runs locally and needs a Service Key (Bearer). — [agentpedia](https://agentpedia.codes/mcp/foursquare); [CData guide](https://www.cdata.com/kb/tech/foursquare-mcp-claude-desktop.rst)
- **Tavily:** 1,000 API credits/month, no credit card. Basic search costs 1 credit, advanced costs 2. Hosted MCP at mcp.tavily.com. — [parallel.ai roundup (Oct 2026)](https://parallel.ai/articles/best-free-web-search-mcp); [xpay Tavily](https://www.xpay.sh/saas-pricing/tavily)
- **Exa:** "The Free Tier gives you $10 in credits (up to 2,500 Lite searches)", and "your free balance resets to $10 on the first of every month". No payment method is needed. Hosted MCP at `https://mcp.exa.ai/mcp`. — [Exa pricing](https://exa.ai/pricing). (Older sources describe a different free tier that was eliminated in Feb 2026. The official page above is current.)
- **Brave Search API:** $5 free credits every month on the Search and Answers plans. A card is required "to prevent abuse". Search costs $5/1k. There is an "LLM Context" endpoint for agents. — [Brave Search API](https://brave.com/search/api/)
- **Jina:** Reader `r.jina.ai` is keyless at 20 RPM (200 RPM with a key), per Jina's 2024 table. Search `s.jina.ai` now appears to require a key. New keys get 10M tokens one-time, non-commercial. MCP at mcp.jina.ai. — [Jina news (2024)](https://jina.ai/news/jina-reader-for-search-grounding-to-improve-factuality-of-llms); [agentdeals Jina](https://agentdeals.dev/vendor/jina-ai); [Spring AI MCP catalog](https://spring-ai-community.github.io/spring-ai-playground/features/default-mcp-catalog/search/)
- **Reddit MCP:** see KQ1 (`reddit-no-auth-mcp-server`, fragile).

### Inferences
- **Recommended Claude Code MCP set (all free):** (1) an OSM/Overpass MCP (keyless); (2) Exa or Tavily for semantic search beyond Claude's built-in search (better for "blog posts by locals about X"); (3) `reddit-no-auth-mcp-server` for Reddit threads; (4) optionally Grounding Lite. The Grounding Lite free tier covers personal use, but it needs a billing account and its terms bar caching.
- **For the mobile app:** use official directory connectors (Tripadvisor, AllTrails, Viator) rather than self-hosted MCPs. Custom remote connectors generally use OAuth or no auth. Key-in-header servers like Grounding Lite (API-key mode) may not plug in directly. This is an inference, not verified.
- Jina Reader (`https://r.jina.ai/<url>`) can render JS-heavy pages (Foody, Google Maps) into text from Claude Code. Its success on those specific sites was not tested.

### Gaps
- Maintenance status (last commit dates) of the community MCP servers was not checked on GitHub directly.
- No dedicated weather MCP was evaluated. Open-Meteo directly, or the Grounding Lite weather tool, covers this.
- Whether Claude.ai custom connectors accept API-key headers was not verified.

## Key question 6: "Agent-oriented" data services (llms.txt, agentic APIs from Tripadvisor/Booking/Expedia, Google Places AI, others): anything free?

### Takeaway
The agent-native, free-for-the-user options in 2026 are (a) **Claude's own directory connectors** (Tripadvisor, Booking.com, Expedia, AllTrails, Viator), (b) **Google Maps Grounding Lite** (a free tier, but billing is required), and (c) agent-oriented search APIs (Brave LLM Context, Exa, Tavily). I found no evidence that major travel sites publish llms.txt. Expedia's B2B MCP was announced but is not clearly shipped.

### Cited Findings
- No evidence of Tripadvisor, Expedia or Booking.com adopting llms.txt. The only mention was a hotel-marketing guide calling llms.txt "an emerging convention", static and unsuitable for live availability. — [trustedagents (hotel marketing)](https://trustedagents.kit.com/posts/the-starting-line-how-hotels-get-found-by-ai)
- Expedia plans a B2B MCP server to let partner agents reach inventory, "expected in months" (May 2026). — [Skift, 21 May 2026](https://skift.com/2026/05/21/expedia-to-launch-agentic-ai-tools-for-b2b-partners/)
- Expedia has a consumer MCP/Claude connector help page: "No Expedia account is needed". — [Expedia MCP help](https://www.expedia.com/playground/mcp/doc/)
- Business-travel booking agents are ahead of consumer OTAs, and "most travel MCP servers only search" (Oct 2026). — [engine.com](https://engine.com/blog/best-mcp-servers-business-travel)
- Google Grounding Lite is explicitly built for LLM grounding (place summaries, review insights in Pro, an agentic data visualization token in Preview). — [Google: Grounding Lite](https://developers.google.com/maps/ai/grounding-lite)
- Brave's "LLM Context" endpoint returns ranked extracted page content for agents, with a token budget of about 1k–33k. — [Brave Search API](https://brave.com/search/api/)

### Inferences
- For this user (free only), the "agentic" layer means using Claude's built-in connectors in the app, plus keyless OSM/Wikipedia/Open-Meteo in Claude Code. Paid agent-commerce APIs (Expedia B2B, Booking affiliate) are irrelevant.

### Gaps
- Not researched: ChatGPT Apps travel partners, Perplexity's place features, Booking's own MCP endpoint details, Viator connector capabilities.

## Key question 7: Verifying that a place is open, current and real, for free

### Takeaway
No single free source reliably answers "is it open today?" Combine (1) a platform that shows live status (Wongnai shows open/closed; Grounding Lite or Claude's map tool for Google data), (2) **recency of social or community posts** (Telegram post timestamps, dated Reddit threads, Wikivoyage "updated" markers, review counts on 2GIS/Tabelog), and (3) open data flags (Overture `operating_status`/`confidence`; OSM `opening_hours`, which is sparse in Asia). Google Maps place pages cannot be read by the fetcher.

### Cited Findings
- A Google Maps search URL fetched as an empty "Google Maps" shell: no name, rating, hours or status. — [Test fetch Google Maps](https://www.google.com/maps/search/?api=1&query=Himalayan+Java+Coffee+Thamel)
- Wongnai shows open/closed status per listing in fetched HTML. — [Test fetch Wongnai](https://www.wongnai.com/restaurants?regions=9681)
- 2GIS shows rating and review count per place, and marks ads ("Реклама"). — [Test fetch 2GIS](https://2gis.ru/moscow/search/кофейня)
- In OSM, Kathmandu cafés are sparsely tagged: 2/10 have `opening_hours` and 0/10 have `check_date`. — [Test fetch Overpass](https://overpass-api.de/api/interpreter?data=[out:json][timeout:25];node["amenity"="cafe"](around:500,27.7149,85.3123);out%2010;)
- Overture's `operating_status` values include `permanently_closed`/`temporarily_closed`. The default changed to null in May 2026, so a missing value no longer implies open. — [Earth Engine catalog](https://developers.google.com/earth-engine/datasets/catalog/overture-maps_places_place); [Overture release notes 2026-05-20](https://docs.overturemaps.org/blog/2026/05/20/release-notes/)
- Grounding Lite returns Google place data with `placeUrl`, but Google warns the "response that the LLM ultimately generates may not include the exact information returned". — [Google: Grounding Lite](https://developers.google.com/maps/ai/grounding-lite)
- Naver's receipt-verified visitor reviews are more trustworthy than blog reviews, which are often paid. — [seoulstart](https://seoulstart.com/guides/finding-good-restaurants-korea-guide)
- Xiaohongshu/social recommendations "can be promotion-driven", and locals cross-check across apps. — [chinaguidelines](https://chinaguidelines.com/en/posts/finding-good-restaurant)
- Claude's fetch results may be cached, so the content may not reflect the latest version. — [Anthropic web fetch docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)

### Inferences
- **Verification checklist the guide should apply (my synthesis):**
  1. Is there a mention dated within the last 6–12 months (a Telegram post, Reddit thread, blog with a date, or Wikivoyage "updated")?
  2. Does a live-status platform show it (Wongnai, 2GIS, Tabelog, or Google via Claude's map or Grounding Lite)?
  3. Search `"<place name>" closed OR "permanently closed" OR закрылся OR tutup` (Indonesian) and look for closure news.
  4. Check whether it is a SEO listicle with no dates. If so, downgrade it.
  5. Hand the user a Google Maps `search/?api=1&query=<name>+<area>` link so they confirm hours in one tap.
- For festival periods (e.g., Tihar, Nepal Sambat in early November 2026, visible on allevents), warn that hours may differ.

### Gaps
- Not tested: whether Google search result snippets (via Claude web search) reliably expose "Permanently closed" labels.
- Freshness of OSM data in Bali or Indian cities was not measured.

## Key question 8: Route output at no cost (Google Maps URLs, My Maps/KML, geo:, Apple Maps, Organic Maps, Leaflet + OSM tiles)

### Takeaway
**Google Maps `dir/?api=1` URLs** officially allow **up to 9 waypoints, but only 3 on mobile browsers**, are capped at 2,048 characters, use pipe separators (`%7C`), and take `travelmode=walking`. **Apple's unified Maps URLs** (iOS 18.4+) officially support **multiple repeated `waypoint=` parameters** with `mode=walking`. Organic Maps supports multi-point maps and pedestrian routes via `om://` links. For longer walks, generate KML/GPX/CSV for Google My Maps or Organic Maps, or render a Leaflet map. OSM tiles may be blocked in claude.ai artifacts and require attribution.

### Cited Findings
- **Google Maps URLs:** directions use `https://www.google.com/maps/dir/?api=1&origin=…&destination=…&travelmode=walking&waypoints=A%7CB%7CC`, with optional `origin_place_id`, `destination_place_id` and `waypoint_place_ids`, and `dir_action=navigate`. "Up to three waypoints supported on mobile browsers, and a maximum of nine waypoints supported otherwise." Waypoints are "not supported on all Google Maps products", in which case they are ignored. The URL limit is 2,048 characters. Search uses `https://www.google.com/maps/search/?api=1&query=…&query_place_id=…`. — [Google Maps URLs docs](https://developers.google.com/maps/documentation/urls/get-started)
- The Google Maps app caps a route at 10 stops (origin + destination + 8) on iPhone and Android. Unofficial guides describe path-style `…/maps/dir/A/B/C/` URLs and URL-merging tricks, without official confirmation. — [myrouteonline](https://www.myrouteonline.com/google-maps/how-many-stops-can-you-add-in-google-maps); [windowsdigitals](https://www.windowsdigitals.com/google-maps-add-more-than-10-stops/)
- **Google My Maps import:** supports CSV, TSV, KML, KMZ, GPX, XLSX and Google Sheets. KML/KMZ files can be up to 5 MB unzipped, other files up to 40 MB. CSV/Sheets accept WKT geometry. HTML/JS balloons in KML may not import. — [My Maps help](https://support.google.com/mymaps/answer/3024836). My Maps reportedly allows up to 10 layers per map (third-party). — [myrouteonline](https://www.myrouteonline.com/google-maps)
- **Apple unified Maps URLs** (iOS 18.4+, macOS 15.4+): `https://maps.apple.com/directions?source=…&destination=…&waypoint=…&waypoint=…&mode=walking`. Modes are driving, walking, transit and cycling. "You can specify multiple waypoints by repeating the `waypoint` parameter". Walking `avoid` values include stairs, hills and busy-roads. There are also `/search?query=…&center=lat,lon`, `/place?coordinate=…&name=…` and `/guides`. Short links on the `maps.apple` host redirect (301) to full URLs. — [Apple: Adopting unified Maps URLs](https://developer.apple.com/documentation/mapkit/unified-map-urls.md)
- **Organic Maps links:**
  - Multi-point map: `om://map?v=1&ll=lat,lon&n=Name&ll=…&n=…`
  - Route: `om://route?v=1&sll=…&saddr=…&dll=…&daddr=…&type=pedestrian` (types are vehicle, pedestrian, bicycle and transit)
  - Multi-stop v2: `om://v2/dir?origin=…&destination=…&waypoints=…|…&mode=…`
  - Search: `om://search?cll=…&query=…`
  - Point: `geo:lat,lon(Title)`
  
  Official test page: omaps.app/api. — [protocol-launcher Organic Maps reference](https://zhensherlock.github.io/protocol-launcher/apps/organic-maps.md); [organicmaps/api-ios PR #4 (May 2026)](https://github.com/organicmaps/api-ios/pull/4)
- **OSM standard tile policy:** "Show OpenStreetMap licence attribution clearly on the map". "Normal interactive viewing by a human" is permitted. Browsers must send a valid Referer, and generic User-Agents get blocked. No `no-cache` headers. Bulk prefetching and offline use are prohibited. Heavy use may be blocked without notice. — [OSMF tile usage policy](https://operations.osmfoundation.org/policies/tiles/)
- **Claude artifacts and map tiles:** an r/ClaudeAI user (about Dec 2025) reported that "The points will draw but the base map will be blank because it is blocked by Claude's CSP". A commenter claimed `tile.openstreetmap.org` and `basemaps.cartocdn.com` are "less aggressively blocked (YMMV)". This is anecdotal and unverified. — [r/ClaudeAI mirror snapshot](https://reddit.sentinel-team.org/posts/1thar6a/snapshots/2026-05-23T02%3A20%3A04.239191Z)
- **Google Maps Embed API** (an iframe map with directions mode) has an unlimited free cap but needs an API key. — [Google Maps Platform pricing](https://developers.google.com/maps/billing-and-pricing/pricing)
- The Claude iOS app's own map can open places in Apple Maps for turn-by-turn directions. — [Claude Help Center](https://support.claude.com/en/articles/11869619-using-claude-with-ios-apps)

### Inferences
- **Output recipe (my synthesis):**
  - **(a)** For walks of ≤3 intermediate stops, which work everywhere including mobile browsers, give one Google Maps `dir/?api=1&travelmode=walking` link.
  - **(b)** For 4–9 stops, the Google URL works in the app or desktop. Because of the mobile-browser cap, also split the route into segments of ≤3 waypoints each, or give the Apple Maps `directions?…&waypoint=…&mode=walking` link for iPhone (iOS 18.4+).
  - **(c)** For day or multi-day plans, generate a KML/GPX/CSV file in Claude Code (or as a downloadable file in the app). Import it into Google My Maps (layer per day) or Organic Maps, which handles offline maps and pedestrian routing.
  - **(d)** For an at-a-glance overview, use a Leaflet artifact with numbered markers and per-stop "Open in Google Maps/Apple Maps" links. Have a fallback if tiles are blocked (markers on a plain SVG, or a static list), and always show "© OpenStreetMap contributors".
- Prefer coordinates or place IDs over names in route URLs. Names in Kathmandu, Bali and India are ambiguous, and coordinates come straight from Overpass or Grounding Lite.
- Keep URLs under 2,048 characters for Google. If the user will paste a URL back into the Claude app for fetching, it must be under 250 characters.

### Gaps
- Not verified: whether Google Maps native apps (Android/iOS) honour all 9 `waypoints` from an `api=1` URL. The doc states only the mobile-browser limit of 3.
- Not tested: whether `https://omaps.app/...` web links (vs the `om://` scheme) carry multi-stop routes.
- Not verified from an official source: the claude.ai artifact CSP for image/tile hosts. Must be tested in practice.
- The My Maps per-layer feature limit (often cited as 2,000) is not confirmed by Google's help page.
