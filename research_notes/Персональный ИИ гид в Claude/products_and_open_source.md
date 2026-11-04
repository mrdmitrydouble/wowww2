# AI travel-guide and trip-planning products and open-source projects (Nov 2026): patterns to borrow for a personal Claude-based guide

Scope note: research done 2026-11-04. GitHub star counts were pulled live from the GitHub search API on 2026-11-04. Many "best AI trip planner 2026" pages are written by competing vendors or affiliates, so they are marked as such. Reddit threads did not show up in search results; community sentiment comes from Trustpilot, App Store listings, Product Hunt and independent blog tests.

## Q1. Consumer AI travel products: what each does, how it learns taste, here-and-now support, presentation, memory, praise and complaints, status

### Takeaway
By late 2026 the market has split in two. Big platforms (Google Maps/Gemini, Booking's Lola, Expedia+Layla, Airbnb, ChatGPT/Claude app connectors) own the live data and the booking rails. Standalone planners (Mindtrip, Stardrift, Stippl, Wanderlog, Wanderboat, Airial) compete on presentation and inspiration. The features that get praised are grounded, map-based and neighborhood-grouped answers, with in-destination help coming up fast. The features that flopped were end-to-end chatbots not grounded in live data (Expedia's Romie, now retired) and AI that "forgets" or invents places.

### Cited Findings

