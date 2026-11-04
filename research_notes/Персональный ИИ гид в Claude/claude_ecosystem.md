# Claude ecosystem capabilities for a personal, mobile-first AI travel guide (state as of 4 Nov 2026)

Research date: 2026-11-04. Most help-center pages fetched carry an "Updated this week/yesterday" label and no explicit date, so they reflect the current state, but individual launch dates come mainly from the official Release Notes page. Labels: **[Verified]** = primary Anthropic doc or page fetched today; **[Secondary]** = press/blog/forum; **[Observation]** = seen directly in the tool definitions of the Claude Code on the web session used for this research (a real Pro+/Max-class account, Nov 2026). This is first-hand evidence, but it is not a public doc and the account may differ from the user's.

---

## 0. Context: plans, regions and the "new Claude experience" (affects every answer below)

### Takeaway
As of Nov 2026 the individual plans are Free / Pro ($20/mo, or $17/mo billed annually) / Max ($100) / Ultra ($200). Since 16 Sep 2026, chat and Cowork are merging into one agentic "Claude" experience, rolling out to Pro/Max/Ultra first, with Free and Team "soon". **Russia is not a supported country, while Nepal, India and Indonesia are**, which matters for a Moscow-based user. Several of the most "proactive" features (Claude Duet, Health) are US-only.

