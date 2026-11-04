# Practitioner Practices: How Real People Use LLM Assistants as Travel Guides, Route Builders and "Where to Go Now" Recommenders (Nov 2025 – Nov 2026)

*Research note for the report writer. Today = 2026-11-04. Window prioritized: Nov 2025 – Nov 2026; older material is flagged [OLDER].*

*Coverage and method: the `last30days` engine was run twice (120-day and 365-day windows). Only Reddit (keyless), Hacker News and GitHub were available. X/Twitter, YouTube and TikTok were NOT available in this environment (no yt-dlp, no X credentials, no ScrapeCreators key), so video and X practice is under-covered. The engine's topical ranking was noisy, so Reddit posts were pulled directly from the arctic-shift public Reddit archive (title search in r/travel, r/solotravel, r/PromptEngineering, r/perplexity_ai, r/JapanTravel, r/GeminiAI, r/ChatGPT). Several large subreddits (r/ClaudeAI, r/digitalnomad, r/Nepal, r/bali, r/ChatGPTPro) timed out on the archive and are NOT covered. Many r/travel and r/solotravel posts about AI are "[removed]" because both subs ban AI content (see Q8). Reddit upvote counts from the archive are captured at ingest time and can be lower than live counts.*

*Credibility tags used below: **[High]** = primary documentation or a named, dated first-person account with specifics; **[Med]** = a named practitioner blog or a Reddit/HN post with engagement and specifics; **[Low]** = a vendor/SEO listicle, a self-promoting post, title-only evidence, or an unverified secondary report.*

---

## Q1. What prompt structures and "travel profile" / "about me as a traveler" documents do people use, and which reportedly improve results most?

### Takeaway
The most consistently reported improvement is to give the model a **reusable traveler profile plus fixed constraints before asking for anything**, and then to ask for options and clusters rather than a finished day-by-day schedule. The most advanced setup reported is a **per-trip Project with a "master document" and a decision log**. Some people add an **anti-preference field** ("places I'm tired of hearing about"), which its author calls the highest-leverage input. No controlled comparison shows which element matters most; the evidence is practitioner testimony.

