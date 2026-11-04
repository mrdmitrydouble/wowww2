# Preference elicitation, situational context, memory and novelty for an LLM travel/POI guide: state of the art 2024–2026

Scope: LLM-based conversational recommendation for places, walks, routes and trips. The emphasis is on Nov 2025–Nov 2026. Output is meant for a system built from a system prompt/skill plus a text profile file, with no custom ML.

Evidence labels used throughout:
- **[S] strong**: peer-reviewed and large-scale or multi-model, live A/B, or several independent studies that agree.
- **[M] moderate**: a single peer-reviewed study, or a well-designed benchmark (often with simulated users).
- **[W] weak**: a small user study, workshop paper, single unreplicated preprint, vendor claim or position piece.
- **[F] foundational**: pre-2024 work, older but still the basis of current practice.
- **[I]**: my inference, not a finding.

Many 2026 items are arXiv preprints that have not been peer reviewed yet. They are flagged.

---

## Q1. When should an LLM agent ask a clarifying question vs act on assumptions?

### Takeaway
The 2025–2026 evidence agrees that agents should ask rarely but well. Capping questions at 1–3 keeps about 90% of task value and cuts user burden by roughly half. The decision to ask should rest on whether the answer would change the action (expected value of information), not on whether something is merely unknown. LLMs left to themselves either over-ask or ask uninformative questions. One new human study also found that asking makes users trust the answer more and check it less, so answers built on elicited constraints still need explicit verification.