### Cited Findings
- Free ($0): "Limited usage" per 5 hours and per week. Includes memory, up to 5 projects, web search, voice mode, Skills and connectors. **No Claude Code, no Research, no "Hand off and schedule tasks"**. Models are Sonnet and Haiku only (no Opus). — [Claude pricing](https://claude.com/pricing)
- Pro: $17/mo on annual billing ("$200 billed up front") or $20 monthly. Adds Claude Code, Research, "Hand off and schedule tasks", Claude in Chrome, and Opus/Sonnet/Haiku. "Fable" is "paid with usage credits". — [Claude pricing](https://claude.com/pricing)
- Max: $100/mo, "5x Pro usage", "Early access to advanced Claude features", priority access, and Fable "up to half your weekly limit". Ultra: $200/mo, "No 5-hour limit" for verified accounts, "10x Pro usage every week". — [Claude pricing](https://claude.com/pricing)
- Chat and Cowork merger (announced 16 Sep 2026): "rolling out on Pro, Max, and Ultra plans over the next few weeks"; Team and Free follow "soon". It applies on web, desktop and mobile, and "There's nothing to turn on." Existing chats, projects, artifacts, connectors and skills carry over. Users can schedule recurring work ("Schedule it for every Monday…"). By default Claude asks before acting, and an optional mode lets it keep working and check in only when needed. — [Anthropic: Cowork and chat are now one Claude](https://claude.com/resources/articles/cowork-is-now-claude)
- Known gaps at the merger: no adding from GitHub, no conversation branching, no Dispatch for new users, and incognito chats open in the previous experience. One user reported on 18 Sep that the merge hadn't reached their account. — [9to5Mac](https://9to5mac.com/2026/09/16/anthropic-merging-claude-cowork-with-chat/) and search summary of secondary coverage [Secondary]
- Release-notes timeline: Cowork reached web and mobile on 7 Jul 2026 ("starting with Max"). A "persistent Cowork agent thread" from mobile arrived 17 Mar 2026 (research preview, Pro/Max). Scheduled tasks in Cowork arrived 25 Feb 2026. "Interactive apps" (interactive connector UIs) arrived on iOS/Android on 25 Mar 2026. — [Claude Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- Supported countries: "Any country or region not listed is unsupported." Russia is not listed. Nepal, India and Indonesia are listed. The page shows the policy effective **Nov 12, 2026**. — [Anthropic supported countries](https://www.anthropic.com/supported-countries)
- Current model family named in Anthropic docs: Claude Fable 5.1, Mythos 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5 (plus older 5 / 4.x). — [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)

### Inferences
- The user's plan isn't stated. Most of the design hinges on whether it is Free or Pro+. On **Free**: no Claude Code, routines, Research, artifact persistent storage or artifact connectors, and only one custom connector. On **Pro and above** everything below is available except Duet and Health, which are US-only.
- Russia's absence from the supported list means account and billing problems are possible while physically in Moscow (e.g. Russian payment cards, IP-based checks). The tools themselves work from supported countries such as Nepal and India. Flag this for the user without speculating about workarounds.
- Because the merged "one Claude" UI is still rolling out, menus and toggle names (e.g. the "Web search" toggle, the "+" menu) may differ between the user's phone and the docs.

### Gaps
- I couldn't confirm whether the user's account already has the merged experience, or what exactly differs on mobile in it.
- Exact message/usage numbers per plan are not published (multipliers only).

---

## 1. Projects in the Claude app (instructions, knowledge files, RAG, project memory, mobile)

### Takeaway
Classic Projects (custom instructions + knowledge files + project-scoped memory) exist on all plans (Free: max 5 projects). RAG auto-expands knowledge capacity up to about 10x, on paid plans only. Claude **cannot be documented to edit project knowledge files** in classic Projects. A **new beta "Projects"** built on Claude Code cloud threads has a Library that holds "files Claude produces", but it is limited to select Pro/Max/Ultra users and accessed via claude.ai/code and the desktop Code tab. Mobile creation and editing of Projects is not documented.

### Cited Findings
- "Free users can create a maximum of five projects." Each project has its own custom instructions. "When your project knowledge approaches context limits, Claude seamlessly enables RAG mode", expanding capacity "by up to 10x while maintaining response quality". RAG is "only available to users with paid Claude plans." No fixed size limit is stated. — [What are projects](https://support.claude.com/en/articles/9517075-what-are-projects)
- Project memory: "Each project has its own memory. In a project, Claude uses that memory plus your non-project memory, but not other projects' memory." To isolate a project, turn off "Use account memory" on its page. — [Memory & chat search help](https://support.claude.com/en/articles/11817273-using-claude-s-chat-search-and-memory-to-build-on-previous-context)
- Chat search inside projects: searches cover each project's conversations separately, and "Claude can't search across projects." — [Memory & chat search help](https://support.claude.com/en/articles/11817273-using-claude-s-chat-search-and-memory-to-build-on-previous-context)
- New Projects (beta): a project becomes one conversation, and "Claude breaks the work into parallel threads that run in the cloud". "The project's Library collects the files you add and the files Claude produces". Each thread starts with the project's "files, repositories, instructions, and memory". Access is for select Pro/Max/Ultra Claude Code users (others can join a waitlist), via claude.ai/code and the desktop Code tab, with chat, Cowork, Team and Enterprise to follow. Some existing projects are being migrated ("we'll email you before we move your projects"), and instructions, files, chat history and scheduled tasks carry over. Running several threads at once consumes usage faster. — [What are projects](https://support.claude.com/en/articles/9517075-what-are-projects)
- An undated report says the iOS app gained Projects support (pick a project, browse its knowledge, start a chat). — [TestingCatalog](https://www.testingcatalog.com/claude-app-got-projects-support-on-ios/) [Secondary]
- A 2026 third-party guide says Projects creation and the Artifacts library are "centered on the web". — [wikidocs guide (Korean)](https://wikidocs.net/368496) [Secondary]

### Inferences
- For a travel guide, a classic Project is the cheapest way to pin a stable "guide persona + rules" (instructions) and reference docs (taste profile, places log exported as Markdown/CSV) that load for every chat in it, including from the phone once the project exists.
- It is **read-mostly**. To update the log, the user (or Claude via a connector) must change the source somewhere else and re-upload the file. Project memory partially compensates, because Claude can remember new likes inside that project automatically or on request.
- Safest assumption: create and edit the Project on web/desktop, then use it from mobile.

### Gaps
- No official statement on whether Projects can be created or edited, or knowledge files uploaded, in the iOS/Android apps as of Nov 2026.
- No official per-file or total size limit for project knowledge was found.
- Whether Claude in a classic Project can write or overwrite knowledge files: not documented. Historically it could not; treat it as unsupported.

---

## 2. Memory (automatic memory, chat search, project memory, explicit edits, import/export, incognito, mobile, plans)

### Takeaway
Memory is now a set of **individual, categorized "topics" saved during chats** (since 10 Jul 2026). It is on by default for Free/Pro/Max/Ultra on web, desktop and mobile. **You can tell Claude in chat to remember, change or forget something**, and you can edit or delete topics in Settings. It is project-scoped, with experimental import/export. "Search past chats" is officially paid-only, which conflicts with a release note.

### Cited Findings
- "Memory is on by default for Free, Pro, Max, and Ultra plans" on web, Desktop and mobile (the latest app version is required). "Claude saves memory as a set of individual topics as you chat, rather than summarizing conversations after they end." Claude saves on its own, and you can ask it to remember something directly. — [Memory & chat search help](https://support.claude.com/en/articles/11817273-using-claude-s-chat-search-and-memory-to-build-on-previous-context)
- Explicit control: you can tell Claude in chat what to remember, change or forget, and the change applies to your next conversation. Topics can be reviewed, edited or deleted in Settings. — [Memory & chat search help](https://support.claude.com/en/articles/11817273-using-claude-s-chat-search-and-memory-to-build-on-previous-context)
- Categories described: role and professional context, people and places in your work, communication preferences, technical and coding preferences, ongoing project details. — [Memory & chat search help](https://support.claude.com/en/articles/11817273-using-claude-s-chat-search-and-memory-to-build-on-previous-context)
- Sensitive topics (health, politics, religion…) are not stored unless "Include sensitive topics in memory" is enabled. Some data is never saved (government IDs, financial account numbers, immigration status, criminal history). — [Memory & chat search help](https://support.claude.com/en/articles/11817273-using-claude-s-chat-search-and-memory-to-build-on-previous-context)
- Per-chat opt-out: turn memory off for a new chat from the "+" menu before the first message. Incognito (ghost icon, all plans) is not saved to memory or history. Deleting a chat doesn't delete the memory entries derived from it. "Reset memory" permanently deletes everything, including project memory. Import from other assistants and export are "experimental and still in active development". — [Memory & chat search help](https://support.claude.com/en/articles/11817273-using-claude-s-chat-search-and-memory-to-build-on-previous-context)
- Chat search ("search and reference past chats") uses RAG, appears as a tool call, and is on by default. The help page lists it for "paid plans (Pro, Max, Ultra, Team, and Enterprise)" — [Memory & chat search help](https://support.claude.com/en/articles/11817273-using-claude-s-chat-search-and-memory-to-build-on-previous-context). This **conflicts with** the release-notes entry for 2 Mar 2026, "chat-history memory for all users, including Free" — [Release notes](https://support.claude.com/en/articles/12138966-release-notes). The release-notes wording came via a summarizer, so treat Free-plan chat search as uncertain.
- Timeline: memory and incognito for Free/Pro/Max/Team on 11 Sep 2025; Max first, then Pro, from 23 Oct 2025; individual categorized entries replaced the daily summary on 10 Jul 2026; memory shared across chat and cloud Cowork, with "Topics" under Settings > Memory, on 25 Aug 2026. — [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- Memory is shared with cloud Cowork but not with locally run Cowork sessions. — [Memory & chat search help](https://support.claude.com/en/articles/11817273-using-claude-s-chat-search-and-memory-to-build-on-previous-context)
- Claude Duet "carries over your memory, skills, and connected apps from your Claude account". — [Anthropic: Claude Duet](https://claude.com/resources/articles/claude-duet)

### Inferences
- Memory is the **lowest-friction** read/write store from the phone and by voice ("запомни, мне понравился этот момо-бар в Тамеле"), and it works on Free. It suits a compact taste profile (cuisine, budget, walking tolerance, noise and crowd aversion, "already visited" highlights).
- It is a poor structured database. Entries are free-text topics that Claude decides how to phrase. There is no guaranteed full listing to the model, no fields such as rating or date, it can't be queried as a table, and export is experimental. A log of hundreds of places belongs in an external store, with memory holding the summary and a pointer.
- Project-scoped memory lets a "Travel guide" project accumulate travel-specific memories without polluting general memory, while still seeing general memory (unless isolated).

### Gaps
- No documented capacity limit on the number or size of memory topics.
- Whether Claude can list all of its memory topics verbatim on request: not documented.

---

## 3. Skills (Agent Skills) on claude.ai and mobile; triggering, token cost, Claude Code differences, plugins

### Takeaway
Custom Skills (ZIP with SKILL.md) can be uploaded on claude.ai (Customize > Skills) on **all plans including Free**. They require the code-execution / "Create and edit files" setting and are **auto-triggered by their description**. Skills enabled on claude.ai sync one-way into Claude Code (v2.1.273+). Use of custom skills **in the mobile app is not documented**, and there is a 2026 report of skills not registering in Claude Code on iOS.

### Cited Findings
- "Skills are available for users on Free, Pro, Max, Ultra, Team, and Enterprise plans." Use them via Customize > Skills. The feature "requires code execution to be enabled" ("Code execution and file creation", called "Create and edit files" in the new Settings). — [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- Triggering: "You don't need to explicitly invoke them—Claude determines when each skill is needed based on your request." If a skill isn't used, make its description clearly say when to use it. In the M365 add-ins you can type `/` to select a skill. — [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- Upload: ZIP of the skill folder via "+" > "+ Create skill" > "Upload a skill". Failures include oversized ZIP, folder name not matching the skill name, a missing SKILL.md, and invalid characters. No numeric size limit is given. — [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- Sync to Claude Code: skills enabled in claude.ai load in Claude Code with the same account ("needs Claude Code v2.1.273 or later"). "The sync is one-way. It reads from your Claude account and never changes anything in it." They are checked about every 10 minutes. — [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- Claude Code 2.1.317 (early Nov 2026) fixed "skills synced from claude.ai being lost or re-downloaded"; 2.1.316 made cloud scheduled tasks load plugins enabled on the claude.ai account. — [Releasebot Anthropic updates](https://releasebot.io/updates/anthropic) [Secondary aggregator of official changelog]
- Org-wide skill management, a partner skills directory and the "open Agent Skills standard" arrived 18 Dec 2025. A Customize section grouping skills, plugins and connectors arrived 25 Feb 2026. A plugin developer portal ("Build plugins for Claude") opened 25 Sep 2026. — [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- Claude Code on iOS (April 2026 issue): project-level skills in `.claude/skills/` were readable but not registered as slash commands or resolvable by the Skill tool. The workaround is a rule telling the agent to Read SKILL.md and execute it inline, at extra token cost. — [GitHub issue #48696](https://github.com/anthropics/claude-code/issues/48696) [Secondary, single user report, may be fixed]
- Claude Duet reuses account skills. — [Claude Duet](https://claude.com/resources/articles/claude-duet)
- Prompting guidance relevant to skill descriptions: newer models "might now overtrigger"; replace "CRITICAL: You MUST use this tool when..." with "Use this tool when...". — [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)

### Inferences
- A "travel-guide" Skill is a portable bundle: the guide methodology (scenario playbooks for "here and now", "day walk", "multi-day plan", "new in a familiar city"), output templates, region notes (Kathmandu, Bali, India), and possibly scripts (e.g. a route-time estimator). It is used automatically in any chat whose request matches the description, without having to be inside a Project.
- Compared with Project instructions, a Skill loads only when relevant and can carry reference files and code. However, it is **static** (Claude can't edit an uploaded skill from chat) and it needs the code-execution setting on.
- The same skill can be committed to a GitHub repo for Claude Code (`.claude/skills/`) and uploaded to claude.ai. The account-level upload is the one that also reaches Claude Code (via sync), Duet and, presumably, mobile chat.

### Gaps
- No official statement on whether custom skills trigger in the iOS/Android chat apps. It is plausible, since mobile chat uses the same account-side code execution, but unverified.
- No official token-cost figure for skills was found in the fetched help page. Anthropic's 2025 engineering material described "progressive disclosure" (only name and description preloaded, the body loaded on trigger), but I did not re-verify it for Nov 2026.

---

## 4. Connectors and device integrations on mobile (Drive, Gmail, Calendar, Notion, GitHub, travel apps; location, maps, reminders, health, camera)

### Takeaway
On iOS and Android Claude has a **native location tool** that suggests nearby places and **renders them on an interactive in-chat map**, with tap-through to Apple Maps or Google Maps. It is available on all individual plans (not Team/Enterprise). Calendar works on both platforms, reminders on iOS only, alarms and timers on Android. Health is US-only. Connectors work on mobile (mobile in beta), and since 25 Mar 2026 interactive connector apps render in the mobile app. The April 2026 "everyday" connectors include **Tripadvisor, Booking.com, Viator, AllTrails, Resy, Uber**. The Google Drive connector can **create and read** files but its update tool is metadata-only. In-place Google Docs editing comes from the separate Google Docs/Sheets/Slides connectors (beta, 6 Oct 2026).

### Cited Findings
- iOS integrations are "supported on all Claude plans". Location: Claude uses your location for nearby suggestions when relevant and asks permission first. "Team and Enterprise members can't use the location tool currently." Maps: Claude "can show suggested places on an interactive map". "Select a location to open it in Apple Maps for navigation." Maps display needs no separate permission. — [Use Claude with iOS apps](https://support.claude.com/en/articles/11869619-use-claude-with-ios-apps)
- Also on iOS: Calendar (check availability, create events; "Ability to edit events depends on your ownership of the event"), Reminders (items within existing lists only), Messages and Mail (drafts only; "Claude does not read existing messages or emails"), and no Contacts access. Health (beta, Pro/Max/Ultra, US only) is read-only. Photos/camera are not covered there. — [Use Claude with iOS apps](https://support.claude.com/en/articles/11869619-use-claude-with-ios-apps)
- Android: location-based suggestions, an interactive map, and "Select a location to open it in Google Maps for navigation". Calendar can create, edit and delete events. Clock alarms and timers are available on all plans. Health Connect requires Pro/Max/Ultra, the US, and Android 14+. Reminders are not available. The location tool isn't available to Team/Enterprise. — [Use Claude with Android apps](https://support.claude.com/en/articles/11869629-use-claude-with-android-apps)
- These location, maps and calendar features launched 3 Sep 2025 on iOS and Android. — [Release notes](https://support.claude.com/en/articles/12138966-release-notes); [AlternativeTo news](https://alternativeto.net/news/2025/9/claude-for-mobile-launches-location-and-calendar-access-on-ios-and-android) [Secondary]
- An independent review notes Claude's app "renders a map with marks and widgets, redirecting to native maps application for routing." — [Using Maps in AI Assistants (Peschinskiy)](https://peschinskiy.github.io/using-maps-in-ai-assistants) [Secondary]
- Everyday connectors (23 Apr 2026): AllTrails, Audible, Booking.com, Instacart, Credit Karma, TurboTax, Resy, Spotify, StubHub, Taskrabbit, Thumbtack, **Tripadvisor**, Uber, Uber Eats, **Viator**. "Connectors are available on all plans, with mobile in beta." Install "with a few taps on mobile". "Claude now suggests the right app for what you're doing." "Before it books or purchases something on your behalf, it's designed to check with you first." AllTrails "will surface trails nearby that match your preferences". — [Anthropic: New connectors for everyday life](https://claude.com/resources/articles/connectors-for-everyday-life)
- Directory size: about 369 integrations as of 19 Jun 2026 per one count; other coverage says "200+" in April. — [DirJournal](https://www.dirjournal.com/blogs/claude-connectors-list) [Secondary, uncertain]. A MediaPost headline/snippet claimed Claude uses Google Maps/Places data for local queries; the page returned 403 and this could not be verified. — [MediaPost](https://mediapost.com/publications/article/414963/anthropic-takes-on-local-search-challenges-google.html) [Unverified]
- Interactive apps (fully interactive connector UIs) in the iOS and Android apps arrived 25 Mar 2026. — [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- Google Docs/Sheets/Slides connectors (beta, 6 Oct 2026) "create and edit Google files directly from Claude". The default "Ask before edits" mode shows approval cards, and an "Accept all edits" mode exists. Team/Enterprise owners must enable them. The Workspace add-on is in "public beta on all paid Claude plans". Mobile isn't mentioned. — [Anthropic blog: Claude now works with Google Docs, Sheets, and Slides](https://claude.com/blog/claude-now-works-in-google-docs-sheets-and-slides)
- A mid-2026 issue reported that the Drive integration supports read, create, copy and search, but has no tool to edit an existing Doc's content. — [claudeissues #72576](https://claudeissues.com/issue/72576-google-drive-mcp-integration-missing-write-edit-support-for-existing-docs) [Secondary]
- Notion connector: reported able to search, create and edit pages and update properties, with Notion search limited to about 30 requests/min. GitHub connector is reported as "read and write" (this may describe GitHub's MCP generally). — [tl;dv best Claude connectors](https://tldv.io/blog/best-claude-connectors/) [Secondary]
- Voice mode can use connected tools (Gmail, Google Calendar, Google Docs and Slack are named). — [Using voice mode](https://support.claude.com/en/articles/11101966-using-voice-mode)

### Inferences
- **Observation:** the Google Drive connector in this session exposes `create_file` (with `textContent`, auto-converted to a Google Doc), `read_file_content`, `download_file_content`, `search_files`, `copy_file`, `share_file` and `trash_file`. Its `update_file` changes **only metadata** (title, description, parent folder, starred, lock). So via Drive alone Claude can append to a log only by **creating new files** (e.g. one dated file per entry or per trip, or copy-then-replace). True in-place edits of a single "places log" Doc need the Google Docs connector (beta), whose individual-plan and mobile availability is unconfirmed.
- **Observation:** the GitHub MCP in this Claude Code session exposes `create_or_update_file` and `push_files`. In Claude Code (including from the phone's Code tab), Claude can commit profile and log files directly. Whether the claude.ai **chat** GitHub integration can write is unverified; historically it was a read-only knowledge sync.
- For "here and now", the native location tool + interactive map is the single most valuable mobile feature. It's free on all individual plans, needs no setup, and hands off to Google Maps for navigation, which matters in Kathmandu and Bali where Apple Maps coverage is weaker. Combine it with web search for freshness and the taste profile from memory or a Project.
- Tripadvisor, Viator and AllTrails connectors may be useful for Asia (treks around Kathmandu, Bali activities). Booking and purchase actions require confirmation.

### Gaps
- Whether the in-chat location tool works when the request comes through voice mode: not documented.
- Whether location and maps are available identically in Nepal, India and Indonesia: no region restriction is stated (only Health is US-only), but this is unverified.
- Camera/photo input (e.g. photographing a menu or sign) is not described in the integrations pages. Image upload in chat is a long-standing feature, but it was not re-verified here.
- Exact capability (read vs write) of the Notion and GitHub connectors in claude.ai chat as of Nov 2026: only secondary sources.
- Whether the Google Docs editing connector is available on Free/Pro individual plans and on mobile.

---

## 5. Web search, web fetch, Research mode (mobile; limits; Reddit)

### Takeaway
Web search (with citations and Bing image results) and web fetch of user-supplied URLs are available. On Free plans they count against the 5-hour limit, and long pages are costly. Location for search can be inferred from IP. In the new experience there is no toggle: "Claude searches the web when it helps." **Research mode is Pro+ only** (not Free). Reddit fetchability is undocumented.

### Cited Findings
- Enabling: "+" > "Web search" (a checkmark shows it's on). "The new Claude experience has no toggle: 'Claude searches the web when it helps.'" With web search on, Claude can "retrieve content from specific URLs you provide and analyze the full page." On Free accounts a long article can use a large share of the usage limit. "Every response includes citations." Image results come via Bing. Claude may infer your location from your IP address for localized results. — [Enabling and using web search](https://support.claude.com/en/articles/10684626-enabling-and-using-web-search)
- Research is listed for Pro and above and not for Free. Web search is on all plans. — [Claude pricing](https://claude.com/pricing)
- Voice mode can use web search. — [Using voice mode](https://support.claude.com/en/articles/11101966-using-voice-mode)

### Inferences
- Since search location comes from IP, a VPN (common for users with Russian accounts) skews "near me" results. The user should state the city or neighbourhood explicitly, or rely on the device location tool.
- **Observation:** in this Claude Code cloud session, WebFetch reached most sites (support.claude.com, claude.com, code.claude.com, platform.claude.com, letsdatascience.com, anthropic.com), but mediapost.com and alternativeto.net returned 403. Site-level blocking of Anthropic fetchers does happen, so Reddit threads may or may not load. Recommend that the guide treat Reddit as "search snippets + fetch if possible" and fall back to other sources.

### Gaps
- No official statement on Reddit fetchability, robots.txt handling or blocked domains.
- Research mode's per-plan quotas and duration for Nov 2026 were not found.
- Whether web search behaves identically in the mobile app vs web (assumed yes, not documented).

---

## 6. Voice mode (search, tools, connectors, projects, memory; Russian; hands-free)

### Takeaway
Voice mode (beta, all plans; iOS, Android, desktop, web, "built to work best from your phone") offers **hands-free** (pause detection) and **push-to-talk** modes. It can use **web search and connected tools**, uses the same models as text (except Fable), and saves transcripts to history. Non-English languages are in beta. **Russian support in two-way voice mode is contradictory across sources**, while dictation in the mobile apps reportedly supports Russian (beta).

### Cited Findings
- "a beta feature available to all plans (Free, Pro, Max, Ultra, Team, and Enterprise)". It is on iOS, Android, Desktop and web, and "built to work best from your phone". Hands-free listens continuously and responds to pauses; push-to-talk is for noisy settings. Claude can use web search and connected tools (Gmail, Google Calendar, Google Docs and Slack named), and "Not every result can be shown on screen in voice mode." Free allows one connected tool in voice; paid plans allow more. "Voice conversations count toward your regular usage limits." Voice uses the same models as chat, and "Claude Fable is not available in voice mode." Preset voices; pace adjustable on mobile. "Textual transcripts of your audio conversations are saved in your chat history". Dictation (speech to text) differs from voice mode. In Cowork and Claude Code, only dictation is available. "Support for languages other than English is in beta"; the language is set in Settings > Capabilities/General. — [Using voice mode](https://support.claude.com/en/articles/11101966-using-voice-mode)
- Russian is listed among supported voice-mode languages — [Engadget how-to, Jul 2026](https://www.engadget.com/2231293/how-to-use- -voice-mode/) [Secondary]. **Contradicted by** a guide saying Anthropic's July 2026 list omits Russian (and Chinese, Ukrainian, Turkish, Polish, Dutch), while dictation supports Russian in beta — [FelloAI](https://felloai.com/es/claude-voice-mode/) [Secondary]. A May 2026 report said Russian was among 18 languages in beta testing — [AndroidHeadlines, May 2026](https://www.androidheadlines.com/2026/05/anthropic-claude-voice-mode-multilingual-update-push-to-talk.html) [Secondary]. Dictation help page: [Using dictation on Claude mobile](https://support.anthropic.com/en/articles/10065434-using-dictation-on-claude-mobile).
- Claude Code's speech-to-text added Russian (20 languages) in March 2026. That is Claude Code, not app voice mode. — [blog post, 2026-03-09](https://jasonmoon-dev.pages.dev/blog/2026-03-09-claude-code-voice-20-languages) [Secondary]

### Inferences
- For walking: hands-free voice mode with web search and connectors is usable for quick "what's nearby / is it open / how far" loops. The user should verify Russian in Settings > voice language on their phone. If Russian voice output is missing, **dictation in Russian + text reply** (or English voice) is the fallback.
- Whether voice mode sees Project instructions and memory isn't documented. Starting voice from inside the travel Project chat is the safest bet (inference).

### Gaps
- Voice mode + projects/memory/skills/location-tool interplay: not documented.
- Background or locked-screen operation: not documented in the fetched page.
- Definitive current Russian voice-mode support: unresolved (check in-app).

---

## 7. Artifacts on mobile: interactive maps, persistent storage, AI-powered artifacts, sharing ("personal app")

### Takeaway
Chat artifacts exist on all plans, and since 16 Sep 2026 Docs/Slides/Design templates can be created in any conversation, with an Artifacts tab. Artifacts can be viewed and edited on mobile, but sharing settings need web or desktop. **Persistent storage** (20 MB/artifact, text only, personal or shared), **AI-powered artifacts** (calling Claude on the viewer's own plan) and **artifact connectors (MCP)** are documented for Pro+ on **web and desktop**, with mobile not stated. Claude Code artifacts (claude.ai/code/artifact) add a richer runtime: a `db` that Claude can read and write later, `sample` (ask Claude), and `mcp` connector calls. Their strict CSP **blocks external images and fetches**, so standard Leaflet + OpenStreetMap tiles won't load there.

### Cited Findings
- Artifacts are on Free, Pro, Max, Ultra, Team and Enterprise, and require "Cloud code execution and file creation". On mobile you can request a design, deck or doc in any chat, view it in the Artifacts tab and edit it. "To change sharing settings, use Claude on the web or Claude Desktop." — [What are artifacts](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)
- Persistent storage: Pro/Max/Ultra/Team/Enterprise, on web and Claude Desktop. 20 MB per artifact, text only. Personal (private) or shared storage, with a confirmation on first use. "New artifacts don't need to be published to store data". Unpublishing a legacy artifact deletes its data. — [What are artifacts](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)
- AI-powered artifacts: they call Claude directly; "usage counts against each person's own plan limits"; no API keys; permission is asked the first time. — [What are artifacts](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)
- MCP in artifacts: Pro+ on web and desktop. They can use connected apps and custom connectors. "Connector tools that need approval for each action aren't available to artifacts." — [What are artifacts](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)
- "Legacy artifacts" are those made in chat before 16 Sep 2026. Artifacts became available on all plans, including Free, on 16 Sep 2026. Inline interactive charts and diagrams in chat arrived 12 Mar 2026. — [What are artifacts](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them); [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- Artifacts first came to the iOS/Android apps on 31 Jul 2025. — [Anthropic blog: build artifacts](https://claude.com/blog/build-artifacts) (via search summary)
- Community reports (May 2026) say storage-backed artifacts are unreliable in the mobile app. Workarounds are mobile Safari logged into claude.ai, or a published link saved to the iOS Home Screen; some users report storage resets. — [Reddit snapshot](https://reddit.sentinel-team.org/posts/1t9t4z5/snapshots/2026-05-16T01%3A22%3A27.604243Z) [Secondary, anecdotal]
- Claude Code artifacts: Pro/Max/Ultra/Team/Enterprise. A live page at claude.ai/code/artifact, private until shared, with public link sharing on individual plans. CSP: the page may load Google Fonts and scripts from cdnjs, unpkg, Tailwind, jQuery and jsDelivr `/npm/`. "The CSP blocks every external image and all other external scripts, stylesheets, and fonts, and lets fetch, XHR, and WebSocket calls reach only the page's own origin and the Google Fonts hosts." Images must be data URIs. Max 16 MiB. Connector calls run through claude.ai using the **viewer's** account, need Claude Code v2.1.209+, and are cached in the viewer's browser. — [Claude Code docs: artifacts](https://code.claude.com/docs/en/artifacts)
- OpenStreetMap tile servers block requests without a Referer, e.g. from local or sandboxed pages. — [libgeodesk issue #37](https://github.com/clarisma/libgeodesk/issues/37); [OSM community thread](https://community.openstreetmap.org/t/general-block-app-is-not-following-the-tile-usage-policy-of-openstreetmap-volunteer-run-servers/147545) [Secondary]

### Inferences
- **Observation:** this account's Claude Code artifact runtime (contract 0.2.96) offers the capabilities `artifact` (the page republishes itself as the record), `assets`, `comments`, `db` (rows Claude can read and write later with the ArtifactData tool, per-user private paths), `downloads`, `files`, `mcp` (viewer's connectors), `room`, `sample` (ask Claude from the page, with tool calls) and `user`. **No geolocation, camera or microphone capability is in this account's roster**, though the platform's tool docs mention such capabilities may exist for some users. So a Claude Code-built "places log" artifact can be a real mini-app: a list/table backed by `db`, an "ask the guide" box via `sample`, and live data via connectors. It **can't** get the phone's GPS and **can't** load raster map tiles from OSM or Google. Maps must be drawn as inline SVG or canvas from stored lat/lon, or replaced by "open in Google Maps" deep links (links are navigation, not fetches; behaviour inside the viewer is unverified).
- Leaflet's JS can load from cdnjs/unpkg, but tile images are external images and are blocked under the documented Claude Code CSP. Chat-artifact CSP was not documented in the fetched pages, but historically also restricted external requests. Assume tiles fail unless tested.
- As a "lightweight personal app" on the phone, an artifact is best for **viewing and curating** (trip itinerary, places log with filters, a checklist). The in-chat native map from the location tool is better for "here and now".

### Gaps
- Official status of persistent storage, AI-powered calls and MCP inside artifacts **in the iOS/Android apps**: not documented.
- The exact CSP for claude.ai chat artifacts (vs Claude Code artifacts): not found.
- Whether a regular claude.ai chat (not Claude Code) can read an artifact's `db` rows: not documented. The ArtifactData tool is a Claude Code tool.

---

## 8. Custom connectors (remote MCP): plans, mobile, auth; free hosting

### Takeaway
Custom remote-MCP connectors are available on **all plans; Free is limited to one**. They are added on the web (Customize > Connectors > "+ Add" > "Add custom connector") and work across all clients, including the mobile apps. Calls originate from Anthropic's cloud, so the server must be publicly reachable. Auth options are OAuth (Claude's identity, dynamic registration, or your own client), **"No sign in"**, or **fixed request headers (API key/bearer)**. A free Cloudflare Worker (about 100k requests/day) is a viable host.

### Cited Findings
- Custom connectors on Free, Pro, Max, Ultra, Team and Enterprise. "Free users are limited to one custom connector." — [Custom connectors help](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp)
- Setup is on the web (Customize > Connectors > "+ Add" > "Add custom connector": name + server URL, review detected auth). Enable per conversation via "+" > Connectors. To edit a connector you must remove and re-add it. — [Custom connectors help](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp)
- Network requirements apply "across every Claude client, including claude.ai, Claude Desktop, Cowork, and the mobile apps". "Claude connects to your remote MCP server from Anthropic's cloud infrastructure, rather than from your local device." The server "must be reachable over the public internet from Anthropic's IP ranges." Local `claude_desktop_config.json` servers aren't available in Cowork or claude.ai. — [Custom connectors help](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp)
- Auth: "Sign in now", "Sign in when needed" or "No sign in". OAuth client: Claude's published identity, automatic registration, or "Use your own OAuth client". Request headers can carry API keys, bearer tokens or other fixed credentials. — [Custom connectors help](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp)
- Cloud scheduled tasks can use claude.ai connectors (traffic routed through Anthropic, so no allowlist changes are needed). — [Claude Code docs: scheduled tasks](https://code.claude.com/docs/en/routines)
- Cloudflare Workers Free: 100,000 requests/day, plus CPU-time and script-size caps (the search snippet said "30ms CPU time, and 1MB script size", which differs from figures I remember from Cloudflare's own docs, so verify before relying on them) — [eastondev blog, May 2026](https://eastondev.com/blog/en/posts/dev/20260526-cloudflare-free-limits/) [Secondary]. Officially, free-plan Workers are capped at 50 external subrequests and 1,000 subrequests to Cloudflare services per invocation — [Cloudflare changelog 2026-02-11](https://developers.cloudflare.com/changelog/post/2026-02-11-subrequests-limit/). Workers Paid is about $5/mo — [costbench](https://costbench.com/software/cloud-infrastructure/cloudflare-pages-workers/free-plan/) [Secondary]

### Inferences
- A personal "travel memory" MCP server on a free Cloudflare Worker (with free KV/D1 storage) is the most robust **structured** read/write store usable from mobile chat, voice mode (as the one connected tool on Free), scheduled tasks and artifacts. Example tools: `get_profile`, `log_place`, `search_places(city, tag)`, `mark_visited`, `wishlist`. The Free plan's single custom-connector slot would be consumed by it.
- "No sign in" is the simplest but exposes data to anyone who guesses the URL. A secret path or a fixed bearer header is a cheap middle ground. OAuth is the most secure but more work.
- The cost is build and maintenance effort (coding, deploy, schema), which can be done once in Claude Code. Free Cloudflare tier limits are far above one person's usage.

### Gaps
- Whether custom connectors can be **added** from the mobile app (only web steps are documented).
- Exact current Cloudflare free-tier CPU and storage limits (only secondary figures were found, and they conflict).

---

## 9. Claude Code on web/mobile, scheduled tasks (routines), Claude in Chrome, Cowork, Duet: proactive suggestions

### Takeaway
Claude Code cloud sessions (Pro+) can be started and steered from the **Code tab of the Claude mobile app**. They need a GitHub repo, which makes a "travel-guide repo" (profile.md, places.csv, skills, scripts) fully editable from the phone. **Cloud scheduled tasks** (formerly "routines"; Pro+, research preview) run on Anthropic's cloud at most hourly, with connectors, and can deliver a **morning "what to do today" digest**. In the merged chat experience, Pro+ users can also "hand off and schedule tasks" directly in chat. **Claude Duet** (proactive agent with a morning brief) is US-only by waitlist, so it is likely unavailable to this user. Claude in Chrome is a desktop-browser feature.

### Cited Findings
- Cloud sessions are available on Pro, Max, Ultra and Team (and eligible Enterprise seats). They can be started from the browser (claude.ai/code), **"Mobile: the Code tab in the Claude app"**, desktop, terminal and scheduled tasks. They keep running after you close the laptop, and you can steer from any device. They count toward plan usage, with no separate VM charge. GitHub is needed for clone and push. — [Claude Code docs: cloud sessions](https://code.claude.com/docs/en/claude-code-on-the-web)
- The Default cloud environment uses "Trusted" network access, a default allowlist of package registries, cloud APIs and dev domains. Hosts outside it fail with 403 `host_not_allowed`. Connector traffic is routed through Anthropic and bypasses the allowlist. — [Claude Code docs: scheduled tasks](https://code.claude.com/docs/en/routines)
- Scheduled tasks: "Scheduled tasks are available on Pro, Max, Ultra, Team, and Enterprise plans". They are created at claude.ai/code/routines, from the desktop app, or with `/schedule` in any session. Triggers are a schedule (hourly/daily/weekly/one-off), an API POST, or GitHub events. "Expressions that run more often than once per hour are rejected." Cron uses UTC unless prefixed `CRON_TZ=`. Limits are 100 scheduled runs per hour per account and 30 "Run now"/API fires per hour per task. Runs draw down subscription usage like interactive sessions. All connected connectors are included by default (remove unneeded ones), and Claude can use them "including writes". Runs start in auto mode. A run may publish a new private artifact without asking. "Scheduled tasks are in research preview." — [Claude Code docs: scheduled tasks](https://code.claude.com/docs/en/routines)
- Recurring browser tasks in Claude in Chrome launched 24 Nov 2025 (Max, beta). Cowork recurring and on-demand scheduled tasks arrived 25 Feb 2026. — [Release notes](https://support.claude.com/en/articles/12138966-release-notes). Claude in Chrome is included from Pro. — [Claude pricing](https://claude.com/pricing)
- Claude Duet (21 Oct 2026): "A research preview is available by waitlist today, starting with US Pro, Max, and Ultra subscribers". It is a standalone iOS/Android app plus claude.ai. "Checks your connected accounts every few hours". "Each morning, it sends you a short brief on the most important items across your connected apps". It carries over memory, skills and connected apps, runs on its own cloud VM and browser, and asks before sending, paying, signing or deleting. Personal errands like booking are "not quite as strong". It shares plan usage limits. — [Anthropic: Claude Duet](https://claude.com/resources/articles/claude-duet); [Let's Data Science](https://letsdatascience.com/news/anthropic-opens-claude-duet-research-preview-for-proactive-a-16522f5d) [Secondary]
- Merged experience scheduling: "Schedule it for every Monday, and Claude starts on the report without being asked." — [Cowork is now Claude](https://claude.com/resources/articles/cowork-is-now-claude)
- Claude Code iOS skill-registration issue (April 2026): see §3. — [GitHub issue #48696](https://github.com/anthropics/claude-code/issues/48696) [Secondary]

### Inferences
- **Observation:** this session's remote-control tools let a Claude Code session create scheduled tasks in three modes (fire into the same session, another session, or a fresh session each time) with `CRON_TZ` support. They also expose **completion notifications: "push sends to the owner's phone when a run finishes with something noteworthy; email…"**, which only fresh-session-per-fire tasks accept. A morning digest that pushes to the phone is therefore technically supported from Claude Code. Task setup can be done by asking Claude in a Code-tab session on the phone.
- A morning-digest task has **no device GPS**, so it must read "current city/dates" from the profile store (repo file, Drive doc or MCP). The `CRON_TZ` must be updated when moving between Moscow (UTC+3), Kathmandu (UTC+5:45), India (UTC+5:30) and Bali (UTC+8). The prompt can instruct Claude to do this itself.
- Claude Code on the phone suits **maintenance** (editing the repo, profile and skills, building artifacts and the MCP server) more than spontaneous on-street use. On-the-go use is better in regular chat or voice with location and maps.
- Duet is the closest to "proactive guide", but it is US-only and inbox/calendar-oriented. It is not available in Nepal/Russia now.

### Gaps
- Whether chat-side "Hand off and schedule tasks" (merged experience) sends push notifications on mobile, and its frequency limits.
- Whether the mobile Code tab supports every routine-management feature (docs list web, desktop and CLI).

---

## 10. Anthropic's official prompting guidance (current models) relevant to a guide system prompt or skill

### Takeaway
Anthropic's Nov 2026 "Prompting best practices" (covering Fable 5.1, Mythos 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5 and older models) recommends: be clear and explicit, explain *why* (context and motivation), use 3–5 diverse examples in `<example>` tags, structure with XML tags, give a role, say what to do rather than what not to do, and match the prompt's style to the desired output. Avoid aggressive "CRITICAL/MUST" language, which causes overtriggering on new models, and control verbosity explicitly. Put long data first and the query last.

### Cited Findings
- "Claude responds well to clear, explicit instructions… If you want Claude to do more than the task strictly requires, explicitly request it". "Think of Claude as a brilliant but new employee who lacks context on your norms". Key test: show the prompt to a colleague with minimal context. — [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Add context and motivation. Example: instead of "NEVER use ellipses", say "Your response will be read aloud by a text-to-speech engine, so never use ellipses…". "Claude can generalize from the explanation." (Directly relevant to voice-mode output.) — [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Examples should be relevant, diverse and wrapped in `<example>`/`<examples>`; "Include 3–5 examples for best results." — [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- XML tags (`<instructions>`, `<context>`, `<input>`) reduce misinterpretation. Use consistent names and nest them. Give Claude a role in the system prompt, where "Even a single sentence makes a difference". — [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Verbosity: the latest models are "more concise", "might skip detailed summaries". Opus 5 is an exception whose responses run longer, so "Prompt explicitly for conciseness". Format control: say what to do instead of what not to do, use XML format indicators, and match the prompt style to the output. — [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Tool use: models follow instructions precisely. "Can you suggest some changes" leads to suggestions only, so be explicit for action. There is an optional `<default_to_action>` block. "Where you might have said 'CRITICAL: You MUST use this tool when...,' you can use more normal prompting such as 'Use this tool when...'". "Instructions such as 'If in doubt, use [tool]' cause overtriggering." — [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Long context (20k+ tokens): put long documents at the top and the query at the end ("can improve response quality by up to 30 percent"), and wrap documents in `<document>` with `<source>` metadata. — [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Research tasks: give clear success criteria, encourage verification across multiple sources, and track competing hypotheses and confidence. — [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Agentic state management sections exist ("Long-horizon reasoning and state tracking", "State management best practices", e.g. persisting progress in files). — [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- The merged Claude experience "asks clarifying questions when a request is unclear" by design. — [Cowork is now Claude](https://claude.com/resources/articles/cowork-is-now-claude)

### Inferences
- For the guide: state the scenarios and the expected output shape for each (e.g. "here and now", max 3 options with distance, open-now status and why it fits the profile). Explain why brevity matters (walking, small screen, TTS). Give 3–5 short Russian examples of ideal answers. Use XML-tagged sections (`<profile>`, `<places_log>`, `<scenario_rules>`). Avoid shouting language in skill descriptions. Tell it explicitly to update the log ("when I say I liked a place, call `log_place`" or "save to memory").
- Clarifying questions: give an explicit policy, such as asking at most one question in "here and now" mode but asking about dates, budget and pace before multi-day plans. This matches Anthropic's "be explicit about the behavior you want" advice.

### Gaps
- I did not fetch the model-specific pages (e.g. "Prompting Claude Opus 5.5 / Sonnet 5.5"), which hold finer guidance on effort and verbosity per model.

---

## 11. Best "single source of truth" for the taste profile and places log (readable and writable from mobile)

### Takeaway
No single built-in store is both structured and fully writable from mobile chat on every plan. Ranked by robustness for read+write from the phone: (1) **personal custom MCP connector** (free Cloudflare Worker + KV/D1). It works in chat, voice, routines and artifacts, but costs build effort and uses Free's single slot. (2) **GitHub repo** edited via Claude Code (Pro+, Code tab on the phone). It is structured, versioned and usable by routines, but clunky for on-the-street logging. (3) **Notion** via connector (write-capable per secondary sources; Notion's free tier is fine). (4) **Google Drive**: create and read only, no in-place edit except via the beta Docs connector. (5) **Claude memory**: easiest (voice, all plans) but unstructured. (6) **Project files**: read-only for Claude. (7) **Artifact storage**: Claude Code artifact `db` is read/write for Claude, but only from Claude Code sessions, with mobile storage support undocumented for chat artifacts.

### Cited Findings
- Memory: writable by explicit request in chat on Free/Pro/Max/Ultra, mobile included, and editable in Settings. Project memory is scoped per project. Export is experimental. — [Memory help](https://support.claude.com/en/articles/11817273-using-claude-s-chat-search-and-memory-to-build-on-previous-context)
- Project knowledge: uploads plus RAG on paid plans; no documented model write access. The new Projects Library contains "files Claude produces" (beta, claude.ai/code and desktop). — [What are projects](https://support.claude.com/en/articles/9517075-what-are-projects)
- Google Drive: mid-2026 reports of no edit tool for existing Docs — [claudeissues #72576](https://claudeissues.com/issue/72576-google-drive-mcp-integration-missing-write-edit-support-for-existing-docs). The Google Docs connector (beta) edits in place with approval cards — [Anthropic blog, 6 Oct 2026](https://claude.com/blog/claude-now-works-in-google-docs-sheets-and-slides)
- Notion connector can create and edit pages (search about 30 req/min). — [tl;dv](https://tldv.io/blog/best-claude-connectors/) [Secondary]
- Custom connector on all plans (Free: 1), usable on mobile apps. — [Custom connectors help](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp)
- Claude Code cloud sessions from the mobile Code tab can push to GitHub (Pro+). — [Claude Code cloud docs](https://code.claude.com/docs/en/claude-code-on-the-web)
- Chat artifact persistent storage: Pro+, web and desktop, 20 MB text. — [What are artifacts](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)
- Scheduled tasks can read and write via connectors and repos. — [Scheduled tasks docs](https://code.claude.com/docs/en/routines)

### Inferences
- **Recommended hybrid (inference):**
  - **Memory (project-scoped)** holds the short, evolving taste profile ("likes quiet rooftop cafés, dislikes tourist traps, vegetarian-friendly, walks 10–15 km/day").
  - **One structured store** holds the places log. Use a custom MCP connector if the user is willing to build it once; otherwise Notion (free) via connector, or a GitHub repo maintained through Claude Code.
  - **Skill / Project instructions** hold the method and rules.
  - Claude periodically "compacts" log insights back into memory or profile.
- On a Free plan, the realistic options are memory, a Notion connector, or the single custom MCP slot (no Claude Code). Drive is usable as append-only (one new file per entry or trip) if the Drive connector is available on Free.
- Whatever the store, give Claude explicit write triggers in the instructions (e.g. "after I rate a place, append it to the log with city, area, category, rating 1–5, date, short note, lat/lon if known").

### Gaps
- Free-plan access to the Google Drive / Notion / GitHub directory connectors: pricing says "connectors" are on Free, but per-connector availability isn't listed.
- Read/write behaviour of the Notion connector in Nov 2026 (no primary source fetched).

---

## 12. Comparison of implementation forms: Project vs Skill vs custom connector/MCP vs GitHub repo + Claude Code vs artifact/web app

### Takeaway
These forms are complementary layers, not alternatives. **Project** = always-on context for a dedicated travel chat (instructions + knowledge + scoped memory; all plans; read-mostly). **Skill** = portable, auto-triggered method and templates in any chat (all plans; static; needs code execution; mobile untested). **Custom MCP** = live, structured read/write memory and tools usable everywhere, including voice and routines (all plans, Free: 1; build effort). **GitHub repo + Claude Code** = versioned source of truth plus automation (morning digest, push notifications) and building blocks (Pro+; GitHub required; awkward on the street). **Artifact** = visual and interactive layer (itinerary, places browser, ask-the-guide box). Its storage, AI and connector features are Pro+ and documented for web/desktop; map tiles and GPS are blocked in Claude Code artifacts.

### Cited Findings
- Project: instructions, knowledge, RAG (paid) and project memory. — [What are projects](https://support.claude.com/en/articles/9517075-what-are-projects); [Memory help](https://support.claude.com/en/articles/11817273-using-claude-s-chat-search-and-memory-to-build-on-previous-context)
- Skill: auto-selected by description, all plans, code execution required, one-way sync to Claude Code. — [Using skills](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- Custom MCP: all plans (Free: 1), every client including mobile; OAuth, no-auth or header auth. — [Custom connectors help](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp)
- Claude Code cloud from mobile, scheduled tasks hourly-minimum with connectors, research preview, Pro+. — [Cloud sessions](https://code.claude.com/docs/en/claude-code-on-the-web); [Scheduled tasks](https://code.claude.com/docs/en/routines)
- Artifacts: storage, AI and MCP Pro+ on web and desktop. Claude Code artifacts' CSP blocks external images and fetches, and connector calls go through the viewer's account. — [What are artifacts](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them); [Claude Code artifacts](https://code.claude.com/docs/en/artifacts)
- Native location tool + interactive map in mobile chat, all individual plans. — [iOS](https://support.claude.com/en/articles/11869619-use-claude-with-ios-apps); [Android](https://support.claude.com/en/articles/11869629-use-claude-with-android-apps)

### Inferences
What each form concretely adds to **recommendation quality**:
- *Project*: consistent persona, rules and the full profile in context, so fewer generic suggestions.
- *Skill*: high-quality scenario playbooks and output templates, so consistent structure (distance, open hours, why it fits, plan B).
- *MCP / store*: real "visited/liked" data, so no repeats and better taste matching over time.
- *Claude Code*: can run scripts (e.g. route time or ordering heuristics) and keep curated region guides in the repo.
- *Artifact*: better overview for multi-day plans.

What each adds to **convenience on mobile**:
- *Native chat + location + voice*: zero setup and best for scenario 1 ("here and now").
- *Project*: one tap to the "Гид" chat.
- *Skill*: works in any chat without choosing a project.
- *MCP*: one-sentence logging by voice ("сохрани: понравилось").
- *Routine*: proactive morning digest with push (Pro+).
- *Artifact*: a bookmarkable itinerary page.

Mapping to scenarios:
1. "Here and now": mobile chat or voice, location tool, web search, profile from memory/Project, log via MCP or memory.
2. "Walk/day in a new place": the same, plus a Skill playbook for routing and ordering, with an in-chat map or a Google Maps link list.
3. "Multi-day trip": Project chat with Research (Pro+), optionally an itinerary artifact; save the trip plan to the store.
4. "New things in a familiar city": requires the visited log, so the MCP / Notion / GitHub store is the key enabler, plus web search for new openings and events, and optionally a weekly scheduled task scanning news.

### Gaps
- No end-to-end test was done on a phone (e.g. Skill triggering in mobile chat, voice mode + custom connector, artifact storage in the iOS app). These should be validated by the user, or flagged in the final report as "verify on device".