**Google (Ask Maps, Gemini in Maps, Gemini trip planning, AI Mode)** — the strongest "here and now" offering, but limited by region
- Ask Maps launched 12 Mar 2026 as a Gemini chat inside Google Maps (US and India, Android and iOS). It draws on 300M+ places plus community reviews, answers with a custom map, and tailors answers to prior searches and saved info. — [MacRumors](https://www.macrumors.com/2026/03/12/google-maps-gemini-integration/)
- By 31 Mar 2026 it was widely available to all Maps users in the US and India, placed directly under the search bar. Google's sample prompts are long, vibe-rich and situational, for example: "I'm taking myself on a solo date… quiet, dark bar within a mile, good for reading"; a sunset-timed scenic walking route; a skyline photo spot "where the sun won't blind" you. — [9to5Google](https://9to5google.com/2026/03/31/google-shows-how-you-should-use-ask-maps-as-the-feature-rolls-out-widely/)
- India update (6 Aug 2026): Ask Maps in Hindi, an optional Gmail connection (off by default, Calendar "soon") that tailors suggestions to upcoming flights and dinner reservations, and a live transit widget. Example: "ideas for spending a few hours near your hotel before tomorrow's flight". — [Google India blog](https://blog.google/intl/en-in/products/ask-maps-gets-more-helpful-in-india/)
- Gemini in Maps navigation extended to walking and cycling worldwide (29 Jan 2026). It is hands-free via "Hey Google", gives landmark-based directions (it cross-references ~250M places with Street View to find visible landmarks), and answers questions like "what neighborhood am I in?" — [TechCrunch](https://techcrunch.com/2026/01/29/google-maps-now-lets-you-access-gemini-while-walking-and-cycling/); [9to5Google](https://9to5google.com/2026/01/29/gemini-google-maps-walking-cycling/)
- Gemini trip planning (Google post, 6 Aug 2026):
  - It uses live Maps, Flights and Hotels data, plus YouTube creators for visual ideas, and a Viator app for tours.
  - With Personal Intelligence on, it can read Gmail, Photos, Search, YouTube and past chats. One example is suggesting restaurants based on saved food photos.
  - It groups activities by neighborhood and checks times against existing bookings.
  - The "Gemini Spark" 24/7 agent builds a Google Doc itinerary from incoming trip emails.
  - No metrics were published. — [Google blog](https://blog.google/products-and-platforms/products/gemini/how-gemini-plans-trips/)
- AI Mode in Search (17 Nov 2025): "Canvas" itinerary side panel (flights + hotels + Maps + web) and agentic restaurant, ticket and appointment booking in the US. Flight and hotel booking was announced as "future" with Booking.com, Expedia, Marriott, IHG and others. — [Google blog](https://blog.google/products/search/agentic-plans-booking-travel-canvas-ai-mode/); Canvas later reported rolling out to 200+ countries — [ChannelNews](https://www.channelnews.com.au/google-ai-mode-gains-global-flight-search-and-trip-planning-canvas-tool/)
- Personal Intelligence in Maps was seen only as beta code strings (reported test, not a launch). — [Android Authority](https://www.androidauthority.com/google-maps-personal-intelligence-3689447/)
- Accuracy: a travel blog reported catching two wrong Ask Maps answers in five days of testing (Tokyo, Barcelona, NYC) and advised verifying hours and prices (weak source). — [travel-tools-guide](https://travel-tools-guide.pages.dev/blog/google-maps-ask-maps-gemini-ai-travelers-2026)

**Mindtrip** — visual, map-first, free
- Launched Mindtrip Flights on 6 May 2026: in-chat paid flight booking via Sabre inventory and PayPal checkout. It is free. Hotel booking was not live as of 25 Aug 2026. The interface is visual and browsable (photos, maps, reviews), and community itineraries can be adapted. Reviewers call it weaker on overland multi-city logistics. — [Travel Anywhere test, Aug 2026 (competing vendor)](https://www.travelanywhere.blog/blog/best-agentic-ai-travel-apps-2026-mindtrip-layla-stippl-stardrift-wanderlog-tested)
- Taste onboarding is a Travel Quiz that creates a "travel persona", plus editable profile preferences. — [Product Hunt](https://www.producthunt.com/products/mindtrip). Mindtrip's own docs on how it learns were not found (see Gaps).
- "Start anywhere" (2024): build an itinerary from a screenshot, YouTube or TikTok link. — [TechCrunch](https://techcrunch.com/2024/07/31/travel-startup-mindtrips-new-feature-lets-you-build-an-itinerary-from-a-screenshot-youtube-or-tiktok-video)
- Other features: Group Chat for collaborative group planning, raised alongside a $12M round — [PhocusWire](https://www.phocuswire.com/mindtrip-secures-12m-funding-launches-group-chat); Events feature for local happenings "wherever they are" (Dec 2025) — [finanzen.net/BusinessWire](https://www.finanzen.net/nachricht/aktien/mindtrip-expands-beyond-travel-into-everyday-experiences-with-new-events-feature-helping-users-discover-local-happenings-wherever-they-are-15207933); "Mindtrip Stays" with conversational hotel discovery and price-drop alerts (Jul 2026, third-party directory, weak) — [tooldirectory.ai](https://tooldirectory.ai/tools/mindtrip)
- CEO Andy Moss: if an AI recommends a restaurant that closed two years ago, users lose trust immediately. Mindtrip itineraries carry a disclaimer that they may be inaccurate. — [USA TODAY via AOL](https://www.aol.com/news/ai-plan-next-vacation-know-091326308.html)

**Layla** — acquired by Expedia
- Expedia Group acquired Layla (Berlin, founded 2023) in July 2026. Terms were undisclosed and Layla keeps operating. — [Expedia IR](https://ir.expediagroup.com/news-and-events/news/news-details/2026/Expedia-Group-acquires-Layla-accelerating-its-AI-powered-trip-planning-and-booking-strategy/default.aspx); [PhocusWire](https://www.phocuswire.com/expedia-group-acquires-ai-travel-planning-app-layla)
- It has a free planning tier and Premium at ~$49.99/yr (PriceLock, unlimited interactions, member rates). It shows live partner pricing and day-by-day plans, and purchases usually complete on the partner site. Rated "strongest all-rounder" in one test. — [Travel Anywhere (competing vendor)](https://www.travelanywhere.blog/blog/best-agentic-ai-travel-apps-2026-mindtrip-layla-stippl-stardrift-wanderlog-tested)
- Trustpilot: 4.2/5 from 96 reviews (72% 5-star, 14% 1-star). — [Trustpilot](https://ca.trustpilot.com/review/layla.ai)
  - Praise: speed, and human agents who finalize bookings ("replaced my travel agent", Oct 2026).
  - Complaints: "The AI frequently forgets earlier instructions" (Sep 2026); routing to distant airports and hotels in the wrong city (May 2026); two-week waits for vouchers.
- Hallucination anecdote: one blog author says Layla recommended a Kyoto ramen shop that had closed in 2024. — [Travel Anywhere blog (vendor; attribution from search summary)](https://www.travelanywhere.blog/blog/worst-ai-travel-planning-mistakes-prompts)

**Stardrift, Stippl, Wanderlog** (all from one Aug 2026 test by a competing vendor) — [Travel Anywhere](https://www.travelanywhere.blog/blog/best-agentic-ai-travel-apps-2026-mindtrip-layla-stippl-stardrift-wanderlog-tested)
- Stardrift:
  - Free.
  - Retains "standing preferences" across trips, e.g. avoiding red-eyes.
  - Neighborhood-grouped activities with daily timing, plus an interactive shareable map and calendar sync.
  - Rated the best whole-trip itinerary, but it does not book.
- Stippl: an organization layer (budget, packing, expense split, journal). Its recommendations are less specific.
- Wanderlog:
  - Best map UI, with drag-to-reorder routing.
  - Imports booking confirmations via Gmail forwarding.
  - Free AI is capped at 5 messages per trip; Pro is $39.99/yr.
  - Rated as "AI feels bolted on".

**Wanderboat ("Wanderboat: Local Guide")** — small, positive, thin evidence
- It is a POI search engine and planner that ranks places using videos, images and insights. It has an "AI Concierge" for real-time questions and a "Hands Off" mode for full trip blueprints. Ratings: Product Hunt 5.0 (4 reviews); App Store 4.77 (22 ratings). — [Product Hunt](https://www.producthunt.com/products/wanderboat-ai/reviews); [AppGoblin](https://appgoblin.info/apps/6736818361)
- It was built by UTA AI, a Sequoia-backed Silicon Valley team, and described as "Xiaohongshu + Mafengwo for the LLM era". — [36Kr](https://www.36kr.com/p/2858620673837956)

**Airial** — social video turned into itinerary
- $3M seed (Jun 2025, Montage Ventures). Founded by ex-Meta and Waymo engineers. It turns social media content into bookable itineraries and plans a creator program. Desktop public beta; mobile apps were promised for 2025 but are unconfirmed. — [TechCrunch](https://techcrunch.com/2025/06/30/former-meta-engineers-airial-travel-tool-helps-travelers-solve-logistics-planning-with-ai); [Travolution](https://www.travolution.com/news/airial-travels-public-beta-takes-off/)
- Paste a TikTok, Reels or blog link and the creator's places are added to the itinerary. A hands-on review saw a "mix of well-known… and lesser-known hidden gems". — [Net Influencer](https://www.netinfluencer.com/ai-startup-airial-travel-raises-3m-for-ai-powered-holiday-plans/); [Only In Your State](https://www.onlyinyourstate.com/trip-ideas/usa/airial-travel-ai-review)

**Booking Holdings: Lola** — new Sep 2026
- A standalone assistant from the Kayak co-founders (Hafner, English), launched 29 Sep 2026, US only. — [Skift](https://skift.com/2026/09/29/kayak-co-founders-launch-lola-booking-holdings-new-ai-assistant-exclusive/); [PhocusWire](https://www.phocuswire.com/news/technology/steve-hafner-paul-english-launch-ai-assistant-lola)
  - Framing: "At Lola, we're trying to solve for what should I do this weekend." It covers open idea to booked trip in one chat.
  - Tiers: free / $5 Plus / $25 VIP. A human concierge (Ten Group) is metered by tier.
  - It takes no ads or paid placement. Hafner expects ~90% of users to stay free.

**Expedia: Romie** — retired (flop)
- Romie (launched 2024) has been retired. Expedia's CPO said early chatbots answered without being tied to live inventory and rates, so "customers left within a few exchanges" and lost trust was slow to recover. The fix ("roughly a year") rebuilt evaluation and data plumbing, while the model barely changed. — [Hospitality.today, 16 Jun 2026](https://www.hospitality.today/article/expedia-learned-where-ai-breaks-it-wasnt-the-model)
- CEO Ariane Gorin: AI "point agents" work better than an end-to-end chatbot. — [Travel Weekly AU](https://travelweekly.com.au/expedia-ceo-warns-that-end-to-end-ai-chatbots-dont-work/)
- Expedia also partnered with Perplexity's Comet browser for travel (Oct 2025). — [PhocusWire](https://www.phocuswire.com/expedia-group-perplexity-comet-partnership-ai)

**ChatGPT (apps, agent, memory)**
- Apps SDK launch on 6 Oct 2025 (DevDay) with Booking.com and Expedia. They pull live prices, images and availability, but booking is finalized on the partner site. — [AltexSoft](https://www.altexsoft.com/travel-industry-news/chatgpt-turns-into-a-travel-hub-with-expedia-and-booking-com); [Travel Weekly](https://www.travelweekly.com/Travel-News/Travel-Technology/OTAs-build-travel-planning-apps-in-ChatGPT)
- The Tripadvisor ChatGPT app is US-only, covers hotels only (no restaurants or activities), and shows only a few review highlights. — [Jotform](https://www.jotform.com/ai/best-chatgpt-travel-apps/)
- Agent mode browses, fills forms and prepares payment, but needs explicit approval at each important step. It works well for "simple and direct itineraries". — [Ulysse](https://ulysse.com/news/en/travel/how-chatgpt-can-now-book-your-next-trip-for-you-984)
- "Traveler.md" is a third-party ChatGPT app ("Remember how you travel") that gives assistants a persistent travel-preference memory. It is the closest commercial analog to a personal profile file. — [ChatGPT app listing](https://chatgpt.com/plugins/plugin_asdk_app_6a7cb6d3e938819198aa071ec7cd9647) (page returned 403 to fetch; description from search snippet)

**Perplexity**
- Hotel booking with Selfbook and Tripadvisor (Mar 2025): ~140k bookable properties, with answers based on Tripadvisor reviews. One reviewer called it "more like curated aggregation than a seamless booking engine". No 2026 updates found. — [PhocusWire](https://www.phocuswire.com/perplexity-selfbook-agentic-ai-travel-booking-tripadvisor); [Triptease](https://www.triptease.com/resources/perplexity-ai-hotel-search-agent)

**Microsoft Copilot**
- Copilot Actions (2025) launched with Booking.com, Expedia, Kayak, OpenTable, Priceline, Tripadvisor, Skyscanner, Viator and Vrbo. No 2026 travel changes were found. — [Windows Central](https://www.windowscentral.com/microsoft/copilot-actions-announcement-2025)

**Apple (iOS 27 Maps, WWDC 2026)** — secondary sources only
- Reported features: save and organize places to visit, "Visited Places" history, US-only "Local Lists" of curated nearby picks, expanded "Suggested Places", and natural-language route search. Apple says recommendations are generated privately and not linked to individual users. A Gemini-based model for Siri is reported but its Maps link is unverified. — [Cult of Mac](https://www.cultofmac.com/news/every-notable-apple-maps-upgrade-in-ios-27); [NewsBytes](https://www.newsbytesapp.com/news/science/apple-unveils-ios-27-maps-with-ai-flyover-local-lists/tldr)

**Airbnb**
- Summer 2026 release (May): AI review highlights, a comparison engine and a multilingual support bot. Fall update (30 Sep 2026): AI listing descriptions in search and AI side-by-side comparison of wishlisted homes, US-first. Airbnb has not published quality or conversion metrics. — [Airbnb newsroom](https://news.airbnb.com/en-au/airbnb-2026-september-update); [Rental Scale-Up](https://www.rentalscaleup.com/airbnb-ai-strategy-2026/)

**Tripadvisor / Viator**
- Repositioned as "experiences-led and AI enabled". Viator has an AI pre-booking chat, and Tripadvisor and TheFork apps are in ChatGPT (investor summaries, weak). — [Quartr Q1 2026](https://quartr.com/events/tripadvisor-inc-trip-q1-2026_3Y1Ztm3v); [Motley Fool Q4 2025 transcript](https://www.fool.com/earnings/call-transcripts/2026/02/12/tripadvisor-trip-q4-2025-earnings-transcript)

**Claude (relevant platform facts)**
- On 23 Apr 2026 Anthropic added consumer connectors, including Tripadvisor, Booking.com, Viator, AllTrails ("surface trails nearby"), Uber, Uber Eats, Resy and StubHub.
  - They are "available on all plans, with mobile in beta".
  - Claude suggests the right connector; when several apps fit, "Claude shows them all and lets you choose".
  - Results can be refined in chat (e.g., "shorter, more scenic, dog-friendly").
  - Claude checks before booking.
  - Source: [Claude blog](https://claude.com/blog/connectors-for-everyday-life)
- The Claude iOS app can use Location Services "to provide contextual suggestions for nearby places and services". It can show suggested places on a map and open them in Apple Maps, and can create Calendar events and Reminders. This is available on all plans; location is not available to Team/Enterprise. — [Claude Help Center](https://support.claude.com/en/articles/11869619-using-claude-with-ios-apps)
- An independent tester found the Claude mobile app renders a map with markers and hands routing to the native maps app, but rated its spatial reasoning as limited. — [peschinskiy.github.io](https://peschinskiy.github.io/using-maps-in-ai-assistants)

**Yandex (Alice AI), 2GIS, Russian market**
- A test of Alice AI for a hotel search (family, big dog, New Year near Moscow), 30 Oct 2025: — [Tourdom](https://www.tourdom.ru/hotline/obzory-tekhnologiy/ozadachili-alisu-ai-zaprosom-na-podbor-otelya-chtoby-otdokhnut-s-detmi-sobakoy-i-vstretit-lyubov/)
  - Good: fast, uniformly structured hotel cards (dog rules, kids' programs, address, link).
  - Bad: robotic tone, no empathy, no follow-up questions, ignored the soft "find love" goal, and proposed a hotel that only allows dogs under 6 kg.
  - GPT was judged more useful, while Alice was better as a source of Russian-language data.
- Alice AI (YandexGPT 5) unified Yandex's AI services and processed 2.9B+ requests last year. No confirmed Alice→Yandex Maps trip-routing feature was found. — [vc.ru](https://vc.ru/provod/3018408-neyroset-alisa-vozmozhnosti). A headline reports you can now talk to Alice AI during map navigation (body not retrievable). — [Inc. Russia](https://incrussia.ru/news/pri-navigatsii-po-kartam-teper-mozhno-pogovorit-s-ii-pomoshhnikom-alisoj/)
- 2GIS:
  - Launched an AI assistant inside company and location cards (summer 2026, part of iOS users). It can interact with venues' booking systems, with calls to businesses planned. — [kod.ru](https://kod.ru/2gis-ai-assistant); [finratings.kz](https://finratings.kz/news/11446-2gis-budet-sam-zapisyvat-vas-v-salony-krasoty-i-servisy/)
  - In Oct 2026 the assistant added transit answers (bus arrival, fare, fewest transfers) built on 2GIS route and schedule data plus live vehicle data. — [kod.ru](https://kod.ru/2gis-ii-pomoshchnik-transport); [www1.ru](https://www1.ru/news/2026/10/29/2gis-naucil-ii-podskazyvat-kogda-priedet-avtobus-i-kak-bystree-dobratsia.html)
- A Russian user report: an AI picked four hotels, two of which did not exist, plus invented attractions. — [Mail.ru](https://vfokuse.mail.ru/articles/68850333-puteshestviya-s-pomoshyu-ii-pochemu-ne-stoit-doveryat-iskusstvennomu-razumu/)
- A Russian "AI guide 2026" roundup lists only multi-model chat wrappers (GoGPT, ChadGPT, etc.) with voice, photo-recognition of monuments and rain re-routing. It lists no GPS-triggered Russian AI audio guide. — [DTF](https://dtf.ru/top_rating/5164371-ii-gid-dlya-puteshestviy)

**AI audio-guide apps**
- VoiceMap (human-made, GPS-triggered):
  - Praised because audio "triggered in the appropriate spots".
  - Complaints: missing basic tours for popular cities, and a tour that failed to start.
  - Source: [App Store](https://apps.apple.com/us/app/voicemap-audio-tours-guides/id852027939)
- SmartGuide offers GPS-triggered stories for 1,000+ destinations, offline maps, and an AI chat and itinerary planner (2026). It is free to download; its claims are self-reported. — [SmartGuide blog](https://blog.smart-guide.org/en/best-tour-guide-apps-for-travelers-in-2026)
- AI-generated narration apps:
  - Narrated Tours: theme-based walks exported as mp3, about 10 min of narration. — [Product Hunt](https://www.producthunt.com/products/narrated-tours-on-demand-audio-guides)
  - CityYoYo: on-demand narration for places you tap or pass in "Tour Mode" (vendor claim). — [CityYoYo](https://cityyoyo.com/blog/best-city-audio-tour-apps.html)
  - Guidude: AI voice tour guide. — [App Store](https://apps.apple.com/app/id6778813799)
  - No independent accuracy reviews of AI narration were found. — [OxGuide](https://oxguide.com/blog/best-ai-tour-guide-apps-2026)

### Inferences
- The "here and now" leader is Google (Ask Maps + Gemini walking navigation + Lens), but Ask Maps is US/India-only. The user is in Kathmandu and Bali for much of the year, and in Moscow, where Google Maps data is weak and Yandex/2GIS dominate. So Ask Maps is useful mainly on his India legs. Elsewhere a Claude setup that uses web search plus his own profile can compete on taste, though not on live POI data.
- The failures cluster around the same issue: answers not grounded in live data (Romie, closed-restaurant cases, invented hotels) and lost constraints in long chats (Layla "forgets earlier instructions"). Both can be reduced in Claude with a persistent profile file and a "verify before recommending" rule.
- Commercial products increasingly use human backup (Layla agents, Lola concierge). That is not replicable for free. The free analog is to have Claude produce a precise "call/message script" for a hotel or driver.

### Gaps
- iMean and several smaller apps (Roam Around, GuideGeek, Wonderplan) were not researched in depth. GuideGeek and Roam Around are only named in roundups.
- No 2026 primary source was found for Perplexity travel features, Gemini Gems for travel, or the Microsoft Copilot travel roadmap.
- Mindtrip's App Store page could not be fetched (404). No first-party documentation exists on how Mindtrip's quiz or memory works; "learns your taste" is marketing language.
- Yandex Maps + Alice AI capabilities could not be verified (article body truncated). Yandex Travel has no confirmed AI hotel assistant.
- Airial mobile app status and Airial's current state in 2026 are unknown.
- Reddit threads were not surfaced by the search tool, so community sentiment comes from Trustpilot, App Store and blogs.

## Q2. UX patterns: taste elicitation and "I don't know what I want", presenting 2–3 options with trade-offs, in-situ walking guidance

### Takeaway
Shipped products mostly elicit taste with one short upfront step (quiz, swipes, vibe chips) and then rely on stated "standing preferences". The most robust mechanism found is comparative judgment (Beli-style "better or worse than X"), which is easy to imitate in voice. For options, the strongest public design is "three positioned options with trade-offs, never a top-10 list" plus "one anchor + one backup per day". For in-situ guidance, the patterns are landmark-based directions, hands-free voice questions ("what neighborhood am I in"), and location-triggered narration.

### Cited Findings
**Taste elicitation**
- Beli (restaurants):
  - The user first picks one of three reactions ("I liked it / It was fine / I didn't like it").
  - The app then asks pairwise "did you like this more than that?" questions to build a personal stacked ranking and a predicted score per place. Users can skip with "Too Tough".
  - Personalized suggestions reportedly need ≥15 ranked places, and the app matches users with similar-taste people worldwide.
  - Sources: [Wikipedia](https://en.wikipedia.org/wiki/Beli_(app)); [Pratt IxD critique](https://ixd.prattsi.org/2022/02/design-critique-beli-ios-app/); [Harvard Crimson](https://www.thecrimson.com/article/2026/2/26/beli-inquiry/) ("people are remarkably bad at determining objective values in a vacuum")
  - Criticism: forcing a linear ranking "is extremely limiting". — [Reddit r/FoodNYC (mirror)](https://cal1.lr.ggtyler.dev/r/FoodNYC/comments/1ix7jpv/does_anyone_actually_use_the_beli_app/mekcmyv/?context=3)
- Swipes and vibes:
  - TravelMind: swipe-based city discovery, launched on Product Hunt 9 Jun 2026. A commenter flagged the cold-start problem in cities with few swipes. — [Product Hunt](https://www.producthunt.com/posts/travelmind-2)
  - Voyant: a waitlisted concept claiming taste learned in about 90 seconds of swipes, refined by bookings and post-trip feedback (unverified marketing). — [Voyant](https://voyant-landing.pages.dev/)
  - Holiday Extras' "Vibe Traveller" matches by mood and aesthetic. — [Travolution](https://www.travolution.com/news/technology/holiday-extras-keeps-momentum-with-ai-match-making-vibe-tool/)
- Mindtrip uses a Travel Quiz for a persona plus editable preferences. — [Product Hunt](https://www.producthunt.com/products/mindtrip)
- Stardrift keeps "standing preferences" across trips (e.g., no red-eyes). — [Travel Anywhere](https://www.travelanywhere.blog/blog/best-agentic-ai-travel-apps-2026-mindtrip-layla-stippl-stardrift-wanderlog-tested)
- Gemini Personal Intelligence infers taste from saved food photos, Gmail bookings and past chats, so the user does not have to state it. — [Google blog](https://blog.google/products-and-platforms/products/gemini/how-gemini-plans-trips/)
- Inspiration-first visual UIs:
  - OpenUI Trip Planner (open source): "answers are interfaces, not text". Ideas are explored as visual spreads/moodboards, and saved places are then turned into a day-by-day board on a map. — [GitHub thesysdev/openui-trip-planner](https://github.com/thesysdev/openui-trip-planner)
  - Mindtrip's start-from-a-screenshot/TikTok approach — [TechCrunch](https://techcrunch.com/2024/07/31/travel-startup-mindtrips-new-feature-lets-you-build-an-itinerary-from-a-screenshot-youtube-or-tiktok-video)
- "Surprise me": the trvl MCP's headline example is "I have €300 and a free weekend. Surprise me", answered with a single destination plus flight, hotel and weather and a savings explanation. — [GitHub MikkoParkkola/trvl](https://github.com/MikkoParkkola/trvl)
- Lola's framing targets the under-specified "what should I do this weekend" intent rather than "which flight is best". — [Skift](https://skift.com/2026/09/29/kayak-co-founders-launch-lola-booking-holdings-new-ai-assistant-exclusive/)

**Presenting options and plans**
- apljacob/travel-agent (Claude Code skill):
  - "one consolidated question batch, branched by what you already said" (skip what is already known)
  - "three positioned options with tradeoffs spoken out loud, never a top-10 list"
  - "one named anchor + named backup per day"
  - "push back on bad ideas… with better alternatives"
  - "web search before every concrete claim"
  - pacing ("two great days beat four exhausting ones")
  - Source: [GitHub apljacob/travel-agent](https://github.com/apljacob/travel-agent)
- Group by neighborhood and check travel time: Gemini — [Google blog](https://blog.google/products-and-platforms/products/gemini/how-gemini-plans-trips/); Stardrift — [Travel Anywhere](https://www.travelanywhere.blog/blog/best-agentic-ai-travel-apps-2026-mindtrip-layla-stippl-stardrift-wanderlog-tested)
- Claude connectors show all candidate apps and let the user choose, then allow conversational refinement ("shorter, more scenic"). — [Claude blog](https://claude.com/blog/connectors-for-everyday-life)
- Alice AI's uniform hotel cards (same fields for each option) were praised as fast to scan, but the lack of follow-up questions was criticized. — [Tourdom](https://www.tourdom.ru/hotline/obzory-tekhnologiy/ozadachili-alisu-ai-zaprosom-na-podbor-otelya-chtoby-otdokhnut-s-detmi-sobakoy-i-vstretit-lyubov/)
- Mobile-first single-file outputs (open-source skills):
  - travel-plan-viz builds an offline HTML with a Leaflet map (no API key), numbered stops, a dashed route, one-tap deep links to Apple Maps or Android geo:, a daily timeline, and "book by date X" reminders computed backwards from departure. — [GitHub zexuanw958-svg/travel-plan-viz](https://github.com/zexuanw958-svg/travel-plan-viz)
  - jianhao-travel-planner produces half-hour time-slot cards, a rain plan per day, and budgets in three tiers. — [GitHub awangwang123/jianhao-travel-planner](https://github.com/awangwang123/jianhao-travel-planner)

**In-situ / walking guidance**
- Gemini walking navigation gives landmark-based turns ("after the Thai Siam Restaurant"), hands-free questions about the neighborhood and nearby places, and Lens for camera questions about landmarks. — [TechCrunch](https://techcrunch.com/2026/01/29/google-maps-now-lets-you-access-gemini-while-walking-and-cycling/); [9to5Google](https://9to5google.com/2026/01/29/gemini-google-maps-walking-cycling/)
- Ask Maps' situational prompts include a sunset-timed scenic walking route and "a few hours near your hotel before tomorrow's flight". — [9to5Google](https://9to5google.com/2026/03/31/google-shows-how-you-should-use-ask-maps-as-the-feature-rolls-out-widely/); [Google India](https://blog.google/intl/en-in/products/ask-maps-gets-more-helpful-in-india/)
- GPS-triggered narration is praised when it fires at the right spot and criticized when it doesn't start (VoiceMap). — [App Store](https://apps.apple.com/us/app/voicemap-audio-tours-guides/id852027939). AI narration on demand for passed places (CityYoYo, vendor) — [CityYoYo](https://cityyoyo.com/blog/best-city-audio-tour-apps.html); mp3 walks about 10 min (Narrated Tours) — [Product Hunt](https://www.producthunt.com/products/narrated-tours-on-demand-audio-guides)
- scenic-routing-mcp routes walks along parks, rivers and landmarks from OSM and exports GPX or an HTML map. It is self-hosted Docker (Valhalla, PostGIS, Ollama). — [GitHub orofarne/scenic-routing-mcp](https://github.com/orofarne/scenic-routing-mcp)

### Inferences
- Minimal-question onboarding works best as "infer, then confirm". Ask at most one consolidated question batch and skip what is known (apljacob). Infer the rest from history, as Gemini does with photos and Gmail; the Claude analog is the profile file plus past trips.
- Contrastive elicitation fits voice better than swipes. One prompt such as "A or B: noisy night market or quiet rooftop?" or "better or worse than [known liked place]?" is Beli's mechanism in one utterance, and the answer can be appended to the profile.
- For "I don't know what I want", products reframe the question around the situation (time left, energy, weather, where you are) instead of asking for preferences. Examples are Lola's "what should I do this weekend" and Ask Maps' situational prompts. A Claude prompt can take this default frame: "time available / energy / company / budget → 3 contrasting options".
- In Claude mobile there is no GPS-triggered audio, so "audio guide" has to be pull-based. The user says or types "I'm at X" or shares location, and Claude narrates a short story plus the next stop. An artifact with Leaflet and deep links (the travel-plan-viz pattern) can stand in for the map.

### Gaps
- No published A/B data was found on swipe vs quiz vs conversational onboarding for travel.
- No independent evaluations exist of AI audio-guide accuracy.
- Ask Maps' answer UI (cards vs lists vs follow-up chips) was not described in the text sources.

## Q3. How products avoid generic, touristy recommendations

### Takeaway
Products avoid generic picks by grounding in proprietary local data (Google's 300M places and reviews, 2GIS/Yandex directories), by ingesting creator and social video (Airial, Mindtrip, Gemini via YouTube, Wanderboat), by personal history (Gemini Personal Intelligence, Beli taste-neighbors), and by explicit "passion lens" rules (elite-planner skills). The data-heavy approaches are proprietary. The "lens + creator links + personal history + verification" approaches can be replicated in Claude.

### Cited Findings
- Ask Maps answers from 300M+ places plus community reviews, tailored to the user's saved places and past searches. — [MacRumors](https://www.macrumors.com/2026/03/12/google-maps-gemini-integration/)
- Gemini adds "visual ideas and recommendations from YouTube creators" and personal photos. — [Google blog](https://blog.google/products-and-platforms/products/gemini/how-gemini-plans-trips/)
- Airial and Mindtrip ingest TikTok, Reels, YouTube and blog links and extract the places mentioned. — [Net Influencer](https://www.netinfluencer.com/ai-startup-airial-travel-raises-3m-for-ai-powered-holiday-plans/); [TechCrunch](https://techcrunch.com/2024/07/31/travel-startup-mindtrips-new-feature-lets-you-build-an-itinerary-from-a-screenshot-youtube-or-tiktok-video)
- Wanderboat ranks POIs using videos, images and insights. — [Product Hunt](https://www.producthunt.com/products/wanderboat-ai/reviews). It is positioned as the "Xiaohongshu + Mafengwo" of LLMs (UGC-notes model). — [36Kr](https://www.36kr.com/p/2858620673837956)
- Beli uses taste-neighbors (users with similar rankings, not just nearby) and "friend ratings". — [Spoon University](https://spoonuniversity.com/lifestyle/beli-the-new-app-personalizing-restaurant-reviews-and-recommendations)
- apljacob/travel-agent states the problem directly: most AI planners output "a top-10 list of generic recommendations, with stale hours". Its remedy is "the traveler's passion is the lens for the entire trip", plus web search before every concrete claim. — [GitHub](https://github.com/apljacob/travel-agent)
- In a Japan test, ChatGPT suggested more local festivals and events than the dedicated apps, while Mindtrip alone gave step-by-step train transfers. — [Practical Globetrotters](https://practicalglobetrotters.substack.com/p/we-tested-4-ai-travel-services-to)
- jianhao-travel-planner keeps a per-city "food intel card" file that is appended on every trip and "grows thicker with use". Its SKILL.md changelog records real failures, e.g. "listed price ≠ paid price". — [GitHub awangwang123/jianhao-travel-planner](https://github.com/awangwang123/jianhao-travel-planner)
- Lola promises no ads or paid placement, unlike other Booking brands. That is a neutrality signal, since commission-driven planners (Airial plans commission and creator revenue) have incentives to bias picks. — [Skift](https://skift.com/2026/09/29/kayak-co-founders-launch-lola-booking-holdings-new-ai-assistant-exclusive/); [Net Influencer](https://www.netinfluencer.com/ai-startup-airial-travel-raises-3m-for-ai-powered-holiday-plans/)

### Inferences
- Replicable in Claude for free:
  - a "lens" rule: every pick must be justified against the user's profile, never by popularity alone
  - a mandatory mix in each set of options: one classic, one local or non-obvious, one wildcard
  - pasting creator links or screenshots for Claude to extract places from
  - a growing per-city notes file, the jianhao pattern, holding places he has liked and disliked in Kathmandu, Bali, Moscow and so on
  - web-search verification of hours and closures before presenting
- Not replicable: Google's place graph and reviews at scale, Beli-style collaborative filtering across users, and 2GIS/Yandex live directories. Partial substitutes are free: the Tripadvisor connector in Claude, an OSM MCP, and Google Grounding Lite (free cap). Local-language sources such as Xiaohongshu-style notes, Russian Telegram channels and Indonesian or Nepali blogs can be reached through web search.

### Gaps
- Curator networks such as Spotted by Locals and Atlas Obscura, and Xiaohongshu-for-travel in Asia, were not researched in this pass.
- No quantitative evidence was found that creator-video ingestion improves satisfaction.

## Q4. Reusable open-source assets (Claude skills, MCP servers, agent repos, prompts, profile schemas) and their quality

### Takeaway
The most reusable assets for a Claude-native setup are a handful of SKILL.md-based travel skills (apljacob/travel-agent for methodology, skywain/trip-planner-skill and travel-plan-viz for verified mobile outputs, jianhao for fact-checking and accumulating notes) and a few MCP servers (cablate/mcp-google-map, Google's official Maps Grounding Lite, OSM servers with no keys). The LangGraph and CrewAI "multi-agent travel planner" repos are mostly portfolio demos of low value. Leaked GPT-prompt repos are large but legally gray and have no confirmed high-quality travel-guide prompt. A formal traveler-profile schema exists (DIF HATPro), but it is aimed at hospitality, not taste.

### Cited Findings
Star counts are from GitHub search API on 2026-11-04.

**Claude / Agent Skills (travel)**
- **apljacob/travel-agent** — 12★, last push May 2026, license is "source-available, non-commercial".
  - A 7-phase workflow modeled on Wendy Perrin, Indagare and Black Tomato.
  - Reference files: discovery-questions with branching, itinerary template (anchor+backup), reservations tracker with computed deadlines, elite-planner principles, and a pushback table.
  - Includes acceptance-test queries.
  - High design quality, low adoption. Best for its *methodology*. — [GitHub](https://github.com/apljacob/travel-agent)
- **skywain/trip-planner-skill** — 48★, MIT, active Oct 2026.
  - "checks opening hours, prices and holidays with tools instead of guessing, hands you a link for every booking, and never books or pays."
  - Renders a `plan.geo.json` into 8 visual themes.
  - "Verified in Claude Code (others untested)."
  - Source: [GitHub](https://github.com/skywain/trip-planner-skill)
- **zexuanw958-svg/travel-plan-viz** — 410★, MIT, active Nov 2026. Offline, mobile-first single HTML: Leaflet with free tiles (no API key), deep links to native maps, daily timeline, booking-deadline reminders. Content is Chinese-oriented. — [GitHub](https://github.com/zexuanw958-svg/travel-plan-viz)
- **awangwang123/jianhao-travel-planner** — 420★, MIT, active Nov 2026. Chinese.
  - A fact-check workflow (multi-source cross-validation, final check against that day's forecast) and a mechanical `tools/checklist.py` the AI must pass before delivering.
  - An accumulating per-city food-intel file.
  - Trigger phrases include "今天去哪" ("where to go today").
  - Warns that some AI environments summarize the 93KB SKILL.md and lose rules.
  - Source: [GitHub](https://github.com/awangwang123/jianhao-travel-planner)
- **cablate/mcp-google-map** — 488★, MIT, active Oct 2026. Bundles 3 Agent Skills, including "evidence-backed travel planning". — [GitHub](https://github.com/cablate/mcp-google-map)
- **Lower-quality or low-signal skills:**
  - QuantumLynx/claude-skills travel-planner (0★) — [GitHub](https://github.com/QuantumLynx/claude-skills/blob/main/plugins/travel-planner/skills/travel-planner/SKILL.md)
  - cheng-chun-yuan/claude-travel-planner-skill (2★; uses the Kiwi.com MCP for flights) — [GitHub](https://github.com/cheng-chun-yuan/claude-travel-planner-skill)
  - majiayu000 claude-skill-registry trip-planner — [GitHub](https://github.com/majiayu000/claude-skill-registry/blob/main/skills/data/trip-planner/SKILL.md)
  - travisjneuman travel-planner (decision matrices, hourly templates; 501 installs reported) — [Claude Marketplaces](https://claudemarketplaces.com/skills/travisjneuman/.claude/travel-planner)
  - ErlebnisW/travel-planner (multi-sub-skill: food, logistics, local intel) appeared in search but was not returned by the GitHub API (possibly removed) — [GitHub](https://github.com/ErlebnisW/travel-planner)
- **Directories:**
  - anthropics/skills (187,151★) — [GitHub](https://github.com/anthropics/skills)
  - ComposioHQ/awesome-claude-skills (78,685★) — [GitHub](https://github.com/ComposioHQ/awesome-claude-skills)
  - travisvn/awesome-claude-skills (15,694★) — [GitHub](https://github.com/travisvn/awesome-claude-skills)
  - The awesome lists don't list a travel planner directly. — [search summary of ComposioHQ / travisvn lists](https://github.com/ComposioHQ/awesome-claude-skills)

**MCP servers**
- **Google Maps Grounding Lite** (official Google, remote MCP at `https://mapstools.googleapis.com/mcp`, Streamable HTTP).
  - Tools: place search with AI summaries, weather, and routes (distance and duration only, no turn-by-turn).
  - Free usage cap of 10,000 for the SKU; Google advises verifying LLM output.
  - Quotas differ between official page versions (search places 100/min and 1,000/day per project vs 300/min).
  - Sources: [Google Developers](https://developers.google.com/maps/ai/grounding-lite?hl=en-GB); [developers.google.cn](https://developers.google.cn/maps/ai/grounding-lite)
- **cablate/mcp-google-map** — 488★, MIT. 18 read-only tools: places, details/hours/reviews, directions, route matrix, multi-stop optimization up to 25 stops, weather, air quality, static maps. Runs over stdio or Streamable HTTP and needs a Google Maps API key. — [GitHub](https://github.com/cablate/mcp-google-map)
- **OpenStreetMap, no API key:**
  - jagan-shanmugam/open-streetmap-mcp (231★, last push Jul 2025) — [GitHub](https://github.com/jagan-shanmugam/open-streetmap-mcp)
  - wiseman/osm-mcp (89★, Mar 2025) — [GitHub](https://github.com/wiseman/osm-mcp)
  - NERVsystems/osmmcp (30★, active Oct 2026) — [GitHub](https://github.com/NERVsystems/osmmcp)
  - cyanheads/openstreetmap-mcp-server (9★, active Oct 2026; geocoding plus Overpass queries; STDIO or Streamable HTTP) — [GitHub](https://github.com/cyanheads/openstreetmap-mcp-server)
- **orofarne/scenic-routing-mcp** — 14★, MIT. Scenic pedestrian routing. Heavy self-hosting (Docker: Valhalla, PostGIS, Ollama, Redis). — [GitHub](https://github.com/orofarne/scenic-routing-mcp)
- **MikkoParkkola/trvl** — 93★, PolyForm Noncommercial. A Go binary with one `travel` router tool across 24 providers (flights, hotels, trains, ferries, weather, places); "No API keys". — [GitHub](https://github.com/MikkoParkkola/trvl)
- **openbnb-org/mcp-server-airbnb** — 556★, active Aug 2026: "Search Airbnb using your AI Agent". — [GitHub](https://github.com/openbnb-org/mcp-server-airbnb)
- **shaikhspeare/wanderlog-mcp** — 168★, active Nov 2026. Build and edit Wanderlog itineraries via chat (unofficial). — [GitHub](https://github.com/shaikhspeare/wanderlog-mcp)
- **pab1it0/tripadvisor-mcp** — 64★, Apr 2025. Tripadvisor Content API, needs a key. — [GitHub](https://github.com/pab1it0/tripadvisor-mcp)
- **foursquare/foursquare-places-mcp** — 18★, official org, Apr 2025. — [GitHub](https://github.com/foursquare/foursquare-places-mcp)
- **alexpriest/swarm-mcp** — 6★, active Oct 2026. MCP over your own Foursquare Swarm check-in history, which could be used to import a personal place history. — [GitHub](https://github.com/alexpriest/swarm-mcp)
- **Archived or defunct:**
  - GongRzhe/TRAVEL-PLANNER-MCP-Server (98★, archived Mar 2026) — [GitHub](https://github.com/GongRzhe/TRAVEL-PLANNER-MCP-Server)
  - The reference MCP servers in modelcontextprotocol/servers-archived are "no longer maintained" — [GitHub](https://github.com/modelcontextprotocol/servers-archived)
- **Other:**
  - liketrek/TREK (15,360★, active Nov 2026): "The most complete open-source travel planner: real-time collaboration, bookings, budgets, packing lists, journ[al]…". A self-hosted app, not a guide. — [GitHub](https://github.com/liketrek/TREK)
  - LetsFG/LetsFG (2,228★): agent-native flight and hotel search and booking MCP — [GitHub](https://github.com/LetsFG/LetsFG)
  - borski/travel-hacking-toolkit (880★): points and miles skills plus MCP — [GitHub](https://github.com/borski/travel-hacking-toolkit)
  - trivago public MCP (used by OpenUI Trip Planner) — [trivago MCP docs](https://mcp.trivago.com/docs)

**Agent repos (LangGraph / CrewAI / ADK)**
- OSU-NLP-Group/TravelPlanner (568★): ICML'24 benchmark; "even GPT-4 only achieves a success rate of 0.6%". Agents "struggle to stay on task, use the right tools… or keep track of multiple constraints". — [GitHub](https://github.com/OSU-NLP-Group/TravelPlanner); [arXiv](https://arxiv.org/abs/2402.01622)
- Typical LangGraph demos:
  - engrazizullah: the day plan is repaired in code (dedupe, hour limits). — [GitHub](https://github.com/engrazizullah/multi-agent-travel-planner)
  - Sonu0701: human-in-the-loop `interrupt()` after the draft. — [GitHub](https://github.com/Sonu0701/multi-agent-travel-planner)
  - Nileshmaharjan: pause and resume from Postgres. — [GitHub](https://github.com/Nileshmaharjan/ai-travel-agent)
  - shreshth-29: CrewAI vs LangGraph implemented side by side. — [GitHub](https://github.com/shreshth-29/Travel_Agent_V1)
- Most-starred general repos are Chinese portfolio or interview projects (e.g., bcefghj/multi-agent-travel-planner 342★) or CrewAI Streamlit demos (AdritPal08 63★). — [GitHub search](https://github.com/bcefghj/multi-agent-travel-planner)
- arpan65/TripAI (6★): a "Multi-agent AI travel planner powered by Claude", 4-phase pipeline. — [GitHub](https://github.com/arpan65/TripAI-Multi-Agent-AI-Travel-Planner)

**Public system prompts**
- LouisShark/chatgpt_system_prompt (10,840★, MIT, active Oct 2026) and linexjlin/GPTs (32,022★, last push Sep 2024) collect leaked GPT prompts. Travel GPT entries exist, but no high-quality travel-guide prompt was verified, and leaked prompts raise ToS and IP concerns. — [GitHub LouisShark](https://github.com/LouisShark/chatgpt_system_prompt); [GitHub linexjlin](https://github.com/linexjlin/GPTs); [BrightCoding (unreliable)](https://blog.brightcoding.dev/2025/08/14/promptcraft-exposed-inside-the-public-vault-of-chatgpt-system-prompts-and-prompt-extraction-tricks)

**Traveler profile schemas**
- DIF HATPro (Hospitality & Travel Profile; Apache-2.0; 1★; active Jun 2026). Modular JSON Schema covering identity, names, contact, "preferences and support needs", "food and dietary preference structures", and "travel profile presentation/query concepts". — [GitHub](https://github.com/decentralized-identity/hatpro-schema-htwg)
- Traveler.md (ChatGPT app) is a commercial "memory for how you travel". Its format is not public. — [ChatGPT listing](https://chatgpt.com/plugins/plugin_asdk_app_6a7cb6d3e938819198aa071ec7cd9647)

### Inferences
- **Quality ranking for this user's purpose:**
  1. **apljacob/travel-agent.** Borrow the principles and the discovery-question-skipping logic. It cannot be redistributed commercially, which is fine for personal use.
  2. **jianhao.** Borrow the "per-city notes that grow" and "pre-delivery checklist" ideas.
  3. **skywain and travel-plan-viz.** Borrow `plan.geo.json` as a structured plan format, and the Leaflet single-file HTML artifact with native-map deep links.
  4. **cablate/mcp-google-map or Grounding Lite** for verified places, hours and routes, if he is willing to create a Google Cloud key within the free caps.
  5. **OSM MCP** as the fully free, no-key fallback. Its coverage in Kathmandu and Bali was not verified.
- **Mobile constraint:** local stdio MCP servers run only in Claude Code or Desktop. Using them from the Claude mobile app requires a remote (Streamable HTTP) deployment added as a custom connector. Several servers support this (cablate, cyanheads OSM, Google Grounding Lite, which is natively remote). This is an inference; custom-connector availability on his plan and on mobile was not verified in this pass.
- The LangGraph and CrewAI demos add little. A single well-written skill plus a profile file plus web search covers what they do. TravelPlanner's 0.6% result argues for keeping constraints explicit in a file rather than relying on long chat context.
- Use HATPro only as a field checklist (dietary, accessibility, support needs). The taste side (vibes, liked and disliked places, pace, contrast pairs) has to be designed ad hoc.

### Gaps
- The Google ADK "travel-concierge" sample (pre-trip, in-trip, post-trip agents with a user-profile state) could not be fetched (repo path moved, 404), so it was not assessed.
- License and maintenance were not verified for repos beyond the search metadata. ErlebnisW/travel-planner status is unknown.
- The full text of a public travel-GPT system prompt was not reviewed.
- OSM POI coverage in Kathmandu and Bali was not checked.

## Q5. Lessons: what measurably improves user satisfaction (metrics, case studies, founder statements)

### Takeaway
Hard satisfaction metrics from AI travel startups are essentially unpublished. The evidence that does exist points the same way. Use is mainstream, including in-destination use (51% of US AI-using travelers). Trust is conditional on verification (~60% verify first). Grounding in live data is the biggest lever: Expedia saw abandonment within a few exchanges without it. Planning-agent benchmarks show that long multi-constraint plans fail without explicit constraint tracking.

### Cited Findings
- Phocuswright "The AI Surge" (US, survey 8–17 Feb 2026): — [Travel Professional News](https://travelprofessionalnews.com/majority-of-u-s-travelers-now-use-ai-for-trips-marking-fastest-behavioral-shift-in-a-decade-new-phocuswright-study-finds/amp/); [Phocuswright](https://www.phocuswright.com/Travel-Research/Consumer-Trends/The-AI-Surge-Travels-Fastest-Behavioral-Shift-in-a-Decade)
  - 56% used AI for planning, booking or in-destination support on at least one trip in the past year.
  - 33% used GenAI for trip research, vs 35% for search engines.
  - 64% of AI travelers use standalone AI platforms, and 81% rate them the most useful environment.
  - 51% used AI for real-time recommendations at the destination.
- Phocuswright 2025: 78% say GenAI improves trip planning; up to 37% trust GenAI recommendations enough to act on them. — [Phocuswright](https://www.phocuswright.com/Travel-Research/Research-Updates/2025/From-hype-to-habit-78-percent-of-travelers-say-GenAI-improves-trip-planning)
- Global Rescue (Sep 2026): ~60% trust AI travel info only after verifying through other sources. — [Global Rescue](https://www.globalrescue.com/common/blog/detail/international-travelers-rapidly-embrace-ai-for-travel-planning-but-trust-remains-conditional/)
- Oliver Wyman: 54% of leisure travelers trust GenAI for inspiration and planning. — [PhocusWire](https://www.phocuswire.com/oliver-wyman-data-genai-travelers-attitude)
- Expedia: ungrounded chatbot answers meant customers left "within a few exchanges". The fix was evaluation and data plumbing, not the model. — [Hospitality.today](https://www.hospitality.today/article/expedia-learned-where-ai-breaks-it-wasnt-the-model). "Point agents" beat an end-to-end chatbot. — [Travel Weekly AU](https://travelweekly.com.au/expedia-ceo-warns-that-end-to-end-ai-chatbots-dont-work/)
- Mindtrip CEO: one closed-restaurant recommendation destroys trust immediately. — [USA TODAY via AOL](https://www.aol.com/news/ai-plan-next-vacation-know-091326308.html)
- TravelPlanner benchmark: GPT-4 0.6% success on multi-constraint plans; failures come from losing track of constraints and tools. — [arXiv](https://arxiv.org/abs/2402.01622)
- Dedicated planners vs general chat: ChatGPT "needed 3–4 follow-up prompts to reach the same specificity a purpose-built tool delivers on first pass", e.g. on budget breakdowns (vendor or affiliate comparison). — [aitravel.tools / roundup](https://aitravel.tools/best-ai-trip-planner/)
- Layla user complaints center on lost instructions and wrong-city results. — [Trustpilot](https://ca.trustpilot.com/review/layla.ai)
- Alice AI critique: no follow-up dialogue and ignored soft goals. — [Tourdom](https://www.tourdom.ru/hotline/obzory-tekhnologiy/ozadachili-alisu-ai-zaprosom-na-podbor-otelya-chtoby-otdokhnut-s-detmi-sobakoy-i-vstretit-lyubov/)
- Skift's Rafat Ali on why "no breakout consumer AI travel startup has emerged (yet)" (podcast). — [PodRocket listing](https://www.podrocket.ai/podcast/85986527-ee8e-48cd-8f41-29c68ac84d08/episode/887884f5-3426-45de-8f97-ee6157575a19). Lola expects ~90% of users on the free tier. — [Skift](https://skift.com/2026/09/29/kayak-co-founders-launch-lola-booking-holdings-new-ai-assistant-exclusive/)
- Airbnb did not disclose models, quality measurements or conversion results for its AI features. — [Rental Scale-Up](https://www.rentalscaleup.com/airbnb-ai-strategy-2026/)

### Inferences
- **Levers a personal Claude guide can copy, ranked by the evidence above:**
  1. **Verify before you recommend.** Web-search hours, closures and "permanently closed" status, and say what was verified (Expedia, Mindtrip CEO, Global Rescue).
  2. **Keep constraints in a persistent file**, not in chat memory (Layla complaints, TravelPlanner).
  3. **Specific over generic.** Give named places with the reason they fit, which closes the 3–4-follow-up gap.
  4. **Ask one smart follow-up instead of zero or many** (Alice critique vs the apljacob single-batch rule).
  5. **Treat in-destination, real-time help as a first-class scenario.** 51% of US AI travelers already use it.
- **Requires proprietary data and cannot be replicated:** live inventory and pricing, Google's place graph and review corpus, Gmail and Photos inference (unless he connects Gmail or Drive to Claude), and human concierge or agents.
- **Free near-substitutes:** Claude's Tripadvisor, Booking.com and Viator connectors (all plans, mobile beta), Claude iOS location plus Apple Maps hand-off, web search, and Google Grounding Lite's free cap.

### Gaps
- No founder interview or case study with retention, NPS or satisfaction deltas was found for Mindtrip, Layla, Stardrift, Wanderboat or Airial.
- No 2026 Phocuswright trust percentage was found.
- The Skift Oct 2025 session "Anthropic's Claude and the Future of Travel Personalization" exists, but its content was not reviewed. — [Skift](https://skift.com/2025/10/31/full-video-anthropics-claude-and-the-future-of-travel-personalization/)