### Cited Findings
- **Question budgets work.** Capping agents at 1–3 clarifying questions cut user-attention cost by 36–73% while keeping 86–94% of the reward that unlimited questioning achieved. The test covered 8 LLMs in 4 customer-service domains. Checking each candidate question against memory of the user's earlier answers cut attention cost by another 13% with little reward loss. At equal attention cost, the best models got more than 2x as much reward per question as the others, so "ask less" and "ask better" are separate goals. [M; preprint, Oct 2026; the cost metric was validated against human judgments with 75% pairwise agreement] — [Zhang et al., "Ask Less, Ask Better", arXiv 2610.24411](https://arxiv.org/abs/2610.24411)
- **Asking changes user vigilance.** In a between-subjects study (N=180, Prolific, everyday decisions such as a group dinner or apartment hunting), two clarifying questions before answering raised perceived understanding (5.4 vs 4.9, p=.020) and satisfaction (5.3 vs 4.9, p=.043). The same participants reviewed answers for less time (55s vs 81s) and accepted more responses unchanged (60% vs 46%), including erroneous ones (52% vs 39%). Constraint violations in the parts of the answer the questions had covered were accepted more often (60% vs 43%) and reported less often (23% vs 37%). The authors recommend showing which constraints were checked and adding extra system-side verification of content built on elicited preferences. [M; preprint, Nov 2026; single human study] — [Zheng et al., "Is That Clear?", arXiv 2611.01087](https://arxiv.org/html/2611.01087)
- **Ask only when the answer changes the action (EVPI).** SAGE-Agent keeps a belief over candidate actions and acts directly when the top candidate clears a probability threshold. Otherwise it scores candidate questions by Expected Value of Perfect Information, with a penalty for asking about the same parameter again, and stops asking when the best question's value is small relative to its current confidence. It reports 7–39% higher coverage with 1.5–2.7x fewer questions than baselines (1.39 questions per task on ClarifyBench with GPT-4o). [M; preprint, Nov 2025; simulated benchmark] — [Suri et al., SAGE-Agent, arXiv 2511.08798](https://arxiv.org/html/2511.08798v2)
- **Separate "is something missing?" from "do the task."** A multi-agent scaffold that separates detecting underspecification from executing the task reached a 69.4% resolve rate on underspecified SWE-bench Verified. That closes much of the gap with fully specified instructions. It asks fewer questions on simple tasks and more on complex ones. [M; EMNLP 2026] — [Edwards & Schuster, "Ask or Assume?", arXiv 2603.26233](https://arxiv.org/abs/2603.26233)
- **Over-asking is a named failure mode.** In the same work, a baseline agent asked questions in nearly every instance regardless of need. The LHAW benchmark has an explicit over-clarification taxonomy: redundant questions, questions about information already given, and question counts out of proportion to the gain. [M] — [search summary of arXiv 2603.26233 and LHAW arXiv 2602.10525](https://arxiv.org/pdf/2602.10525)
- **Learning when to ask.** Standard RLHF rewards direct single-turn answers. Labelling preferences by simulating future turns teaches models to ask only when needed: +5% F1 on recovering users' intended interpretations and +3% accuracy on deciding when to ask. [M; ICLR 2025] — [Zhang et al., "Modeling Future Conversation Turns to Teach LLMs to Ask Clarifying Questions"](https://arxiv.org/abs/2410.13788)
- **LLMs ask uninformative questions by default.** Measured by expected information gain in a 20-Questions setting, LLMs often generate uninformative questions. DPO training improves this. [M; EMNLP Findings 2024] — [Mazzaccara, Testoni & Bernardi](https://iris.unitn.it/retrieve/9431dc31-20ed-4c37-a0ce-c3c7f1f8ffd1/LearningToAskInformativeQuestions.pdf)
- **An explicit belief state beats a monolithic LLM elicitor.** PEBOL keeps Bayesian beliefs over items, uses natural-language inference between the user's statements and item descriptions, and picks queries with Thompson sampling or UCB. After 10 turns it reached MRR@10 of 0.27 vs 0.17 for the best monolithic LLM baseline. The authors argue that monolithic LLMs lack the multi-turn, decision-theoretic exploration/exploitation reasoning that elicitation needs. [M; 2024 preprint; simulated users] — [Austin et al., arXiv 2405.00981](https://arxiv.org/abs/2405.00981)
- **More answers can make LLM recommendations worse.** With out-of-the-box LLM conversational recommenders (GPT-3.5, GPT-4, Claude 3.5 Sonnet), "the more questions a user answers about their preferences, the worse the model's recommendations become." The loss came from recall: extra information filtered out bad items but made the model lose confidence in good ones. The fixes were combining a predetermined initial question, item-centred questions (which items the user enjoys), "Incremental Prediction" (an explicit running prediction after each turn) and "Aggregate Context". Only the combination worked. Zero-shot chain-of-thought hurt performance. [M; COLING 2025; LLM-simulated users built from real Reddit requests; small absolute effects of 1–4 points] — [de Carvalho et al., "A Flash in the Pan", COLING 2025](https://aclanthology.org/2025.coling-main.561.pdf)
- **Funnel order: broad questions first.** Google trained a questioner to ask broad, easy questions first (genre, era) and specific ones later (director, tone, details). Including past questions with their answers reduced repetition, but only for the fine-tuned model. [M/W; workshop paper (SIGIR GenNext 2025) and preprint Oct 2025; MovieLens with simulated users] — [Montazeralghaem, Tennenholtz, Boutilier & Meshi, arXiv 2510.12015](https://arxiv.org/html/2510.12015v1)
- **Attention-limited oversight.** A model of one human supervising several agents with limited attention lowered cost by 18–31% compared with three standard "when to ask" rules. [W; preprint, Oct 2026; 864 synthetic cases] — [arXiv 2610.41129](https://arxiv.org/abs/2610.41129)

### Inferences
- [I] A prompt-only policy can approximate EVPI: "List the 2–3 most plausible readings of the request. If your top recommendation is the same under all of them, do not ask. Otherwise ask the one question whose answer separates them." This is the SAGE-Agent stopping rule turned into words.
- [I] "Ask by showing" fits mobile and voice better than a bare question. The user's choice among 2–3 contrasting options works as the clarifying answer, and the user gets value on the same turn. This combines the item-centred finding (COLING 2025) with question budgets (Ask Less, Ask Better).
- [I] Every clarified constraint should be visibly re-checked in the output ("fits: ≤30 min, quiet, open now"). The Is That Clear? finding shows clarification lowers user vigilance exactly where errors matter.
- [I] Check the profile and the session's earlier answers before asking anything. This is the −13% attention-cost lever (memory review), and it avoids LHAW's "question about information already given".

### Gaps
- No study found tests ask-vs-act specifically for travel/POI with real mobile users.
- No study measures the cost of a question in voice mode, or in a second-language or bilingual (Russian) setting.
- Most evidence uses simulated users. Only Is That Clear? (N=180) is a human study, and it was not about travel.

---

## Q2. Which elicitation formats extract the most preference signal per unit of user effort?

### Takeaway
Concrete items beat abstract attributes. Asking "which places/items did you love?", or reacting to shown options, gives more usable signal than "what features do you prefer?". Interactive elicitation takes less user effort than writing a prompt or labelling examples. Critiques of shown options ("too touristy", "closer") are the classic low-effort refinement channel and LLMs now handle them in free text. Picture-based elicitation is an established tourism method for users who cannot state preferences, but it measures appeal, not intent. Head-to-head comparisons of pairwise vs choose-one-of-three vs "describe the vibe" for LLM travel agents are missing.

### Cited Findings
- **Item-centred beats abstract.** Nudging the LLM to ask about item examples ("what movies the user enjoys") rather than abstract attributes was the key elicitation improvement in an LLM conversational recommender. [M; COLING 2025] — [de Carvalho et al.](https://aclanthology.org/2025.coling-main.561.pdf)
- **Interactive elicitation takes less effort.** In GATE, an LM elicits the task by asking questions. Users reported that interactive elicitation required less effort than writing prompts or labelling examples, and predictive performance was comparable or better. [M; ICLR 2025; human study] — [Li, Tamkin, Goodman & Andreas, "Eliciting Human Preferences with Language Models"](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9867d5a22653ce98b02595061e40f12-Paper-Conference.pdf)
- **Free-text critiques help.** Google's REGEN pairs recommendation with natural-language critiques. A single LLM (LUMEN) handles critiquing, retrieval and generation, and adding critiques improved recommendation quality. [M/W; preprint 2025; critiques were generated synthetically from Amazon reviews, not by live users] — [REGEN, arXiv 2503.11924](https://arxiv.org/html/2503.11924v1); [Google Research page](https://research.google/pubs/regen-a-dataset-and-benchmarks-with-natural-language-critiques-and-narratives)
- **Critiquing background.** Critiquing-based recommenders, both system-suggested critiques ("cheaper", "closer") and user-initiated ones, are the long-standing low-effort format for refining recommendations. [F] — [Chen & Pu, critiquing survey (EPFL record)](https://infoscience.epfl.ch/record/176775)
- **Picture-based tourism elicitation.** Users pick appealing photos and the system infers a "seven-factor" travel profile. The premise is that tourism is emotional and people struggle to state travel preferences early on. In a 2020 user study (N=81), participants could adjust the predicted profile, which supported the approach. [F/W] — [Sertkan, Neidhardt & Werthner, "Eliciting Touristic Profiles: A User Study on Picture Collections", arXiv 2006.05172](https://ar5iv.arxiv.org/html/2006.05172); [PicTouRe code](https://www.github.com/MeteSertkan/PicTouRe)
- **Users want different dialogue styles.** In a within-subjects study (N=139) with two scripted CRS dialogues, preference for an exploratory interaction style was predicted by enjoyment, usefulness, novelty and conversational quality. Clustering found five latent user profiles with distinct style preferences. Age, gender and desire for control moderated the choice. [W/M; OZCHI 2025] — [Mahmud et al., arXiv 2508.02328](https://arxiv.org/abs/2508.02328)
- **Voice favours the first and most popular options.** With podcast recommendations delivered by voice vs on screen (N=100), listeners mostly picked among the first options offered. Readers explored much more and were less likely to choose the most popular or top-rated items. Enjoyment did not differ. The authors advise that voice systems offer top-ranked choices that are diverse, personalized and changed often. [F; RecSys 2018] — [Cornell Tech summary of Yang et al.](https://tech.cornell.edu/news/study-smart-speakers-make-passive-listeners)
- **Summarize-and-refine for spoken options.** In spoken dialogue systems, presenting a few options chosen with a user model, then summarizing and refining, was more efficient and preferred over data-driven clustering. Plain user-model presentation does not scale to many options. [F] — [Winterboer & Moore line of work, Edinburgh](https://era.ed.ac.uk/bitstreams/fe1279df-b2c1-4877-ae12-ffdefb0b51a0/download); [EACL 2006](https://www.coli.uni-saarland.de/~vera/EACL06.pdf)
- **Choice overload.** Comparing top-20 and top-5 lists, choice difficulty increased when many items were about equally attractive and not diverse. Item diversity moderates choice overload. [F; RecSys 2010; exact effect sizes not verified this session] — [Bollen, Knijnenburg, Willemsen & Graus, RecSys 2010 (DBLP)](https://dblp1.uni-trier.de/rec/conf/recsys/BollenKWG10.html); [follow-up by the same group, UMUAI](https://link.springer.com/article/10.1007/s11257-016-9178-6)
- **Pairwise judgments by LLMs are biased.** In LLM-as-judge pairwise setups, LLM evaluators amplify biased preferences and reject ties. This concerns the LLM judging, not users choosing, but it argues against having the LLM silently pairwise-rank options in place of the user's own choice. [M; BlackboxNLP 2025] — [The Comparative Trap](https://aclanthology.org/2025.blackboxnlp-1.5/)
- **Elicitation efficiency in CRS user studies.** Efficiency is typically measured objectively (time spent, number of preference refinements, clicks) alongside subjective measures. The 2026 ACM study comparing elicitation strategies could not be fetched, so its results are unknown. — [ACM DL 10.1145/3774935.3803059](https://dl.acm.org/doi/10.1145/3774935.3803059)

### Inferences
- [I] **On the go:** use "choose one of 2–3 contrasting options" (a choice-based critique) with no preliminary question. Each option should differ along the dimension of greatest uncertainty, such as classic vs local-offbeat or calm vs lively. The pick, or a critique like "neither, too far", is the elicitation signal. Diverse options also counter choice overload.
- [I] **Trip planning:** use a short funnel (Q1) that starts with an item-centred anchor question: "name 1–3 places from past trips you loved and 1 you regretted". Follow with 2–3 broad dimensions (pace, mainstream-vs-offbeat appetite, budget/comfort, company) and then specifics.
- [I] Photos the user sends ("like this?") should be logged as **appeal** signals and kept separate from intent (see Q4/Q7). The picture-based literature measures attraction to an image, not willingness to go or enjoyment.
- [I] "Describe the vibe" open questions are cheap for the user (one voice utterance). Their output should be converted back into 2–3 concrete candidates to confirm, because abstract statements under-perform item-centred signals.
- [I] Store an "interaction style" field in the profile (prefers one confident pick vs a menu; wants explanations or not), since users split into distinct style clusters.

### Gaps
- No 2024–2026 empirical comparison was found of pairwise vs choose-one-of-three vs open "vibe" questions in LLM travel recommendation.
- No study was found on image-based elicitation with multimodal LLMs for travel since 2020.
- Choice-overload thresholds for voice output with LLMs are unmeasured.

---

## Q3. How should situational context (mood, energy, intent, time, weather, companions) be modelled and elicited cheaply?

### Takeaway
Context-aware recommender research supports a small set of context factors: time, weather, companions, mood/intent, budget and location. LLMs integrate user-stated context well but do worst at time coherence. They also under-use real-time context unless it is supplied from tools (weather, events, crowds). Context should be inferred from the message plus tools where possible, with at most one question about the highest-impact unknown, usually time budget or energy. Per-trip context must not leak into durable memory (see Q4).

### Cited Findings
- **LLM itinerary user study (GPT-4 "GPT Trip Planner", N=30, 60 plans in 20 cities).** Including user-defined travel profiles in prompts raised ratings on every criterion. POI coherence was high (4.13/4.00 of 5). **Time coherence** was lower (3.65/3.78) and originality moderate (3.90). Participants flagged hallucinated POI locations, under-used time, over-reliance on popular POIs, and missing weather, events and visitor density. The authors' guidelines: (1) identify districts, assign them to time slots based on travel time and opening hours, then pick POIs per district; (2) add a "travel style" parameter (relaxed / balanced / intensive) to set POI count; (3) let users set their desired exploration level, from mainstream to off-the-beaten-path; (4) use weather APIs and event data, for example indoor options in bad weather. [W; RecTour@RecSys 2025 workshop; small N] — [González-Sanz, Cantador & Bellogín, CEUR Vol-4052 paper 6](https://ceur-ws.org/Vol-4052/paper6.pdf)
- **Popularity calibration plus context.** On Brightkite, Foursquare, Gowalla and Yelp, context-aware models alone are not a uniform fix for popularity bias. Popularity calibration (matching recommendations to each user's own popularity profile) works but trades off accuracy. Combining context-awareness with calibration gave the best balance. [M; RecSys 2025] — [Forster, Kopeinik, Helic, Thalmann & Kowald, arXiv 2507.03503](https://arxiv.org/abs/2507.03503)
- **Mood, budget, companion and location** are the four core context factors of a 2025 context-aware POI recommender, with mood, budget and companion supplied by the user. [W; non-LLM, details unverified] — [ResearchGate: "A Personalized Context-Aware Places of Interest Recommender System"](https://www.researchgate.net/publication/390744434_A_Personalized_Context-Aware_Places_of_Interest_Recommender_System)
- **Time-aware LLM user profiles** for context-aware recommendation were assessed at CARS 2025. Only the title and framing were verified. [W] — [Sabouri et al., arXiv 2508.08512](https://arxiv.org/pdf/2508.08512)
- **POI pitfalls review.** Popularity bias is more pronounced in POI recommenders than in other recommender systems, and recommending popular POIs can worsen massification of central venues. [M; review 2025] — [arXiv 2507.13725](https://arxiv.org/pdf/2507.13725)
- **Remembered experience drives future choice.** In a spring-break study, remembered experience, not in-the-moment or anticipated experience, directly predicted the desire to repeat the trip. Both predicted and remembered experiences were more extreme than real-time ratings. [F; Psychological Science 2003] — [Wirtz, Kruger, Scollon & Diener (World Database of Happiness entry)](https://worlddatabaseofhappiness.eur.nl/publications/what-to-do-on-spring-break-the-role-of-predicted-on-line-and-remembered-experience-in-future-choice-4365/)

### Inferences
- [I] **A practical state model** of 6 slots, each with a default and a source:
  - `time_budget`: from the message, otherwise ask. This is the highest-impact slot.
  - `energy` (low / medium / high): from the message, time of day, or a previous long day in the log.
  - `intent/mood` (recharge, explore, social, photo, eat, culture, nature).
  - `company` (solo, partner, friends, family). Default solo when travelling alone, per the profile.
  - `weather/daylight`: from a tool, never asked.
  - `location/transport`: from the message or the app.
- [I] **One-question rule for state:** if both time and energy are unknown, ask a combined question such as "How much time do you have, and do you want to walk a lot or take it easy?" Voice makes compound questions cheap.
- [I] **Fold mood into the contrasting options** rather than asking about it ("calm: X; lively: Y; unusual: Z").
- [I] Low energy or a short time budget should push toward familiar, close, low-risk options. A free day with high energy can carry more novelty. This matches the calibration finding that the right popularity mix is per user and per context.

### Gaps
- No 2024–2026 study was found that measures how best to elicit mood or energy in LLM travel chat. Evidence on mood as a POI context factor comes from small or non-LLM studies.
- No study on weather-conditioned LLM itinerary quality was found beyond the qualitative guidelines above.

---

## Q4. How should taste and the user profile be represented, and how should memory work for an LLM personal guide?

### Takeaway
Natural-language profiles are a viable, editable and scrutable representation: editing the profile changes recommendations. 2025–2026 memory benchmarks show four consistent failures:
1. Models forget or ignore stated preferences as conversations lengthen.
2. Models know a preference but don't act on it.
3. Models fail to update beliefs when preferences change, often falling back to the old value.
4. Memory writes "promote" passing remarks into durable facts and broaden their scope, which makes errors persistent.

Fixes that work in prompt + file form: keep the profile short and always in context, separate durable taste from episodic notes, tag provenance, date and scope on every entry, gate what gets written, and supersede old values explicitly.

### Cited Findings
- **Preference following collapses with length.** On PrefEval (3,000 preference/query pairs, 20 topics, explicit and implicit preferences), zero-shot preference-following accuracy fell below 10% at only 10 turns (~3k tokens) for most models. Even with prompting and retrieval, following deteriorates in long contexts. Models sometimes inferred a preference correctly and then failed to apply it consistently. Fine-tuning on the benchmark helps. [S; ICLR 2025 oral, 10 models] — [Zhao et al., "Do LLMs Recognize Your Preferences?", arXiv 2502.09597](https://arxiv.org/html/2502.09597v1)
- **Knowing a preference is not acting on it.** Across 16 systems and 5 memory architectures (1,000 preferences at 3 levels of expression strength), agents often pass the recall test for a preference but do not apply it in the matching behavioural scenario. Memory architectures narrow the gap but do not close it. [M; preprint, Jul 2026] — [Feng, Ma & Chersoni, "Know It, Act on It", arXiv 2607.29433](https://arxiv.org/abs/2607.29433)
- **Preference drift and belief-update failure.** HorizonBench has 360 simulated users with 6-month histories of ~4,300 turns each, where life events change preferences without the user restating them. The best model (Claude Opus 4.5) scored 52.8%, below the human range of 56–64%. All 25 models did worse on evolved preferences than on static ones. In over a third of errors on evolved preferences, models chose the user's original value. The failure persists in short-horizon variants, so it is a state-tracking problem, not only a context-length one. [M; preprint, Apr 2026; synthetic] — [Li et al., HorizonBench, arXiv 2604.17283](https://arxiv.org/abs/2604.17283)
- **Persistent sycophancy through memory writes.** When an agent commits a user's claim to durable state, downstream failure rises from 45.0% (session only) to 71.9% (+27 points). Three write-time pathologies:
  - **status promotion**, in 51.4% of episodes: a passing remark becomes a stable preference, or a task-specific instruction becomes a general rule;
  - **attribution removal**, in 33.1%: the source of the claim is dropped;
  - **scope broadening**: cross-domain committed claims add 12.6–22.8 points of failure.

  Proposed governance ladder: commit gating (write only stable, relevant, future-appropriate content); stricter criteria for profiles than for temporary notes; preserving source, uncertainty and intended use; scope-aware retrieval bounded by task, domain and time; and lifecycle audits with rollback. [M/S; preprint, Jul 2026; 12 models, 2 agent frameworks] — [Mao et al., arXiv 2607.10526](https://arxiv.org/html/2607.10526v3)
- **Linked memory beats raw dialogue retrieval, but long spans remain hard.** On PERMA, memory systems that link related interactions extracted preferences more precisely and used fewer tokens than semantic retrieval of raw dialogue. They still struggled to keep a coherent persona across long time spans and under cross-domain interference. [M; preprint, Mar 2026] — [PERMA, arXiv 2603.23231](https://arxiv.org/abs/2603.23231)
- **LongMemEval.** Covers information extraction, multi-session reasoning, temporal reasoning, knowledge updates and abstention. Commercial assistants and long-context LLMs lose about 30% accuracy on long interactive histories. Design levers that helped: session decomposition, keys expanded with extracted user facts, and time-aware query expansion. Knowledge-update and multi-session questions are among the hardest. [S; ICLR 2025] — [NeurIPS/ICLR listing](https://neurips.cc/virtual/2024/104893); [secondary summary](https://www.emergentmind.com/topics/longmemeval)
- **Benchmarks under-test consolidation.** Existing memory benchmarks mostly test shallow cross-session retrieval: average memory consolidation is about one session, with little stress on memory mutation or forgetting. [M; preprint, Apr 2026] — [From Recall to Forgetting, arXiv 2604.20006](https://arxiv.org/pdf/2604.20006)
- **Editable natural-language profiles.** User Profile Recommendation generates natural-language profiles from reviews and recommends from them. Editing the profile directly changes downstream recommendations, which makes the system scrutable. [M; ACL 2024] — [Ramos et al., ACL 2024](https://aclanthology.org/2024.acl-long.753.pdf). A 2026 reproduction with open-weight models confirms the profiles are useful and increase transparency and scrutability, and that users can correct misattributed preferences. [M; preprint] — [arXiv 2609.19831](https://arxiv.org/html/2609.19831)
- **Users may not recognize themselves in generated profiles.** A 2025 music study found it unclear whether users consider LLM-generated taste profiles accurate, and identification varied with user and item attributes. A music-recommendation survey notes profiles must be concise to be scrutable, and describes editable "taste cards" that change rankings without retraining. [W/M] — [Biases in LLM-generated musical taste profiles, arXiv 2507.16708](https://awesomepapers.io/recommender-systems/papers/2507.16708); [Music Recommendation with LLMs survey, arXiv 2511.16478](https://arxiv.org/html/2511.16478v3)
- **Stated vs revealed preferences.** In a study of young adults' social-media news feeds, what users say they want and what their behaviour suggests diverge. Participants saw the gap as platform incentives working against their values, and preferred feeds built on stated preferences. [M; ACM journal 2026] — [Understanding the Gap Between Stated and Revealed Preferences, ACM 10.1145/3817029](https://dl.acm.org/doi/10.1145/3817029); [arXiv 2604.11517](https://arxiv.org/pdf/2604.11517). A 2026 preprint argues LLM recommenders should use explicit, context-rich textual feedback rather than only implicit logs. [W] — [arXiv 2605.29141](https://arxiv.org/html/2605.29141v1)
- **Not interacted is not the same as disliked.** In recommender learning, missing interactions are missing-not-at-random: users are never exposed to most items, so unobserved items are not negatives. This bias falls hardest on less popular items, which are less likely to be seen. [F/M; WSDM 2020 and follow-ups] — [Saito et al., "Unbiased Recommender Learning from MNAR Implicit Feedback", arXiv 1909.03601](https://alphaxiv.org/abs/1909.03601); [Google Research BISER](https://research.google/pubs/bilateral-self-unbiased-recommender-learning-for-missing-not-at-random-implicit-feedback/)
- **Image ≠ expectation ≠ experience.**
  - Anticipation and recollection of trips are rosier than the experience itself ("rosy view", from a 10-day Europe trip, a Thanksgiving vacation and a 3-week bike tour). [F; JESP 1997] — [APS Observer on Mitchell & Thompson](https://www.psychologicalscience.org/observer/vacation-not-what-you-remember)
  - Remembered experience, not in-the-moment experience, predicts the wish to repeat. [F; 2003] — [Wirtz et al.](https://worlddatabaseofhappiness.eur.nl/publications/what-to-do-on-spring-break-the-role-of-predicted-on-line-and-remembered-experience-in-future-choice-4365/)
  - Small tourism studies find that idealized Instagram imagery (e.g., influencer Reels of the Colosseum) leaves out crowds and safety issues that surface in visitor reports, and that "hidden spot" content can lead to disappointment. Pre-trip exposure to user-generated imagery hurt on-site experience in a thesis study. [W] — [Soares 2025 (RePEc)](https://ideas.repec.org/h/spr/prbchp/978-3-031-83705-0_24.html); [van der Veen 2023 thesis](https://campus-fryslan.studenttheses.ub.rug.nl/364)

### Inferences
- [I] **Profile file architecture**, mapped to the failures above:
  - (a) A short durable **Taste summary** of about 10–20 lines, always loaded. This addresses PrefEval and Know-vs-Act.
  - (b) **Deal-breakers / hard no's** at the top, checked explicitly on every answer.
  - (c) An **Interaction style** section.
  - (d) A **Places log** in which each place has separate fields: `appeal` (liked a photo or idea), `intent` (wants to go), `visited` (date, context), `experience` (rating plus a one-line reason), and `would_return`.
  - (e) **Current trip / today** constraints with an explicit expiry date, never merged into the taste summary. This prevents status promotion and scope broadening.
  - (f) A **Change log** where old values are marked superseded, with a date, rather than deleted. This addresses HorizonBench and LongMemEval knowledge updates.
- [I] Tag every durable line with provenance and confidence, for example `[said 2026-10-12]`, `[inferred from 3 visits]`, `[guess - confirm]`. This is the sycophancy paper's L3 "source and status preservation" in plain text.
- [I] **Commit gating rule:** promote something to durable taste only if the user states it as general ("I always/never..."), or it is consistent across at least 2 independent experiences. One-offs go to the log.
- [I] **Unvisited is unknown.** "Not visited" and "skipped because of context" (rain, tired, no time) must never be stored as dislikes. Only explicit rejection on taste grounds or a bad experience counts as negative.
- [I] Because users may not recognize themselves in generated profiles, show the profile diff to the user after an update ("I noted: prefers quiet viewpoints over crowded ones, correct?"). Keep it short so it can be checked.

### Gaps
- Episodic vs semantic memory designs for personal travel agents specifically: no travel-specific benchmark was found. Evidence comes from general personalization benchmarks, mostly synthetic.
- How well a static text profile (rather than a memory system) performs compared with tool-based memory was not directly measured anywhere I found.

---

## Q5. Popularity and "touristy" bias in LLM recommenders: how big is it, and what mitigates it?

### Takeaway
LLM travel and place recommendations are measurably skewed toward mainstream items and toward venues with heavy digital footprints. Popularity, not quality, drives the selection: Yelp rating had no significant effect while visits and review counts did. LLMs also write in a promotional, cliché-heavy register. Grounding in real venue lists removes fabricated places but not this selective invisibility. Mitigations with evidence:
- calibration to the user's own popularity appetite;
- context-aware calibration;
- a hybrid in which the LLM proposes novel-but-adjacent interest areas and a retrieval step picks real items (deployed at scale by Google with gains in exploration and enjoyment);
- serendipity-aligned prompting or training.

For a prompt-only system, the practical equivalent is explicit slate composition (anchor + adjacent + wildcard) with justification links, tuned per user and per moment.

### Cited Findings
- **Destination-level audit.** 6,480 recommendations for 216 traveller personas across ChatGPT and DeepSeek showed measurable bias in all six families tested (popularity, geographic, cultural, stereotype, demographic, reinforcement). About 50% (ChatGPT) and 57.9% (DeepSeek) of city recommendations were outside Euromonitor's Top-100, yet both "still favour mainstream destinations". **Japan appeared for 88.9% of ChatGPT personas and 76.9% of DeepSeek personas.** Output was promotional and cliché-dense. Follow-up lists were more than 90% novel, so reinforcement bias was low. The authors propose a re-ranking layer balancing exposure fairness, seasonality, low-carbon routing and stereotype penalties. [M; MDPI *AI* 2025; destination level, not POI level] — [Andreev et al., "Destination (Un)Known", doi 10.3390/ai6090236](https://doi.org/10.3390/ai6090236)
- **POI-level audit: "uneven informational layer over cities".** Restaurant recommendations from GPT-4o-mini, Llama-3.3-70B and Gemini-2.0-flash were checked across 304 neighbourhoods in 5 US cities, with 320 synthetic profiles per neighbourhood.
  - Open-ended prompting: **36.8% of recommended venues did not exist**. Hallucination was higher in neighbourhoods with fewer visits and reviews.
  - Invisibility: on average **96.8% of real venues were never recommended**.
  - With a supplied list of 100 real candidates: hallucination fell to about 0%, but 47.5% of venues were still never recommended. 31.9% of the never-recommended venues were shared across all three models.
  - Selection drivers: more visits, spend and Yelp reviews raised the chance of a recommendation. **Yelp rating had no significant effect.**
  - Profile effects: tourist profiles were steered toward pricier venues than residents.

  [M/S; preprint, Jul 2026; large audit, US only] — [Chen, Weng & Moro, arXiv 2607.06260](https://arxiv.org/html/2607.06260)
- **User-perceived bias.** Participants using generative AI travel planners reported over-representation of popular destinations and a lack of less-known options. Positivity bias appeared in 67.9% of recommendations. [W; details and date not verified] — [ResearchGate: socio-technical exploration of bias in GenAI travel planners](https://www.researchgate.net/publication/403507624_A_socio-technical_exploration_of_bias_in_generative_AI_travel_planners)
- **The same complaint in a real LLM itinerary user study.** Participants noted over-reliance on popular POIs and asked to set their desired exploration level. [W; RecTour 2025] — [González-Sanz et al.](https://ceur-ws.org/Vol-4052/paper6.pdf)
- **Calibrate to the user's popularity profile.** Popularity calibration aligns recommendations with each user's own popularity appetite. Combining it with context-awareness gives the best accuracy/bias balance on four POI datasets. [M; RecSys 2025] — [Forster et al., arXiv 2507.03503](https://arxiv.org/abs/2507.03503)
- **Industry evidence for LLM-guided exploration (Google).** In a hybrid hierarchical approach, an LLM generates **novel interest clusters adjacent to the user's history** (within a controlled cluster vocabulary), and a classic recommender then retrieves items only within those clusters. Live experiments on a platform serving billions of users showed a significant increase in both exploration of novel interests and overall user enjoyment. [M/S; live A/B but preprint; no metrics given in the abstract] — [Wang et al., "LLMs for User Interest Exploration in Large-scale Recommendation Systems", arXiv 2405.16363](https://arxiv.org/abs/2405.16363). A 2025 follow-up using multimodal LLMs for serendipity on a short-form video platform reported significant gains in serendipity and user satisfaction in live experiments. [M; RecSys 2025 EARL workshop] — [arXiv 2506.08283](https://arxiv.org/html/2506.08283v2)
- **Serendipity is "unexpected + relevant" and hard to judge.**
  - SOLAR (EMNLP Findings 2025) aligns an LLM with serendipity-aware objectives and gains in both accuracy and serendipity. [M] — [SOLAR](https://aclanthology.org/2025.findings-emnlp.538.pdf)
  - LLM-as-judge serendipity scores agree only modestly with humans. Multi-LLM averaging improves agreement. [M; RecSys 2025] — [SerenEva, arXiv 2507.17290](https://arxiv.org/pdf/2507.17290)
  - Serendipity-oriented re-ranking trades off against NDCG relevance. [M] — [same search cluster](https://arxiv.org/pdf/2507.17290)
- **Overtourism concern.** Recommending popular POIs worsens massification of central venues, and popularity bias is stronger in POI recommendation than in other domains. [M] — [arXiv 2507.13725](https://arxiv.org/pdf/2507.13725)

### Inferences
- [I] The default LLM output is a "Japan-for-everyone, top-reviewed-venue" distribution. A prompt-level guide must actively counter-steer, not merely "allow" novelty.
- [I] **Slate composition rule** (prompt-implementable analogue of calibration plus Google's adjacent-exploration):
  - For 3 options: 1 **anchor** (a classic or proven type the user likes), 1 **adjacent** (a less-known place sharing a key attribute with something he loved), 1 **wildcard** (unexpected, but tied to a stated value).
  - Tilt the ratio with the exploration dial in the profile and with current state: tired, short time or first day in a city → anchor-heavy; free day, high energy or repeat city → novelty-heavy.
  - Track his acceptance and enjoyment of offbeat picks and calibrate to that, rather than using a fixed quota.
- [I] Serendipity needs a stated bridge ("because you liked X, this has the same Y"). That is what makes an unexpected pick feel relevant rather than random, and it mirrors the "adjacent novel interest" design.
- [I] Counter the promotional register: require one honest caveat per place (crowds, touts or scams, best/worst time, "skip if..."). This addresses the documented positivity and cliché bias and the Instagram expectation gap.
- [I] "Classic ≠ bad." Many first-time-in-city requests are best served by a classic plus timing advice (go early, go via the back route). The anchor slot covers this.

### Gaps
- No measured popularity-bias audit of LLM POI recommendations in Asian cities (Kathmandu etc.) or Russian-language prompts was found. The best POI-level audit is US-only.
- No study was found comparing explicit novelty quotas vs calibration in LLM conversational travel recommendation with real users.

---

## Q6. LLM itinerary and route planning: benchmarks, failure modes, mitigations

### Takeaway
Unaided LLMs remain poor at full, feasible itineraries.
- GPT-4 passed 0.6% of plans on TravelPlanner (2024).
- On TripTailor (2025), fewer than 10% of LLM itineraries reached human level.
- A 2026 re-analysis finds plan generation success of about 0.43 on TravelPlanner and about 0.15 on TripCraft for the best model.
- Error self-correction is very weak (about 0.03–0.14), and models over-flag valid steps as errors.

Recurring failures are hallucinated places and logistics, temporal inconsistency that grows with trip complexity, detours and poor routing, and confusion of POI types and transport. What works: grounding to real candidate lists (it removes fabrication), external tools and solvers for hard constraints (about 94% vs 10% pass rate), cluster-then-route spatial decomposition, and explicit time accounting. LLM self-critique alone is not enough.

### Cited Findings
- **TravelPlanner.** GPT-4 achieved a 0.6% final pass rate. [S; ICML 2024; foundational benchmark] — [Xie et al., arXiv 2402.01622](https://arxiv.org/abs/2402.01622)
- **LLM + SMT solver.** With all information supplied, the best plain LLM (o1-preview) found viable plans only about 10% of the time. LLM-Modulo with external verifiers reached 20% (GPT-4-Turbo) and 65% (o1-preview). Translating constraints into an SMT solver reached a **93.9% test pass rate** (Claude 3 Opus), and 86.7% with paraphrased prompts. [S; NAACL 2025] — [Hao et al.](https://aclanthology.org/2025.naacl-long.176/)
- **TripTailor.** Over 500,000 real POIs and about 4,000 real itineraries. Fewer than 10% of state-of-the-art LLM itineraries reached human-level performance. Failures: confusing attractions, hotels and restaurants; misapplying transport; unnecessary detours and unoptimized routes. [S/M; ACL Findings 2025] — [TripTailor](https://aclanthology.org/2025.findings-acl.503/)
- **Revisiting LLM travel planning (2026), which decomposes the task.**
  - Constraint extraction: near-saturated on TravelPlanner (F1 0.98), but weak on text-valued and negated constraints such as room type, house rules and transport.
  - Plan generation success: about 0.43 at best on TravelPlanner, about 0.15 on TripCraft. Models show a POI-selection bias.
  - Error identification: high recall, low precision. Models over-report valid steps as violations.
  - Error correction: 0.03–0.14, and models repeat the same errors after being told about them.
  - Supplying better POI selections raised success from 0 to 0.49 on a subset.
  - The authors conclude self-verification alone is unlikely to suffice.

  [M; preprint, May 2026; Gemini 3 Pro and others] — [Zhang et al., arXiv 2605.03308](https://arxiv.org/html/2605.03308v1)
- **Temporal inconsistency grows with complexity.** All models show significant temporal inconsistency, rising with itinerary complexity, and some models had travel-time violations in every itinerary. A guardrail validator and corrector is proposed. [M; preprint, Oct 2025] — [Iti-Validator, arXiv 2510.24719](https://arxiv.org/pdf/2510.24719)
- **TripCraft** adds real transit schedules, events, attraction categories and personas, and replaces pass/fail with continuous temporal, spatial, ordering and persona scores. A "parameter-informed" setting raised the Temporal Meal Score from 61% to 80% on 7-day plans. [M; preprint, Feb 2025] — [TripCraft, arXiv 2502.20508](https://arxiv.org/abs/2502.20508)
- **ItiNera** (an industry system for open-domain urban itineraries) decomposes the request, selects candidate POIs, applies cluster-aware spatial optimization (hierarchical TSP), and only then has the LLM write the itinerary. It reported 31.4% recall vs 18.4% for GPT-4 with chain-of-thought (Shanghai data, as reported in a review). [M; EMNLP 2024 Industry] — [ItiNera, ACL Anthology](https://aclanthology.org/2024.emnlp-industry.104); [code](https://github.com/YihongT/ITINERA)
- **Grounding removes invented venues but not invisibility.** Open-ended prompting produced 36.8% non-existent restaurants; a supplied candidate list brought this to about 0%. [M/S] — [arXiv 2607.06260](https://arxiv.org/html/2607.06260)
- **Hallucinated POI locations** were a key complaint in the GPT-4 itinerary user study. The recommended fix is districts → time slots → POIs per district, with explicit travel times and transport options shown. [W] — [González-Sanz et al., RecTour 2025](https://ceur-ws.org/Vol-4052/paper6.pdf)
- **Users reporting non-existent attractions** appear as a travel-app failure category in a study of user-reported LLM hallucinations in app reviews. [M] — [Scientific Reports 2025](https://www.nature.com/articles/s41598-025-15416-8.pdf)
- **TRACE** (10,000 dialogues, 2,400 Yelp POIs, 8 US cities) requires each tourism recommendation to cite verbatim review evidence and to recover after the user rejects a suggestion. No approach led on accuracy, grounding and recovery at once (the "Three-Competency Gap"). Zero-shot LLMs led on accuracy and recovery but cited evidence less densely. [M; preprint, May 2026] — [TRACE, arXiv 2605.07677](https://arxiv.org/abs/2605.07677)
- **Map-grounding vendor claim.** Google's Maps Platform says grounding in Maps data reduces hallucinations and stale references. [W; vendor marketing, no independent test found] — [Google Maps Platform blog](https://mapsplatform.google.com/resources/blog/powering-the-next-era-of-agentic-experiences-announcing-new-grounding-capabilities/)

### Inferences
- [I] **For a Claude mobile guide without custom code:**
  - (1) Never name a specific venue from memory alone when a web or maps search tool is available. Retrieve candidates first, then choose. This is the "candidate-constrained" mode that eliminated fabrication.
  - (2) For multi-stop days: cluster by area, order the clusters, then pick stops, and write out each leg's walking or transit time and each stop's opening hours.
  - (3) Do arithmetic explicitly, with a code tool if available, for total time and budget.
  - (4) Run a final constraint checklist against hard constraints and deal-breakers instead of asking the model to "double-check": self-correction is weak and over-flags.
  - (5) When unsure about hours or existence, say so and give a quick verification step ("check that it's open before going").
- [I] **Walks and routes:** LLMs are weakest at spatial and temporal feasibility. State realistic distances and durations with a buffer, and prefer loops or one-directional routes within one cluster.
- [I] **Quick repair after rejection** (TRACE): a contrasting alternative that names the critique dimension ("not that touristy: here's a quieter one 10 min away").

### Gaps
- No 2025–2026 benchmark covering Kathmandu, Nepal or Russian cities was found. Data coverage outside the US, China and Europe is likely thinner, and the restaurant audit showed hallucination rises where digital footprints are sparse.
- Walking-route quality (pleasantness, safety, slopes) has no LLM benchmark that I found.

---

## Q7. Low-friction feedback after visits, and how to use ratings to update the profile

### Takeaway
There is little direct 2024–2026 research on post-visit feedback loops in LLM travel agents. Adjacent evidence gives clear design principles:
- Remembered experience, not anticipation and not even in-the-moment feeling, predicts whether someone wants to repeat. A brief "how was it?" captured after the visit is the right signal for future recommendations.
- Anticipation and imagery are systematically rosier than experience, so appeal and intent signals must not be read as enjoyment.
- Explicit, context-rich textual feedback is argued to align better with true preferences than implicit logs.
- Memory writes from feedback should be gated and scoped, because over-generalizing a single experience into a rule is a documented failure.

### Cited Findings
- Remembered experience directly predicted desire to repeat a vacation. Anticipated and in-the-moment experience did not. Predicted and remembered experiences were more extreme than real-time ratings. [F; Psychological Science 2003] — [Wirtz et al.](https://worlddatabaseofhappiness.eur.nl/publications/what-to-do-on-spring-break-the-role-of-predicted-on-line-and-remembered-experience-in-future-choice-4365/)
- The "rosy view": anticipation and retrospection of trips exceed the experience itself. People may choose trips partly for anticipation and recollection. [F; 1997] — [APS Observer](https://www.psychologicalscience.org/observer/vacation-not-what-you-remember)
- Idealized social imagery (influencer content) omits crowds and safety issues that appear in visitor reports, and "hidden spot" content can disappoint. [W] — [Soares 2025](https://ideas.repec.org/h/spr/prbchp/978-3-031-83705-0_24.html). Congruence between projected and perceived destination images reduces the gap between expectation and reality, which affects satisfaction. [W] — [Springer, Saalbach-Hinterglemm Instagram study](https://link.springer.com/10.1007/978-3-030-94751-4_31)
- Explicit, context-rich feedback is argued to be necessary for LLM recommenders to align with users' true preferences. [W; preprint 2026] — [arXiv 2605.29141](https://arxiv.org/html/2605.29141v1)
- Users preferred feeds built on stated preferences over behaviour-based ones once the gap was made visible. [M] — [ACM 10.1145/3817029](https://dl.acm.org/doi/10.1145/3817029)
- Status promotion and scope broadening make a single committed claim contaminate later, unrelated recommendations. [M/S] — [arXiv 2607.10526](https://arxiv.org/html/2607.10526v3)
- Recovering from rejection is a separate competency that needs evaluating. [M] — [TRACE](https://arxiv.org/abs/2605.07677)

### Inferences
- [I] **Feedback timing:** ask at the next natural touchpoint, such as the next time he opens a chat or asks for something nearby, rather than with a push mid-visit. Make it one tap or one short voice phrase: "How was X: great / ok / not for me? One word why?" This captures remembered experience at low effort.
- [I] **Attribution:** when the experience was bad, ask or infer whether the cause was the place (taste) or the context (rain, exhaustion, crowds at noon, bad company fit). Only taste-caused negatives update durable taste. Context-caused ones become context rules ("avoid Durbar Square at midday").
- [I] **Three-signal ledger per place:**
  - appeal (from photos or saves) → raises exploration priority;
  - intent ("want to go") → enters a wishlist with no taste inference;
  - experience (after the visit) → the only signal allowed to update taste weights.
- [I] **Update rule:** one strong experience creates a *hypothesis* line tagged `[1 visit]`. Two or more consistent experiences, or an explicit general statement, promote it to durable taste. A contradicting newer experience supersedes the line with a date (HorizonBench and LongMemEval knowledge-update lessons).
- [I] Periodically, for example at the start of a new trip, show 3–5 profile lines and ask "still true?". This is cheap drift control and matches the scrutability findings.

### Gaps
- No 2024–2026 study was found on post-visit feedback UX for LLM travel assistants, or on how many feedback prompts users tolerate.
- No empirical work was found that operationalizes the appeal / intent / experience split in POI recommenders. It rests on psychology and tourism-marketing studies, mostly older or small.

---

## Synthesis: actionable heuristics for a prompt + text-profile travel guide (Claude mobile, voice, Russian-speaking frequent traveller)

### Takeaway
A prompt-and-file system can capture most of the evidence-backed gains:
- an explicit ask-or-act rule with a 0–1 question budget on the go and a short funnel for trip planning;
- "ask by showing" contrasting options;
- a profile split into durable taste, hard deal-breakers, expiring situational constraints and a three-signal places log with provenance and dates;
- deliberate slate composition against the LLM's mainstream bias;
- tool-grounded, cluster-then-route itineraries with explicit time arithmetic and a final constraint checklist.

### Cited Findings (heuristics, each with its basis and evidence strength)

**A. Ask or act**
1. **Default to acting. Ask at most one question on the go.** Before asking, privately list 2–3 plausible interpretations. Ask only if the best recommendation differs between them, and then ask the single question that separates them. Never ask what the profile, the message, the clock or a tool already answers. — Basis: EVPI stopping rule ([SAGE-Agent](https://arxiv.org/html/2511.08798v2), M); 1–3 question budgets keep 86–94% of value at 36–73% less attention cost, and checking memory first saves another 13% ([Ask Less, Ask Better](https://arxiv.org/abs/2610.24411), M); over-clarification taxonomy ([LHAW](https://arxiv.org/pdf/2602.10525), M).
2. **Ask by showing.** When unsure, give 2–3 contrasting options that span the main uncertainty (classic vs offbeat, calm vs lively, near vs worth-the-trip), each with a one-line "why for you". His pick or critique is the clarification. — Basis: item-centred elicitation beats abstract questions ([COLING 2025](https://aclanthology.org/2025.coling-main.561.pdf), M); interactive elicitation takes less effort ([GATE, ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9867d5a22653ce98b02595061e40f12-Paper-Conference.pdf), M); diversity reduces choice overload ([Bollen et al. 2010](https://dblp1.uni-trier.de/rec/conf/recsys/BollenKWG10.html), F). The format itself is [I].
3. **Planning mode: a short funnel interview of 3–5 questions, broad to specific, starting with examples.** "1–3 places from past trips you loved, 1 you regretted" → pace (relaxed / balanced / intensive) → mainstream-vs-offbeat appetite → company and budget → must-sees. Skip anything already in the profile. — Basis: funnel ordering ([Google, arXiv 2510.12015](https://arxiv.org/html/2510.12015v1), M/W); item-centred questions ([COLING 2025](https://aclanthology.org/2025.coling-main.561.pdf), M); travel-style parameter ([RecTour 2025](https://ceur-ws.org/Vol-4052/paper6.pdf), W).
4. **Keep a running hypothesis after each answer.** Restate the current best guess in one line ("So far: half-day, low effort, nature, solo") before the next question or recommendation. Don't rely on generic "think step by step". — Basis: Incremental Prediction and Aggregate Context fixed the round-over-round degradation, while zero-shot CoT hurt ([COLING 2025](https://aclanthology.org/2025.coling-main.561.pdf), M).
5. **After clarifying, show what was checked.** End recommendations with a compact fit line ("fits: ≤30 min round trip · open now · not crowded at this hour"), especially for constraints the user just gave. — Basis: clarifying questions increased acceptance of erroneous answers in exactly the clarified areas ([Is That Clear?, N=180](https://arxiv.org/html/2611.01087), M).

**B. Elicitation formats and voice**
6. **Three options maximum in voice. Put the most personalized or diverse one first.** Voice users pick among the first options and lean popular, so when the exploration dial is high, the novel option should not come last. — Basis: [Yang et al., RecSys 2018 (N=100)](https://tech.cornell.edu/news/study-smart-speakers-make-passive-listeners) (F); summarize-and-refine ([Winterboer & Moore](https://era.ed.ac.uk/bitstreams/fe1279df-b2c1-4877-ae12-ffdefb0b51a0/download), F).
7. **Treat critiques as first-class signals.** "Too touristy / too far / too expensive / more nature" → immediately offer a contrasting alternative along that dimension and log the critique dimension (not the place) as a candidate preference. — Basis: critiquing paradigm ([Chen & Pu](https://infoscience.epfl.ch/record/176775), F); NL critiques improve recommendations ([REGEN](https://arxiv.org/html/2503.11924v1), M/W); rejection recovery ([TRACE](https://arxiv.org/abs/2605.07677), M).
8. **Photos he shares or likes are appeal signals only.** Log them under `appeal`, never as `liked` or `visited`. Use them to choose what to propose, not to infer enjoyment. — Basis: picture-based elicitation captures emotional attraction ([PicTouRe](https://ar5iv.arxiv.org/html/2006.05172), F/W); anticipation is rosier than experience ([rosy view](https://www.psychologicalscience.org/observer/vacation-not-what-you-remember), F); Instagram expectation gap ([Soares 2025](https://ideas.repec.org/h/spr/prbchp/978-3-031-83705-0_24.html), W).
9. **Store an interaction-style field** (wants one confident pick vs a menu; short vs explained; how much control). — Basis: five distinct style clusters, with control preference as a moderator ([OZCHI 2025, N=139](https://arxiv.org/abs/2508.02328), W/M).

**C. Situational state**
10. **Keep a 6-slot state with defaults: time budget, energy, intent/mood, company, weather/daylight, location.** Infer from the message, the local time and a weather tool. If one slot dominates and is unknown (usually time or energy), ask one combined question ("How much time, and walk a lot or take it easy?"). Fold mood into the contrasting options rather than asking about it. — Basis: CARS factors and LLM itinerary guidelines on weather, events and crowds ([RecTour 2025](https://ceur-ws.org/Vol-4052/paper6.pdf), W; [mood/budget/companion CARS](https://www.researchgate.net/publication/390744434_A_Personalized_Context-Aware_Places_of_Interest_Recommender_System), W); context plus calibration works best ([Forster et al., RecSys 2025](https://arxiv.org/abs/2507.03503), M). Slot design is [I].
11. **State shifts the novelty mix.** Low energy, little time, bad weather or first hours in a new city → more familiar, close, low-risk options. A free day with high energy → more novelty and distance. — Basis: per-user, per-context popularity calibration ([Forster et al.](https://arxiv.org/abs/2507.03503), M). The direction of the mapping is [I].
12. **Per-trip and per-day constraints live in an expiring "Now / This trip" block** (e.g. "only 30 min today", "with friend X until Fri"), with an expiry date, and never get merged into durable taste. — Basis: status promotion (51.4%) and scope broadening drive persistent errors ([arXiv 2607.10526](https://arxiv.org/html/2607.10526v3), M/S).

**D. Profile and memory (text file)**
13. **Profile layout:**
    - (1) Hard no's / deal-breakers.
    - (2) Taste summary of 10–20 lines.
    - (3) Exploration dial and popularity appetite.
    - (4) Interaction style.
    - (5) Now / This trip block with expiry.
    - (6) Places log with `appeal | intent | visited(date, context) | experience(rating + why) | would_return`.
    - (7) Change log.

    Load (1)–(5) every session; consult (6) as needed. — Basis: preference following collapses in long context ([PrefEval, ICLR 2025](https://arxiv.org/html/2502.09597v1), S); linked and consolidated memory beats raw dialogue retrieval ([PERMA](https://arxiv.org/abs/2603.23231), M); concise editable NL profiles are scrutable and effective ([UPR, ACL 2024](https://aclanthology.org/2024.acl-long.753.pdf), M; [music survey](https://arxiv.org/html/2511.16478v3)).
14. **Tag every durable line with source, date and confidence**, for example `[said 2026-10-12]`, `[inferred: 3 visits]`, `[guess - confirm]`. Keep the scope explicit (e.g. "in hot weather", "in Moscow"). — Basis: source, status and scope preservation and scope-aware retrieval ([arXiv 2607.10526](https://arxiv.org/html/2607.10526v3), M/S).
15. **Commit gating.** Promote to durable taste only on an explicit general statement or at least 2 consistent experiences. Single events go to the log as hypotheses. Read back the diff to him in one line for confirmation. — Basis: L1 and L2 commit gating ([arXiv 2607.10526](https://arxiv.org/html/2607.10526v3)); users may not identify with generated profiles ([arXiv 2507.16708](https://awesomepapers.io/recommender-systems/papers/2507.16708), W).
16. **Supersede, don't append.** When new evidence conflicts, mark the old line `superseded YYYY-MM-DD` and prefer the newer one. At the start of each new trip, run a 3–5 line "still true?" check. — Basis: belief-update failure, where over a third of errors revert to the original value ([HorizonBench](https://arxiv.org/abs/2604.17283), M); knowledge updates are among the hardest memory tasks ([LongMemEval](https://www.emergentmind.com/topics/longmemeval), S).
17. **Not visited means unknown, not disliked. Skipped-because-of-context is not rejected.** Only explicit taste rejections or bad experiences attributed to the place count as negatives. — Basis: MNAR and exposure bias ([Saito et al.](https://alphaxiv.org/abs/1909.03601), F/M; [BISER](https://research.google/pubs/bilateral-self-unbiased-recommender-learning-for-missing-not-at-random-implicit-feedback/)).
18. **Explicitly check deal-breakers before sending.** "Knowing" a preference does not mean the model acts on it. Add a final instruction: "Before answering, check each option against Hard no's and the Now block; drop or flag violations." — Basis: Know-vs-Act gap ([arXiv 2607.29433](https://arxiv.org/abs/2607.29433), M); [PrefEval](https://arxiv.org/html/2502.09597v1) (S).

**E. Familiar vs novel**
19. **Assume the default is mainstream and counter-steer with slate composition.** For 3 options: anchor (a classic or proven type), adjacent (a lesser-known place sharing a loved attribute), wildcard (unexpected, linked to a stated value). Tilt by the exploration dial and current state (heuristic 11). — Basis: Japan for 89% of personas ([Destination (Un)Known](https://doi.org/10.3390/ai6090236), M); 96.8% of real venues invisible, selection driven by visits and reviews rather than rating ([arXiv 2607.06260](https://arxiv.org/html/2607.06260), M/S); LLM-proposed adjacent novel interests raised exploration and enjoyment in live tests ([Google, arXiv 2405.16363](https://arxiv.org/abs/2405.16363), M/S); calibration ([RecSys 2025](https://arxiv.org/abs/2507.03503), M). The 1/1/1 split is [I].
20. **Every novel pick needs a bridge sentence** ("because you loved X, this has the same Y"). Serendipity = unexpected + relevant. — Basis: adjacent-interest design ([Google](https://arxiv.org/abs/2405.16363)); serendipity alignment ([SOLAR](https://aclanthology.org/2025.findings-emnlp.538.pdf), M). The bridge as a prompt rule is [I].
21. **Learn his popularity appetite from outcomes, not from a fixed quota.** Track in the profile how often offbeat vs classic picks were accepted and enjoyed, and adjust the dial. — Basis: calibration to the individual's popularity profile ([Forster et al.](https://arxiv.org/abs/2507.03503), M).
22. **One honest caveat per place** (crowds or timing, touts or scams, "skip if..."), and plain language instead of superlatives. — Basis: promotional, cliché-dense LLM register ([Destination (Un)Known](https://doi.org/10.3390/ai6090236), M); positivity bias in 67.9% of recommendations ([socio-technical study](https://www.researchgate.net/publication/403507624_A_socio-technical_exploration_of_bias_in_generative_AI_travel_planners), W); idealized imagery causes disappointment ([Soares 2025](https://ideas.repec.org/h/spr/prbchp/978-3-031-83705-0_24.html), W).

**F. Itineraries and routes**
23. **Retrieve before recommending.** Use search or maps tools to confirm that each named place exists, its location and its current hours. If unverifiable, say so. — Basis: 36.8% fabricated venues open-ended vs about 0% with a candidate list ([arXiv 2607.06260](https://arxiv.org/html/2607.06260), M/S); POI location hallucinations ([RecTour 2025](https://ceur-ws.org/Vol-4052/paper6.pdf), W).
24. **Cluster → schedule → fill.** Group by area, assign areas to time slots using opening hours and travel times, then choose stops within each area, avoiding back-and-forth. — Basis: [ItiNera](https://aclanthology.org/2024.emnlp-industry.104) (M); detours in LLM plans ([TripTailor](https://aclanthology.org/2025.findings-acl.503/), S/M); 3-step guideline ([RecTour 2025](https://ceur-ws.org/Vol-4052/paper6.pdf), W).
25. **Write out the time arithmetic** (walk or ride minutes + visit minutes + buffer) and total it against the time budget. Use a code tool for multi-day plans or budgets. — Basis: temporal inconsistency grows with complexity ([Iti-Validator](https://arxiv.org/pdf/2510.24719), M); time coherence was the lowest-rated aspect ([RecTour 2025](https://ceur-ws.org/Vol-4052/paper6.pdf), W); solvers vs LLM-only, about 94% vs 10% ([Hao et al., NAACL 2025](https://aclanthology.org/2025.naacl-long.176/), S).
26. **Final hard-constraint checklist instead of "please double-check".** Self-correction succeeds only 3–14% of the time and over-flags valid steps, so run an explicit checklist on budget, time windows, deal-breakers and opening hours. — Basis: [Revisiting travel planning, arXiv 2605.03308](https://arxiv.org/html/2605.03308v1) (M); [TravelPlanner](https://arxiv.org/abs/2402.01622) (S).

**G. Feedback loop**
27. **Ask "how was X?" at the next touchpoint, in one tap or one word** (great / ok / not for me + an optional why). This captures remembered experience, the signal that predicts repeat choice. — Basis: [Wirtz et al. 2003](https://worlddatabaseofhappiness.eur.nl/publications/what-to-do-on-spring-break-the-role-of-predicted-on-line-and-remembered-experience-in-future-choice-4365/) (F); explicit feedback argument ([arXiv 2605.29141](https://arxiv.org/html/2605.29141v1), W). The timing is [I].
28. **Attribute before updating.** Was a bad experience caused by the place type (update taste) or by context (create a context rule, e.g. "avoid midday heat at open squares")? Only experience signals update taste. Appeal and intent never do. — Basis: [I] built on the CARS and MNAR evidence above and the stated-vs-revealed gap ([ACM 10.1145/3817029](https://dl.acm.org/doi/10.1145/3817029), M).

### Inferences
- [I] The strongest evidence (S) supports four heuristics: always-in-context concise profiles (PrefEval, LongMemEval), external grounding and solver-style verification for itineraries (TravelPlanner, Hao et al., TripTailor), the size of popularity and hallucination bias (destination and POI audits), and tight question budgets (multiple 2025–2026 papers, though mostly with simulated users).
- [I] The weakest-supported heuristics are elicitation of mood and energy, post-visit feedback UX, and the exact anchor/adjacent/wildcard split. They are reasonable engineering choices but should be validated with the user's own feedback over the first trips.
- [I] For this specific user (voice, on the go, Kathmandu/Moscow), heuristics 1, 2, 6, 10, 12, 19 and 23 carry the most day-to-day value. Heuristics 3 and 24–26 matter in multi-day planning mode.

### Gaps
- No study was found of Russian-language or bilingual LLM travel recommendation quality, or of popularity or hallucination bias for Nepal or South Asia. Bias and hallucination may be worse there, since hallucination rises where digital footprints are sparse ([arXiv 2607.06260](https://arxiv.org/html/2607.06260)), but this is untested.
- No head-to-head human study was found comparing elicitation formats (pairwise vs 1-of-3 vs open "vibe" vs photo) for LLM travel recommendation.
- Several key 2026 results (Ask Less, Ask Better; Is That Clear?; HorizonBench; persistent sycophancy; Know It, Act on It) are recent preprints without peer review or replication.
- Could not access: the full text of the ACM 2026 elicitation-strategy comparison ([10.1145/3774935.3803059](https://dl.acm.org/doi/10.1145/3774935.3803059)); ItiNera's user-owned-POI features; Google Maps grounding effect sizes (only a vendor claim exists).