### Cited Findings
- **Per-trip Claude Project + master doc + decision log.** Dhruv Bhutani planned a 3-week Japan trip in a dedicated Claude Project. A master document held all trip context, and its top section was a **decision log** of major choices (dropping a side trip, changing hotels, days per city). This meant new chats did not need the trip re-explained. Separate reference docs covered a seafood allergy (safe dishes, ingredients to avoid, restaurant phrases), camera lenses, vintage watch shops and streetwear brands. Fixed **"anchors"** (e.g., a pre-dawn Fushimi Inari shoot) were set, and everything else went into **flexible pools** of cafes, shops and neighborhoods. A Chrome MCP let Claude read live pages from URLs he supplied. Android Authority, Sep 30 2026. **[High: named author, recent, Claude-specific; no verbatim prompts given]** — [Android Authority](https://www.androidauthority.com/claude-ai-travel-planning-3715820/)
- Same article: Claude's *unprompted* recommendations "seemed superficial" to someone who already knew Japan. The value came from the author's own curation, not from discovery. **[High]** — [Android Authority](https://www.androidauthority.com/claude-ai-travel-planning-3715820/)
- **"Killer prompt" structure (Jitendra Jain, May 23 2026).** Role: "elite travel architect" that treats destination choice as a constrained-optimisation problem. Bracketed fields: travellers, trip length, travel window, departure airport, max flight time, all-in budget, passports/residency, weather needs, **the real reason for the trip**, likes, things to avoid, hard constraints (diet, allergies, health), and **"places I'm tired of hearing about"**, which the author calls the highest-leverage field. Output: a constraints summary, then 3 destinations, each with a fit rating, the logic, one specific local activity and dining insight, a "reality check" on friction points and a "verify before booking" note, then "my pick" and "if the constraints don't work". The prompt gives the model **explicit permission to say the constraints conflict** and to flag items that need verification. **[Med: named practitioner (hotel marketer), detailed, but not tested]** — [Hotelemarketer](https://hotelemarketer.com/2026/05/23/how-i-plan-every-trip-with-ai-in-2026-the-killer-prompt-the-workflow-around-it-and-what-it-means-for-hotels/)
- Jain's follow-up stress-test is "What would make me regret each one?" He also observes that many prompts ask AI to please everyone and then get "mush". **[Med]** — [Hotelemarketer](https://hotelemarketer.com/2026/05/23/how-i-plan-every-trip-with-ai-in-2026-the-killer-prompt-the-workflow-around-it-and-what-it-means-for-hotels/)
- **Traveler-profile framework from "100+ iterations" (r/PromptEngineering, Jan 11 2026).** (1) Paste a reusable "traveler profile": who is coming and their ages, pace (chill / balanced / packed), interests, budget vibe, constraints (mobility, early mornings, long walks), and rules like **"don't ping-pong me across the city"** and **"cluster by neighborhood"**. (2) Add immovable constraints: flight times, where you are staying, bookings and must-dos, and **"things I've already done on previous visits (so it doesn't recommend the obvious again)"**. (3) Ask for neighborhood clusters, not day-by-day schedules. (4) Generate 15–25 options, then rank the top 5–7 with one-line trade-offs. (5) "Hidden gems" work only with constraints (see Q2). (6) Make the model audit its own plan. The author is promoting an app (Xploro), and the post had low engagement (1 point, 5 comments), but one commenter confirmed: "The audit its own plan step is underrated." **[Med-Low: self-promotional, but concrete and consistent with other sources]** — [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1qadsqp/)
- A commenter on the same thread shares a fill-in template that reads like a dense narrative brief, used "with small, continuous/ongoing tweaks": "My wife and I (ages [age] and [age]…) will travel to ___ … We will take the ___ train from [city]… arriving … around dinnertime. We will stay overnight in ___…" **[Low-Med]** — [r/PromptEngineering comment thread](https://www.reddit.com/r/PromptEngineering/comments/1qadsqp/)
- **Front-load a travel profile and make it persistent.** Fix #7 in Rachel Caldwell's "9 worst AI travel planning mistakes" is to put a personal travel profile first and tell the AI to use it for every answer in the conversation: "Do not revert to generic recommendations." Caldwell, May 18 2026. **[Low-Med: vendor blog promoting its own chat product; no original testing]** — [Travel Anywhere](https://www.travelanywhere.blog/blog/worst-ai-travel-planning-mistakes-prompts)
- **Pace and energy statements as profile lines** (verbatim examples): "I travel best with one major activity per day and unhurried afternoons"; "my partner needs at least one slow morning in three". Budge blog, May 24 2026. **[Low-Med: vendor blog, but practical]** — [Budge](https://budge.me/blog/what-ai-gets-wrong-travel-recommendations)
- **Russian-language practitioner patterns (RBC Style, Dec 29 2025):**
  - Role + task + format. Example: "ИИ-дизайнер путешествий, лучший в мире тревел-агент и опытный путешественник"; days split into «Утро / день / вечер»; route logic explained.
  - A fixed per-country "folder" prompt: «Я буду в Китае, в городе Гуанчжоу, 30 дней и буду задавать тебе вопросы на любые темы», with separate chats per task.
  - A compact personal-context line: «живу в таком-то районе, люблю прогулки и еду, не люблю экскурсии в музеях на пять часов, есть только полдня».

  **[Med: named interviewees, dated, Russian audience]** — [RBC Style](https://style.rbc.ru/impressions/694d0e3f9a7947fe74c4831a)
- **"Interview me first" as part of the structure.** Jain's "Plan" stage has the AI ask 8–10 targeted questions before drafting. He then gives hard constraints (driving limits, meal rules, rest days) and asks the model to check its own draft against them. **[Med]** — [Hotelemarketer](https://hotelemarketer.com/2026/05/23/how-i-plan-every-trip-with-ai-in-2026-the-killer-prompt-the-workflow-around-it-and-what-it-means-for-hotels/)
- **Fixed output format worth reusing:** day → morning / lunch / afternoon / evening, with **one "book ahead" flag and one rainy-day swap per day**. The plan was written by Claude and published with a form that deep-links a prefilled prompt into ChatGPT (`chatgpt.com/?q=`), Claude (`claude.ai/new?q=`) or Google AI Mode. The poster says the Gemini app does not accept prompts from a link. r/ChatGPT, Sep 20 2026. **[Low: 0 points, self-built tool; the deep-link behaviour is the poster's claim and not independently verified]** — [r/ChatGPT](https://www.reddit.com/r/ChatGPT/comments/1wledpf/)
- Australian press guidance also recommends a personal travel profile, letting the bot ask follow-up questions, and "lots of pushback". **[Low-Med: snippet-level]** — [The Nightly](https://thenightly.com.au/lifestyle/travel/ai-bots-can-help-plan-your-next-holiday-if-you-ask-the-right-questions-c-22914439)

### Inferences
- Three elements recur across independent sources: (a) a stable profile, (b) explicit anti-preferences or "already done", and (c) explicit pace and energy rules. Together they are the practitioner consensus "travel profile". The decision-log idea (Android Authority) is the one uniquely suited to long trips with many chats.
- For a voice-dictating mobile user, a profile kept in a Claude Project (or in memory) avoids re-dictating context each time. Practitioners report that re-explaining context is the main friction.
- "The real reason for the trip" and "places I'm tired of" are cheap fields with outsized effect according to their author. They suit a frequent Asia traveler who has already seen the classics.

### Gaps
- No A/B evidence on which profile fields matter most. All claims are testimonial.
- No published "traveler profile" document written for Claude's memory or Projects specifically (as opposed to pasted text) was found, beyond the Android Authority description.

---

## Q2. What techniques get beyond generic top-10 tourist answers?

### Takeaway
"Hidden gems" phrasing alone returns the same recycled list. What practitioners report working is: **hard filters** (radius from base, "not top-10", a *specific reason* to go such as market day or sunset angle); **anti-preferences and an "already done" list**; **searching in the local language or on local platforms** (the strongest specific tip, reported for Perplexity); **asking for categories and neighborhoods rather than names**; **forcing trade-offs and ranking**; and **"what am I not asking about"** questions. A structural limit remains: models over-weight SEO and travel-blog content and show measurable popularity bias.

### Cited Findings
- "If you ask for 'hidden gems', you'll get the same recycled list." This only becomes useful with filters: "within X minutes of where I'm staying", "not top-10 tourist stuff", and "give a *specific reason* to go (market day, sunset angle, seasonal specialty, etc.)". r/PromptEngineering, Jan 11 2026. **[Med-Low]** — [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1qadsqp/)
- **Search in the local language.** "One really goated feature… making Perplexity search in the language of the country you are visiting." English searches miss specific info. In the comments, u/nexflatline says: "Almost all my prompts start with 'Search in Japanese on Japanese sources…' and it actually strictly follows the instructions." The same commenter says Gemini "still appears strongly biased by English results". Another commenter asks devs to make this automatic. r/perplexity_ai, Mar 31 2026, 28 points. **[Med: concrete, corroborated by a commenter; Perplexity-specific]** — [r/perplexity_ai](https://www.reddit.com/r/perplexity_ai/comments/1s8j8no/)
- **Local platforms hold the local data.** The cited platforms are Dianping, Xiaohongshu and Mafengwo (China), Tabelog (Japan) and Naver (Korea; Naver now integrates Tabelog data). The suggested prompt asks the model to name the local platform per destination and cite recent reviews from it. **[Low-Med: vendor blogs plus a Korea Times news item]** — [Voyaige](https://voyaige.to/blog/best-ai-travel-planner-for-china-2026); [Korea Times](https://www.koreatimes.co.kr/business/tech-science/20250801/naver-partners-with-tabelog-to-offer-restaurant-search-in-japan); [Budge](https://budge.me/blog/what-ai-gets-wrong-travel-recommendations)
- **Category vs. name rule.** "AI can tell you which neighbourhood to look in and what kind of restaurant to find — the specific name is the part you need to verify." AI is reliable for the neighbourhood, restaurant type and price tier. **[Low-Med: vendor blog, but consistent with incident evidence in Q5]** — [Budge](https://budge.me/blog/what-ai-gets-wrong-travel-recommendations)
- **Gap-finding questions** (verbatim): "what should I know about Lisbon that most travel guides skip", "what am I not asking about", "what's wrong with this plan". Budge, May 24 2026. **[Low-Med]** — [Budge](https://budge.me/blog/what-ai-gets-wrong-travel-recommendations)
- **Anti-preferences field:** "places I'm tired of hearing about" is called the highest-leverage field. **[Med]** — [Hotelemarketer](https://hotelemarketer.com/2026/05/23/how-i-plan-every-trip-with-ai-in-2026-the-killer-prompt-the-workflow-around-it-and-what-it-means-for-hotels/)
- **"Already done" list:** listing "things I've already done on previous visits" stops "tourist brochure mode". **[Med-Low]** — [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1qadsqp/)
- **Persona of a local insider for cultural nuance:** Valeria Kutkina used a "5.2 Thinking" model with search and assigned the persona «ты мужчина, житель Малайзии с семейной историей в несколько поколений, уважающий религиозные традиции». She paired it with her own role («я женщина-турист, предпочитаю стильную, но удобную одежду») to check religious and dress nuances. Separately, Tagir Khairutdinov uses AI to find alternatives to popular places and avoid queues. **[Med]** — [RBC Style](https://style.rbc.ru/impressions/694d0e3f9a7947fe74c4831a)
- **Vibe-style descriptive prompts work in Google's Ask Maps.** Google's own examples include "a quiet, dim bar within a mile for a solo outing, suited to reading", a rooftop or park where the setting sun won't shine into the camera, and a scenic walking route timed to arrive at sunset. 9to5Google, Mar 31 2026. **[High for what Google recommends; not evidence of quality]** — [9to5Google](https://9to5google.com/2026/03/31/google-shows-how-you-should-use-ask-maps-as-the-feature-rolls-out-widely/)
- Ask Maps can also be asked to "explain its choices or surface lesser-known spots". BGR, Oct 8 2026. **[Med]** — [BGR](https://www.bgr.com/2276065/things-ask-gemini-for-better-google-maps-results/)
- **Mixed results on Ask Maps for hidden gems.** One reviewer says the suggestions work for tourist staples but "fall flat off the beaten path". Another (Tom's Guide) was enthusiastic. Reviewers note that the real work is done by human reviews that Gemini merely synthesizes. **[Low-Med: aggregated via search; Tom's Guide body not retrievable]** — [Tom's Guide](https://www.tomsguide.com/ai/i-prompted-gemini-in-google-maps-to-find-local-hidden-gems-and-now-i-have-loads-of-new-places-to-check-out); [letsdatascience](https://letsdatascience.com/news/google-integrates-gemini-into-maps-itinerary-planning-35d9431b)
- **Structural limit: SEO bias.** u/Icy_Essay_7490 tested the approach in cities he knows well: "The AI is good at telling obvious things. But once you foray into something more niche, it's worse than hit and miss… the models take industrial-SEO content much more seriously than it deserves." r/PromptEngineering, Mar 2026. **[Med: a single experienced commenter]** — [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1rv4v3q/)
- A second commenter on the same thread: for "traditional" food requests, the model sometimes suggests places where the dishes are "traditional" but "somehow reinvented". **[Med]** — [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1rv4v3q/)
- **Academic evidence of popularity bias.** Drápela (2025, Mendel University conference paper) tested GPT models on Czech destinations and found a strong bias toward established hotspots, with lesser-known places rarely recommended. Collab-REC (arXiv 2508.15030, v4 March 2026) is a multi-agent framework that measurably increases diversity and surfaces lesser-visited locales versus a single-agent baseline. **[High-Med: academic, but small scope; Europe only]** — [Mendel University Press](https://doi.mendelu.cz/artkey/doi-990008-5700_THE-ALGORITHM-EFFECT-HOW-AI-DRIVEN-TRAVEL-PLANNING-FUELS-OVERTOURISM.php?l=en); [arXiv 2508.15030](https://arxiv.org/html/2508.15030v4)
- **Poisoned sources.** A r/travel user (Oct 20 2026, 620 points, ~100 comments) found that a Montenegro trip had "wrong times, wrong distances, wrong landmarks" in hike info "verified even with multiple source". He traced this to a network of near-100% AI-generated travel sites (named domains include montenegro-spirit, japan-atlas, georgia-spirit, seoul-spirit, busan-trip, sardinia-trip) that are heavily backlinked and cited by AI tools. His test was to ask an AI about cheap food in Sardinia and check its sources; the network's site appeared. A top comment (47 points): "All the AIs are reading the SEO and AI travel blogs and then regurgitating it into more AI slop." **[Med-High: high engagement, specific, reproducible test]** — [r/travel](https://www.reddit.com/r/travel/comments/1xauh1u/)

### Inferences
- In practice, "non-obvious" comes from **constraints plus local-language and local-platform sourcing plus the user's own seeds**, not from the words "hidden gem". In the Android Authority case, the good picks came from the author's own lists (watch shops, streetwear) that Claude then organized.
- For Nepal, Bali or India, the analog of "search in Japanese" would be to ask Claude to search in Nepali, Indonesian or Hindi and in local outlets. No source tested this for those languages (see Gaps).
- Asking the model to **show its sources and drop anything sourced only from generic SEO or AI-farm sites** directly counters the Montenegro failure mode. This is an inference from the r/travel post; no one documented it as a prompt.

### Gaps
- No evidence found specific to Kathmandu, Bali or India on hidden-gem prompting. The r/Nepal and r/bali archive searches timed out.
- No quantitative comparison of "local-language search" vs English search beyond one Reddit anecdote.
- X/TikTok/YouTube creator tips (e.g., "TikTok/Instagram saves → itinerary") are under-covered because those sources were unavailable.

---

## Q3. How do people handle "I don't know what I want" (mood-based prompts, interviewing prompts, A/B option prompts)?

### Takeaway
The dominant practice is to **make the assistant interview you first** ("ask me N constraints before planning"). The model then offers **contrasting versions**: high-energy vs low-energy day, a rainy-day backup, or 3 options with trade-offs and a regret test. Some app builders complain that interviews feel like "20 questions", so keep them short.

### Cited Findings
- "The single best change I made was forcing the assistant to ask me questions first." The prompt: «ask me 10 constraints about pace, budget, food priorities, transit tolerance, and **what I will regret if I miss**». It then asks for **two versions: high energy days and low energy days, plus a rainy day backup**. r/perplexity_ai, Dec 18 2025, 75 points. Commenters add "build an itinerary that supports two different energy levels in the same day" (for two travelers) and "The rainy day backup saves trips." **[Med: decent engagement, concrete]** — [r/perplexity_ai](https://www.reddit.com/r/perplexity_ai/comments/1ppmldi/)
- Interview pattern: "Before you draft any itinerary, ask me 8–10 specific questions." This is followed by a 3-destination output with fit ratings, a "my pick", and the follow-up "What would make me regret each one?" **[Med]** — [Hotelemarketer](https://hotelemarketer.com/2026/05/23/how-i-plan-every-trip-with-ai-in-2026-the-killer-prompt-the-workflow-around-it-and-what-it-means-for-hotels/)
- An options-not-plan example: three trip ideas within two hours of Madrid by train, each with its main trade-offs, "which gives you choices to react to". **[Low: listicle-level, via search summary]** — [Kayak](https://www.kayak.com/news/ai-travel-prompts/)
- Shortlist mechanic: generate 15–25 options and rank the top 5–7 with one-line "why this over that". **[Med-Low]** — [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1qadsqp/)
- Counter-signal: an app builder posted "planning with AI still feels like a 20-question interview" (r/travel, Sep 25 2026; post removed, title-only evidence). **[Low]** — [r/travel](https://www.reddit.com/r/travel/comments/1wpw3cu/)
- Mood-based day-plan apps exist ("Show HN: I made a travel app that instantly builds day plans based on your mood"). **[Low, OLDER: 2025 HN]** — [Hacker News](https://news.ycombinator.com/item?id=43735630)
- Event-aware date choice as a decision aid: "what's happening in [city] on these 3 weekends, big concerts, sports, conferences, and which one looks the quietest?" The same post adds a calibration line: "If you're not sure about something, say so and tell me where to check." r/GeminiAI, Oct 19 2026. **[Low-Med: low engagement, but a useful pattern]** — [r/GeminiAI](https://www.reddit.com/r/GeminiAI/comments/1x9whtl/)

### Inferences
- For a voice user who "often doesn't fully know what he wants", a good fit is a **short interview (3–5 questions, one at a time)** followed by **2–3 contrasting options** (classic / unusual / low-energy) with trade-offs. Long questionnaires are a reported annoyance.
- "What will I regret missing?" and "What would make me regret each option?" are two cheap, memorable questions that recur across independent sources.

### Gaps
- No found practitioner material on purely mood-based prompting (e.g., "I feel tired and curious, 2 hours, Thamel") with reported outcomes.
- No evidence on the ideal number of interview questions.

---

## Q4. On-the-go workflows: voice mode, location sharing, screenshots, photo of a menu or street, "I have 2 hours here" prompts; what works on mobile?

### Takeaway
People use **voice through earbuds as a walking companion** (Gemini with GPS, ChatGPT voice), **photos of menus and order sheets** for translation and dish explanation, and in-trip questions **inside the trip project** so context carries over. Claude's mobile app now has an official **location tool and interactive map** (open in Apple Maps on iOS or Google Maps on Android). A recurring complaint is that voice guides do not know exactly where you are standing unless location is shared.

### Cited Findings
- **Claude mobile location tool (official).** Claude can use your location for "contextual suggestions for nearby places and services" and will request access when relevant. It displays locations on an interactive map, and you can select a location to open it in Apple Maps and get turn-by-turn directions. Example prompts: "Find good restaurants near me that are open now"; "Show me coffee shops within walking distance on a map." The feature is "supported on all Claude plans", but "Members of Team or Enterprise plans can't access the location tool at this time." **[High: official help page]** — [Claude Help Center (iOS)](https://support.claude.com/en/articles/11869619-use-claude-with-ios-apps)
- On Android, suggested locations appear on an interactive map and open in Google Maps (per the Android help page, as summarized by search). **[High-Med: official page, seen via search summary]** — [Claude Help Center (Android)](https://support.claude.com/en/articles/11869629-use-claude-with-android-apps); [Does Claude use my location?](https://privacy.claude.com/en/articles/11186740-does-claude-use-my-location)
  - Conflict: a third-party guide says the feature is beta, Pro/Max-only and US-only as of Oct 2026. This contradicts the official "all plans" wording. **[Low]** — [lilachbullock.com](https://www.lilachbullock.com/claude-mobile-app/)
- **Earbuds + Gemini as a walking guide.** While solo traveling in Portugal and Spain, the poster talked to the Gemini app through earbuds while walking, asking about passing buildings, street history and "where locals actually eat nearby". Persona prompts ("a cultural historian or a witty traveler") made it "almost like walking around with a personal guide". "Since it can use your GPS location, it actually knows where you are." r/PromptEngineering, Mar 16 2026, 35 points, 24 comments. Caveats in the comments: niche recommendations are "worse than hit and miss" and closed places still appear ("check anyway the opening hours in google maps"). The prompt PDF was sold via Gumroad (self-promotion). **[Med]** — [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1rv4v3q/)
- **ChatGPT voice as a tour guide at Teotihuacan** "worked better than expected, but it had no idea where I was standing". r/travel, Jul 31 2026; title-only, the post body was removed under the sub's AI rule. **[Low: title only]** — [r/travel](https://www.reddit.com/r/travel/comments/1vbf6p3/)
- **In-trip division of labour.** Jain uses Gemini for routing, drive times and "open now" checks via its Google Maps integration, and ChatGPT for voice and conversational in-trip use. He asks in-trip questions inside the trip project so the model already has context, uses camera translation for menus and signs, and downloads offline language packs before flying (connectivity "is the first assumption to break in transit"). **[Med]** — [Hotelemarketer](https://hotelemarketer.com/2026/05/23/how-i-plan-every-trip-with-ai-in-2026-the-killer-prompt-the-workflow-around-it-and-what-it-means-for-hotels/)
- **Low-energy pivot and rain pivot in a Claude Project.** When tired in Shinjuku, Claude suggested nearby low-energy options and an allergy-safe ramen place. When rain hit the Fuji plans, it drew replacements from the pre-built flexible pool. **[High]** — [Android Authority](https://www.androidauthority.com/claude-ai-travel-planning-3715820/)
- **Menu photos (Russian practitioners).** Standing prompt: «Я буду присылать фотографии меню — прошу объяснять, что это за блюда, подходят ли они мне как европейцу», plus «сразу показывать цены в юанях, долларах и рублях по актуальному курсу». Another practitioner sends photos of Korean order cards. Practitioners also advise not giving the assistant passport or bank-card data. **[Med]** — [RBC Style](https://style.rbc.ru/impressions/694d0e3f9a7947fe74c4831a)
- **Ask Maps (Gemini inside Google Maps)** answers micro-logistics questions: parking, entrances, queue times, reservation policies, stroller or wheelchair access, laptop-friendly cafes with outlets. It can pin places and save them to a Maps list. Queue info "can try" to draw on recent reviews and may not be reliable. BGR, Oct 8 2026. **[Med]** — [BGR](https://www.bgr.com/2276065/things-ask-gemini-for-better-google-maps-results/)
- **Ask Maps availability:** as of Mar 31 2026 it is available to "all Maps users in the US and India", on Android and iOS only, with desktop to come "eventually". **[High]** — [9to5Google](https://9to5google.com/2026/03/31/google-shows-how-you-should-use-ask-maps-as-the-feature-rolls-out-widely/)
- Ask Maps limits: it needs an internet connection, sparse Google listings in many regions limit its usefulness, and queries go to Google servers. **[Low-Med]** — [travel-tools-guide](https://travel-tools-guide.pages.dev/blog/google-maps-ask-maps-gemini-ai-travelers-2026)
- **Third-party "audio guide" GPTs** exist, e.g., photograph a landmark to hear its story. **[Low]** — [ChatGPT "Audio Guide" GPT](https://chatgpt.com/g/g-PtcICfyMd-audio-guide)

### Inferences
- For a Claude-mobile, voice-first user, the officially supported path for "here and now" is: **grant location, ask by voice for N options open now within X minutes' walk, have them shown on the map, open in Google Maps**. This covers the most common on-the-go need without third-party tools.
- Ask Maps would be a strong verifier or second opinion in **India**, but per the March 2026 report it is not available in **Nepal or Indonesia**. Its status there should be checked on device (see Gaps).
- The "had no idea where I was standing" complaint suggests telling the model the exact location (a street or landmark name, or a screenshot of the map) when using a voice mode that has no location tool.

### Gaps
- No found first-person account of Claude's voice mode used as a walking guide (all voice-guide accounts were Gemini or ChatGPT).
- Ask Maps rollout beyond US and India after March 2026 is unconfirmed.
- No account found of people sending map screenshots to an LLM for "where now" decisions, though it is plausible.
- The "I have 2 hours here" prompt pattern was not documented with outcomes. The closest is the Atlanta 3-hour test (Q8).

---

## Q5. Verification: how do people catch hallucinated or closed places, cross-check with Google Maps and reviews, and handle recency?

### Takeaway
Verification is universally recommended. The concrete practices are: (1) build **confidence and verification flags into the prompt**; (2) **cross-model audit**, e.g., a Claude or Opus draft checked by Gemini, which is grounded in Google Maps business data (HN users say it caught closing hours and permanent closures "on every nit"); (3) a **two-source rule**, with addresses and hours checked in Maps or a search engine; (4) **Google Maps sorted by "Newest" reviews**, plus local platforms; and (5) checking the AI's **cited sources** for AI-generated "content farm" sites.

### Cited Findings
- **Cross-model audit.** On HN (~early Sept 2026), u/jampa drafted an itinerary with Opus, then had Gemini 3.7 Flash review it. It flagged "this place will close 5PM" and "this place is closed for good": "It was right on every nit." Others note that Gemini runs web search on most queries, and a commenter identifying as Google AI says its grounding uses the same business data (including hours) as Google Maps. Another argues any model with web search could check hours. **[Med: multiple corroborating commenters; one self-identified insider]** — [Hacker News](https://news.ycombinator.com/item?id=49538512)
- **Restaurant prompt with an open-status confidence level** (fix #4): request 5 restaurants, each with an open-status confidence level, **a Google Maps search term** and a backup; "Do not recommend any restaurant if you are uncertain it is still operating." Fix #1 for hotels: give the year the information is from and what to verify; forbid fabricated availability or pricing. Fix #3: "Do not present any entry requirement as confirmed fact." **[Low-Med: vendor blog]** — [Travel Anywhere](https://www.travelanywhere.blog/blog/worst-ai-travel-planning-mistakes-prompts)
- **Calibration line:** "If you're not sure about something, say so and tell me where to check." The poster says "it stops it from sounding sure when it isn't." **[Low-Med]** — [r/GeminiAI](https://www.reddit.com/r/GeminiAI/comments/1x9whtl/)
- **Verification channels:** Google Maps sorted by "Newest" reviews; Tabelog (Japan); The Infatuation (major Western cities); recent-dated local food blogs; someone who visited within the last year; official government advisories for visas. **[Low-Med]** — [Budge](https://budge.me/blog/what-ai-gets-wrong-travel-recommendations)
- **Two-source rule (Russian practitioners):** AI as the base, with addresses, opening hours and schedules checked via a search engine or maps. Other checks: maps, reviews, local sources, and asking locals (e.g., taxi drivers). AI "не может сказать «я не знаю» и выдумывает ответы"; it does not see repairs, strikes, closures or queues. **[Med]** — [RBC Style](https://style.rbc.ru/impressions/694d0e3f9a7947fe74c4831a)
- **Check what can change right before departure:** «ИИ можно доверить каркас путешествия», but «всё, что способно измениться к моменту приезда, нужно проверять отдельно непосредственно перед выездом». The author also found the AI worked well with sources he supplied himself; errors came from current-state data. Rambler, Oct 4 2026 (ChatGPT, Caucasus road trip). **[Med]** — [Rambler](https://sci.rambler.ru/soft/57165853-kak-ya-splaniroval-puteshestvie-cherez-ii-i-sovershil-oshibku/)
- **Source auditing:** ask the AI for its sources and check them. In the Montenegro case, the cited sources were AI-generated sites. **[Med-High]** — [r/travel](https://www.reddit.com/r/travel/comments/1xauh1u/)
- **Self-audit:** "ask the model to sanity-check timing, travel time, closures, and anything likely to require reservations." "AI is often better at fixing a draft plan than generating a perfect one from scratch." **[Med-Low]** — [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1qadsqp/)
- **Cross-tool check before booking** (fix #9): cross-check factual claims across tools and manually verify disagreements. The supporting statistic is a 2024 Skift survey claim **[OLDER]**. **[Low-Med]** — [Travel Anywhere](https://www.travelanywhere.blog/blog/worst-ai-travel-planning-mistakes-prompts)
- **Known hallucination and closure cases (for calibration):**
  - Peru's non-existent "Sacred Canyon of Humantay", reported by the BBC (tourists paid ~$160). **[OLDER: autumn 2025]**
  - A hallucinated Lisbon restaurant, "Palácio do Mago".
  - An SEO Travel audit: ~90% of AI itineraries had at least one error; 40% of Barcelona itineraries included Tickets Bar (closed 2020); a never-existing "Antico Caffe Ponit" in Rome.
  - Tsukiji inner market (closed 2018) still suggested.

  **[Med: widely re-reported; the percentages come from a marketing agency]** — [WebProNews](https://www.webpronews.com/ai-hallucinations-in-travel-apps-lead-to-fake-landmarks-and-dangers/); [Earth's Attractions](https://www.earthsattractions.com/ai-travel-fails/); [Breitbart (citing BBC)](https://www.breitbart.com/tech/2025/10/06/travelers-using-ai-to-plan-vacations-are-disappointed-when-destinations-dont-exist/)
- Gemini Flash recommended "Lacquer Lounge on Gough" in Hayes Valley as a wine bar. It is a nail salon, "Has been since 2025." The poster: "For finding somewhere to eat tonight I still just text [a friend] or check google maps." r/GeminiAI, Sep 24 2026. **[Med: specific, verifiable claim; low engagement]** — [r/GeminiAI](https://www.reddit.com/r/GeminiAI/comments/1woye1u/)
- Russian cases:
  - 2 of 5 suggested hotels were fictional and 1 had closed in 2022.
  - A "coffee shop with Ararat view" turned out to be a pharmacy.
  - ChatGPT told Spanish tourists that no visa or ESTA was needed for Puerto Rico.
  - A winter road closure to Amberd fortress was ignored.

  **[Med]** — [RBC Style](https://style.rbc.ru/impressions/694d0e3f9a7947fe74c4831a)
- A Greetwell survey: 55% of 485 US travelers who used AI for travel got at least one recommendation that was wrong, unavailable, closed or non-existent. **[Low-Med: vendor survey via Hostelworld blog]** — [Hostelworld](https://www.hostelworld.com/blog/what-ai-is-actually-good-for-when-youre-planning-a-trip/)

### Inferences
- The highest-leverage, cheapest verification for a Claude user is to **force a verification column**: confidence it is still open, a Google Maps search term or link, and "verify" flags. Then spot-check in Google Maps by "Newest" reviews. A second-model audit by Gemini is useful because Gemini is grounded in Maps business data (per HN).
- Specific named venues in less-documented places are the riskiest outputs. Category-level advice is safer. This matters for Kathmandu side streets and Bali villages.

### Gaps
- No systematic measurement of Claude's closure or hallucination rate with web search on vs off for travel.
- No Nepal-specific verification practice was found (e.g., Pathao or local apps, Nepali Facebook groups).

---

## Q6. Route outputs: multi-stop Google Maps links, saved lists, KML/My Maps, artifacts with maps; walking-time realism

### Takeaway
Practitioners convert AI output into maps in four ways:
1. **Google Maps directions URLs** (`/maps/dir/?api=1&…&waypoints=…&travelmode=walking`). These have hard waypoint limits: 3 on mobile browsers, 9 otherwise.
2. **Clusters exported to Google My Maps**, often via KML.
3. **Claude Code / agent skills** that generate KML for Organic Maps or My Maps, or an HTML map with color-coded days and one-tap Maps links.
4. **Ask Maps**, which can pin places and save them to a Maps list.

Walking-time realism is a known weakness: AI plans underestimate transit and buffers, so practitioners prefer neighborhood clusters.

### Cited Findings
- **Official Google Maps URL format:** `https://www.google.com/maps/dir/?api=1&origin=…&destination=…&travelmode=walking`, with `waypoints=` separated by `|` (encoded `%7C`). Optional `waypoint_place_ids` must be in the same order as the waypoints. Limit: "up to three waypoints supported on mobile browsers, and a maximum of nine waypoints supported otherwise." Search URL: `https://www.google.com/maps/search/?api=1&query=…` (optional `query_place_id`). The docs show walking and waypoints in separate examples, not combined. **[High: official docs]** — [Google Maps URLs docs](https://developers.google.com/maps/documentation/urls/get-started)
- Multi-stop limits in practice: Google Maps directions allow about 10 stops. Google does not optimize stop order (you drag stops manually). "Send to phone" does not support multi-stop routes. Transit directions don't support multiple destinations. Workarounds include chaining several routes. **[Low-Med: route-tool vendors]** — [Routerra](https://routerra.io/blog/googlemaps-more-then-10-stops); [Routific](https://www.routific.com/blog/google-maps-multiple-stops)
- **Clusters to My Maps:** Claude grouped designer shops by geographic area, and the author turned those clusters into a Google My Maps file. **[High]** — [Android Authority](https://www.androidauthority.com/claude-ai-travel-planning-3715820/)
- **Agent skills (GitHub, 2026):**
  - skywain/trip-planner-skill (Claude Code, Codex, Gemini CLI etc.) produces hour-by-hour days, map links and an **offline KML for Organic Maps / Google My Maps**.
  - kevinsslin/wayfarer (Obsidian) exports KML with one layer per day.
  - theoms/co-work-travel-planner-claude generates an **HTML map with all stops pinned, color-coded by day, plus one-tap Google Maps links**.
  - d-wwei/trip-planner builds a Leaflet map with navigation buttons and "verified travel times".
  - deusyu/google-maps-skill and galmeida9/Claude-maps-itinerary are Claude Code Maps skills.

  **[Med: real repos; maintenance and quality not assessed]** — [skywain/trip-planner-skill](https://github.com/skywain/trip-planner-skill); [kevinsslin/wayfarer](https://github.com/kevinsslin/wayfarer); [theoms/co-work-travel-planner-claude](https://github.com/theoms/co-work-travel-planner-claude); [d-wwei/trip-planner](https://github.com/d-wwei/trip-planner); [deusyu/google-maps-skill](https://github.com/deusyu/google-maps-skill); [galmeida9/Claude-maps-itinerary](https://github.com/galmeida9/Claude-maps-itinerary/blob/main/SKILL.md)
- **KML import constraints noted in a repo PR:** no folders or MultiGeometries, plain-text descriptions, under 5 MB and 2,000 rows. These were not verified against Google's help page. **[Low-Med]** — [Colin-Travel-Planner PR #135](https://github.com/FriendOfMankind/Colin-Travel-Planner/pull/135)
- **A Google Maps connector for Claude** exists via MCP (Composio), which lets Claude search places rather than rely on model memory. **[Med]** — [Composio](https://composio.dev/toolkits/google_maps/framework/claude-cowork)
- **Ask Maps can pin and save to a Maps list** (e.g., vintage shops in an area). **[Med]** — [BGR](https://www.bgr.com/2276065/things-ask-gemini-for-better-google-maps-results/)
- **Gemini is rated best at visit ordering:** it is "the best at taking a cluster of places and working out a visiting order" and has "much better route planning tools than the other models". But multi-leg transit (train + bus + walk) "worked meh". **[Med]** — [Hacker News](https://news.ycombinator.com/item?id=49538512)
- **Walking-time realism failures:**
  - A 3-hour ChatGPT Atlanta itinerary took 4.5 hours, with "one hour in each place, with no time allotted for travel".
  - A Seoul plan with up to 9 stops in a day.
  - Two hours allotted for Changing of the Guard (45 minutes in reality).

  **[Med: hands-on tests; dates vary, some OLDER]** — [AOL](https://www.aol.com/travel-easy-tested-chatgpt-itineraries-090628315.html); [iVisitKorea](https://www.ivisitkorea.com/how-ai-travel-planners-can-ruin-your-trip/)
- **Distances are approximated, not measured.** Neural networks approximate distances from training-data weights rather than measuring physical tracks; check every leg in a navigator. The article cites an estimate that "even the most advanced GPT" produced only 4.4% successful routes. **[Med: Habr corporate blog; the 4.4% figure is likely from an older benchmark]** — [Habr (tsnis)](https://habr.com/ru/companies/tsnis/articles/1094872/)
- Clustering instead of timed schedules: "Day-by-day outputs often look impressive but fall apart in real life: too much travel time, unrealistic pacing, and bouncing across the city." **[Med-Low]** — [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1qadsqp/)
- A Russian comparison (ChatGPT, Grok, Claude, same prompt) found similar answers, with Grok more accurate and **Claude producing an optimal, non-overloaded route that accounted for travel time**. **[Low-Med: seen via search snippet only; page returned 502 on fetch]** — [Московские новости (mn.ru)](https://www.mn.ru/smart/kak-planirovat-puteshestvie-s-pomoshhyu-ii-ot-vybora-lokaczii-do-marshruta-na-den)

### Inferences
- For a phone-first user, links should be **split into chunks of ≤3 waypoints**, or use a single destination per link plus a separate search link per place, because mobile browsers cap waypoints at 3. Whether the Google Maps *app* accepts more when opened from a link is not documented here.
- Claude can produce Google Maps search or directions URLs as text. Claude Code can go further and generate KML or an HTML map artifact. The Claude mobile location tool already offers "show on map, open in Google Maps" for nearby places.
- Asking the model to **cluster by neighborhood and give realistic walking minutes plus a 20–30% buffer** is a defensive practice suggested by the failure evidence. It is an inference; no source specified a buffer percentage.

### Gaps
- No test found of how reliably LLMs write *correct* multi-stop Maps URLs (typos, wrong encoding, wrong order).
- Google My Maps import limits are not verified from Google's own help page.
- Organic Maps / Maps.me usage with AI output in Asia (offline needs) is only mentioned in one repo.

---

## Q7. Memory and feedback loops: logging what you liked, feeding it back, using Claude/ChatGPT memory for travel taste

### Takeaway
The explicit practice is a **post-trip review written in the same project, pasted into future "dream" prompts**, and a **decision log** in the trip's master document. Assistant memory has matured. ChatGPT's 2026 "Dreaming" memory builds topic dossiers that explicitly include travel preferences and rewrites stale trip facts. Claude opened memory (and Projects) to free users in March 2026. Systematic "taste logs" of liked and disliked places are rarely documented.

### Cited Findings
- **Reflect stage:** write a personal trip review in the same project, then paste it into future Dream prompts. **[Med]** — [Hotelemarketer](https://hotelemarketer.com/2026/05/23/how-i-plan-every-trip-with-ai-in-2026-the-killer-prompt-the-workflow-around-it-and-what-it-means-for-hotels/)
- **Decision log at the top of a master doc** in a Claude Project, so new conversations need no re-explanation. **[High]** — [Android Authority](https://www.androidauthority.com/claude-ai-travel-planning-3715820/)
- **"Things I've already done on previous visits"** in the reusable profile. **[Med-Low]** — [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1qadsqp/)
- **ChatGPT "Dreaming" memory (mid-2026).** OpenAI's example says ChatGPT "already knows from past travel planning that you enjoy wildlife photography, prefer hotels with strong AC, and enjoy a quiet dinner over a crowded bar". Memory revises itself ("you're going to Singapore in July" becomes "you went to Singapore in July 2026"). The press describes "narrative dossiers… sorted by work, hobbies, and travel preferences". Users can review and correct the memory summary; Temporary Chat keeps one-offs out. **[High-Med: OpenAI page returned 403 on fetch; content via search snippets and The Decoder]** — [OpenAI](https://openai.com/index/chatgpt-memory-dreaming/); [The Decoder](https://the-decoder.com/chatgpt-now-saves-narrative-dossiers-about-you-sorted-by-work-hobbies-and-travel-preferences/); [MakeUseOf](https://www.makeuseof.com/chatgpt-now-remembers-your-preferences-automatically-and-it-actually-works/)
- **Critique of memory-based travel personalization:** "The agent remembers what she liked. Not where she stayed." A recalled preference is not the same as a recalled hotel, and no study shows memory changing which hotel an assistant names. **[Med: trade-press commentary]** — [Hospitality.today](https://www.hospitality.today/article/the-agent-remembers-what-she-liked-not-where-she-stayed)
- **Claude memory for free users from March 2026**, with an import tool from other assistants. Projects are available on the free tier per press reports. **[Med: press, not Anthropic primary]** — [Engadget](https://www.engadget.com/ai/anthropic-brings-memory-to-claudes-free-plan-220729070.html); [aiproductivity.ai](https://aiproductivity.ai/news/anthropic-claude-memory-free-tier-chatgpt-import/); [Tom's Guide](https://www.tomsguide.com/ai/claude-just-made-two-of-its-best-features-free-heres-how-to-use-projects-and-artifacts)
- A points-travel template "interviews you once, remembers every card, point balance, and preference", but advises keeping passport numbers out of memory. **[Low-Med]** — [MavGPT](https://mavgpt.ai/resources/claude-travel-agent-guide)
- Sharing travel experiences with AI as a journal or companion is socially contested. In r/solotravel (Dec 2025) commenters pushed back ("Would much rather journal or share stories with friends"), and the post was removed under the sub's AI rule. **[Low: tangential]** — [r/solotravel](https://www.reddit.com/r/solotravel/comments/1ph4rpz/)
- **Saved social posts as a seed list:** a user saves Instagram reels into a folder as a shortlist, then has ChatGPT plan from it (7 vs 10 days; ranking spots; ring-road loop). The poster builds the connecting app (Recalo), so there is a conflict of interest. **[Low]** — [r/ChatGPT](https://www.reddit.com/r/ChatGPT/comments/1x4a46z/)

### Inferences
- A **"taste log"** (place, verdict, why, tags such as "too touristy" or "loved the vibe"), stored as a Project document and updated after each outing, is the logical extension of the decision-log and Reflect patterns. No source documented this exact structure with outcomes.
- Automatic memory captures broad preferences. An explicit log captures specifics (liked or disliked venues, "already visited"), which practitioners say stops repetition.

### Gaps
- No first-person evidence that Claude's memory (vs a pasted profile) improves travel recommendations.
- No found practitioner using voice notes after visits to update a preference document.

---

## Q8. Common failure modes and complaints

### Takeaway
The recurring failures are:
- outdated or closed venues and outright hallucinated places;
- confident errors on visas and rules;
- popularity and SEO bias;
- AI-generated "content farm" sources poisoning answers;
- unrealistic pacing and transit times;
- safety risk on mountain routes;
- commercial steering;
- high usage cost for agentic travel searches.

Major travel subreddits ban AI-generated content, including requests to validate an AI itinerary.

### Cited Findings
- **Communities ban AI.** r/travel Rule 6 (announcement Oct 6 2026, 342 points): "ChatGPT and AI usage is strictly against the rules". This includes "citing or referencing AI as a source" and "asking the community to proofread or validate your AI-generated itinerary". Penalties: a 28-day ban, then a permanent ban. r/solotravel also removes AI content ("ChatGPT or other AI-generated content is not allowed and will be removed as spam"). **[High: primary mod announcements]** — [r/travel Rule 6](https://www.reddit.com/r/travel/comments/1wzf8xx/); [r/solotravel removal notice](https://www.reddit.com/r/solotravel/comments/1u0ees4/)
- **AI-generated travel sites as poisoned sources** (Montenegro: wrong hike times, distances, landmarks). **[Med-High]** — [r/travel](https://www.reddit.com/r/travel/comments/1xauh1u/)
- **SEO-heavy and obvious answers; weak on niche.** **[Med]** — [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1rv4v3q/)
- **Popularity bias** shown academically (Czech GPT study; Collab-REC). **[High-Med]** — [Mendel University Press](https://doi.mendelu.cz/artkey/doi-990008-5700_THE-ALGORITHM-EFFECT-HOW-AI-DRIVEN-TRAVEL-PLANNING-FUELS-OVERTOURISM.php?l=en); [arXiv 2508.15030](https://arxiv.org/html/2508.15030v4)
- **Visa and rule errors:**
  - PSA: "ChatGPT is giving wrong answers about the 'rolling' part of the Schengen 90/180 rule" (r/travel, Feb 8 2026; title-only, body removed). **[Low-Med]** — [r/travel](https://www.reddit.com/r/travel/comments/1qzakov/)
  - The Puerto Rico ESTA case. **[Med]** — [RBC Style](https://style.rbc.ru/impressions/694d0e3f9a7947fe74c4831a)
- **Mountain and hiking safety:**
  - Three novice climbers were rescued from Mud Creek Canyon, Mount Shasta, on Aug 31 2026 after relying on AI to plan the climb (KRCR). Which AI is **conflicting**: an SF Chronicle headline on HN (Sep 2 2026) says ChatGPT, while Habr and a secondary Indian outlet say Gemini (food and water under-recommended). **[Med; tool identity unresolved]** — [KRCR](https://krcrtv.com/news/local/gallery/three-mount-shasta-climbers-rescued-after-relying-on-ai-to-plan-climb); [SF Chronicle via HN](https://www.sfchronicle.com/outdoors/article/shasta-climbers-rescued-chatgpt-22414629.php); [Habr](https://habr.com/ru/news/1091424/); [NewsKarnataka](https://newskarnataka.com/world/hikers-rescued-after-relying-on-ai-for-mount-shasta-trek/03092026/)
  - A 16-year-old was rescued by helicopter from Widowmaker Arete, Crown Mountain, BC (Oct 3 2026), reportedly after following a Claude-suggested route (Habr, Oct 7 2026). **Contradicted** by a r/travel commenter (36 points) who says he used AI for clothing, not the trail, and "came out to defend himself". Rescuers advise Gaia GPS, CalTopo or AllTrails instead. **[Med; causal claim disputed]** — [Habr](https://habr.com/ru/news/1091424/); [r/travel comment thread](https://www.reddit.com/r/travel/comments/1xauh1u/)
- **Overpacked, unrealistic pacing** (Atlanta 3h → 4.5h; 9 stops/day in Seoul). **[Med]** — [AOL](https://www.aol.com/travel-easy-tested-chatgpt-itineraries-090628315.html); [iVisitKorea](https://www.ivisitkorea.com/how-ai-travel-planners-can-ruin-your-trip/)
- **Seasonality and current state ignored** (cable cars closed for maintenance, a fuel station no longer operating, Amberd road snowed in). **[Med]** — [Rambler](https://sci.rambler.ru/soft/57165853-kak-ya-splaniroval-puteshestvie-cherez-ii-i-sovershil-oshibku/); [RBC Style](https://style.rbc.ru/impressions/694d0e3f9a7947fe74c4831a)
- **Commercial steering:** Gemini's travel booking links "give Alphabet a cut", and it gently steers trip conversations toward commercial offers. **[Med-Low: HN opinions]** — [Hacker News](https://news.ycombinator.com/item?id=49538512)
- **Flights: no magic.** On a popular "use ChatGPT to save hundreds on flights" post (r/ChatGPT, Oct 9 2026, 186 points), the top comment (103 points): "It's no better than Google flights… not as if AI is discovering 'secret flights'." **[Med]** — [r/ChatGPT](https://www.reddit.com/r/ChatGPT/comments/1x1s72a/)
- **Cost and limits of agentic search:** a GitHub issue reports that 3 travel-search prompts in ChatGPT Web "Work" mode consumed ~73% of a 5-hour usage window (Sep 14 2026). **[Med: single user report]** — [openai/codex#45510](https://github.com/openai/codex/issues/45510)
- **The big error-rate claims** (≈90% of AI itineraries have at least one error; ~4% of complex plans fully viable) come from a marketing agency audit and an older benchmark respectively. Treat them as indicative only. **[Low-Med]** — [Hotelemarketer](https://hotelemarketer.com/2026/05/23/how-i-plan-every-trip-with-ai-in-2026-the-killer-prompt-the-workflow-around-it-and-what-it-means-for-hotels/); [RusTourismNews](https://www.rustourismnews.com/90-of-ai-travel-itineraries-are-inaccurate/)
- **Model-specific claims:**
  - ChatGPT is "the most willing to hallucinate confidently" (Jain). **[Med-Low]** — [Hotelemarketer](https://hotelemarketer.com/2026/05/23/how-i-plan-every-trip-with-ai-in-2026-the-killer-prompt-the-workflow-around-it-and-what-it-means-for-hotels/)
  - "Gemini's live-data confidence can mask outdated underlying sources" (Jain). **[Med-Low]** — same source
  - One HN commenter called Gemini the only recent "SOTA" model that actively hallucinated details. **[Low]** — [HN search result](https://news.ycombinator.com/item?id=49538512)
- **Grok:** its real-time X search is pitched as its travel edge in how-to pieces, but no independent test was found. One forum user suspected it leaned on TripAdvisor and Yelp. **[Low]** — [Perplexity AI Magazine](https://perplexityaimagazine.com/ai-tools/how-to-plan-a-trip-with-grok/); [TexAgs](https://test1.texags.com/forums/54/topics/3601302)

### Inferences
- For mountain and trek regions (Nepal), AI route suggestions are a documented safety hazard. Practitioners and rescuers recommend dedicated trail apps and local operators for anything off-road.
- Because r/travel and r/solotravel ban AI-itinerary validation, "post your AI plan to Reddit for a check" is not a viable workflow there. Reading Reddit as a source is still common.

### Gaps
- No Claude-specific failure statistics.
- Verbosity complaints in travel contexts were not specifically documented in this search, though overpacking was.

---

## Q9. Russian-language community practices (Habr, vc.ru, Telegram, Pikabu)

### Takeaway
Russian-language material is mostly **press and corporate-blog guides plus a few first-person accounts**. Common themes:
- role + constraints prompts;
- per-country folders/chats;
- menu-photo prompts with currency conversion;
- a "two-source rule";
- AI only for the "skeleton" (каркас);
- strong distrust of AI for current-state info.

Access issues (VPN, aggregators like СигмаЧат or Telegram bots, GigaChat/Alisa as fallbacks) are a distinct theme. No substantive Pikabu or Telegram-channel practice was found.

### Cited Findings
- **RBC Style (Dec 29 2025)** collects practices from five practitioners: role prompts; a per-country folder with task-specific chats; menu photos with prices in ¥/$/₽; a local-persona check for Malaysia; a "half-day, love walks and food, hate 5-hour museum tours" brief; the two-source rule; never giving passport or card data; and asking taxi drivers. Errors reported: fake hotels, a pharmacy shown as a café, ignored seasonality, wrong visa advice. **[Med-High for Russian practice]** — [RBC Style](https://style.rbc.ru/impressions/694d0e3f9a7947fe74c4831a)
- **Rambler (Oct 4 2026):** first-person Caucasus road trip with ChatGPT. AI was good for the skeleton (city order, overnights, spare days) and suggested a better overnight base (Verkhny Fiagdon) that cut a 3-hour drive to about 1 hour. It failed on current state: cable cars closed for maintenance or already shut, a closed fuel station, and outdated fuel availability marks. Advice: check everything that can change right before departure. **[Med-High]** — [Rambler](https://sci.rambler.ru/soft/57165853-kak-ya-splaniroval-puteshestvie-cherez-ii-i-sovershil-oshibku/)
- **Habr (tsnis corporate blog):** AI approximates distances rather than measuring them; verify each leg with a navigator. **[Med]** — [Habr](https://habr.com/ru/companies/tsnis/articles/1094872/)
- **Habr news (Oct 7 2026):** BC teen / Claude route and Shasta / Gemini cases; rescuers recommend Gaia GPS, CalTopo and AllTrails. The Claude causal claim is disputed (see Q8). 20 comments; their text was not retrievable. **[Med]** — [Habr](https://habr.com/ru/news/1091424/)
- **vc.ru (May 18 2026, section "НейроВед"):**
  - Proposed task split: ChatGPT for routes, sights, packing and translating menus or signs; Gemini for nearby cafés, museum hours, comparing districts for safety and travel times; Claude for summarizing many hotel reviews, comparing insurance terms and reading visa or rental rules.
  - Advises treating AI answers as hypotheses.
  - Promotes VPN-free access via the СигмаЧат aggregator/Telegram bot.
  - 191 comments, text not retrieved.

  **[Low-Med: promotional]** — [vc.ru](https://vc.ru/ai/2934049-neyroseti-dlya-puteshestviy)
- **Московские новости:** the same prompt to ChatGPT, Grok and Claude gave similar answers. Grok was more accurate on facts; Claude built "оптимальный, не перегруженный маршрут" with travel time accounted for. Advice: be specific, add constraints, avoid multiple questions per prompt, give the list of places plus the hotel address and ask for minimal travel time. **[Low-Med: seen via search snippet; page 502]** — [mn.ru](https://www.mn.ru/smart/kak-planirovat-puteshestvie-s-pomoshhyu-ii-ot-vybora-lokaczii-do-marshruta-na-den)
- **78.ru (Jul 22 2026):** "Выдумал отель, запутал маршрут и наврал о визе: как ChatGPT «разводит» доверчивых туристов". **[Low: title-level only]** — [78.ru](https://78.ru/articles/2026-07-22/vidumal-otel-zaputal-marshrut-i-navral-o-vize-kak-chatgpt-razvodit-doverchivih-turistov)
- **Other Russian cases (via search summary):**
  - A Petrozavodsk resident was sent to a non-existent architectural monument.
  - A St Petersburg hotel list with two fake hotels.
  - In Japan, a tourist went to Mount Misen for sunset, but the ropeway had closed 2 hours earlier than ChatGPT claimed.
  - The mechanism is described as the model merging two real place names into a fake attraction.

  **[Low-Med]** — [Raffe](https://raffe.ru/neyroseti-absolyutno-bespoleznye-voprosy-puteshestviya-v-ukraine/); [VFokuse Mail](https://vfokuse.mail.ru/article/puteshestviya-s-pomoshyu-ii-pochemu-ne-stoit-doveryat-iskusstvennomu-razumu-68850333/)
- **Access from Russia:** Russian guides note that ChatGPT and Claude access can be unstable from Russia and mention GigaChat and Alisa as VPN-free options. **[Low-Med]** — [mn.ru via search](https://www.mn.ru/smart/kak-planirovat-puteshestvie-s-pomoshhyu-ii-ot-vybora-lokaczii-do-marshruta-na-den); [Habr (bothub)](https://habr.com/ru/companies/bothub/articles/1023070/)

### Inferences
- Russian-language practice matches the English-language consensus (skeleton by AI, verify current state). It adds a stronger emphasis on **menu or photo translation with ruble conversion** and on **local-persona prompts** for cultural norms. These are relevant to a Russian speaker in Nepal, India and Bali.

### Gaps
- No usable Telegram-channel or Pikabu practitioner content was surfaced by web search. Telegram is poorly indexed.
- Habr and vc.ru comment threads (where practitioner tips often live) could not be retrieved.
