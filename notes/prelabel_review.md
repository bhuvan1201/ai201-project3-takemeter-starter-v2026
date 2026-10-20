# AI pre-label review — historical suggestions

## Final user decision

The user accepted all 150 AI-suggested labels, retained candidates 122 and 188 as `opinion`, and chose to proceed with 172 labeled posts under the time-limit fallback. `labels.csv` now contains only those 172 posts; `excluded_posts.csv` preserves the remaining 28 with their text, source links and exclusion reasons. All 20 cold labels are preserved. AI-prelabel provenance remains recorded.

The sections below preserve the earlier AI review and its suggestions; pending-review wording below describes that earlier state, not current outstanding work. Candidate IDs below are original 1–200 identifiers, not current spreadsheet row numbers. Current counts are question 89, opinion 67, proposal 12, experience 4. README contains the final dataset write-up and three hard cases.


All 200 candidates were read as title plus full body against the README taxonomy. This review classifies author purpose, not factual accuracy. Linked media and current source availability were not independently verified.

The user labeled candidates 1–20 before this pass. Their labels are unchanged and the original first 20 records are preserved in `cold_labels_first20.csv`. This was not an independent blind agreement test: the AI could see those labels.

Candidates 21–200 received 150 AI-suggested labels and 30 proposed exclusions. The user subsequently classified candidates 122 and 188 as `opinion`, overriding the proposed exclusions. The other 150 AI-suggested labels still need human review; 28 proposed exclusions remain. An empty label now means a proposed exclusion, explained in the note; it is not an unfinished AI classification.

`labels.csv` is now the working review file: at the user’s request, `labels_review.csv` replaced it. It retains all 200 candidates in original order, full text and source notes. Two empty export columns were removed. The older `labels_review.xlsx` is stale; do not overwrite the CSV from it.

Candidate numbers below exclude the header. Spreadsheet row = candidate number + 1. Each post may occupy several physical lines in a text editor.

## Provisional counts

| Label | Count | Share of 172 labeled candidates |
|---|---:|---:|
| question | 89 | 51.7% |
| opinion | 67 | 39.0% |
| proposal | 12 | 7.0% |
| experience | 4 | 2.3% |
| **Total labeled** | **172** | **100%** |

28 candidates remain proposed for exclusion. If accepted, reaching 200 usable posts requires at least 28 replacements. The 20–40% balance criterion is still not met. Collect more proposals and experiences; do not change labels to meet a quota. Twenty-eight replacements alone cannot bring experiences to 20% of a final 200-post set.

## User review decisions

- Candidate 122: user selected `opinion`, overriding the AI exclusion suggestion.
- Candidate 188: user selected `opinion`, overriding the AI exclusion suggestion.

The original AI exclusion reasons remain in each CSV note for the review history.

## Your first 20: discussion points, no label changes

- Candidate 2: kept `question`. The body develops extensive judgments of teams and drivers; `opinion` is a plausible alternative under the main-body rule. Decide whether the open request or the developed assessment dominates.
- Candidate 17: kept `opinion`. I would suggest `question`: the author explicitly asks why people are confident in Audi and does not develop their own answer. You make the final decision.
- Candidate 18: kept `opinion`. This mixes a specific rewatch experience with judgments about the broadcast; `experience` is a plausible alternative. Compare with the experience/opinion boundary.

## Proposed exclusions

Keep these rows in the review record until you confirm or reject each scope decision. They have blank labels, not a new fifth training label.

| Candidate | Title | Reason |
|---:|---|---|
| 24 | Jennie Gow, Andrew Benson, Jolyon Palmer, and Jack Nicholls discuss the Max-Checo incident in Brazil in their 2022 season review on the BBC Chequered Flag podcast | Mainly transcribes other people's podcast discussion; the brief endorsement does not make this the author's own opinion post. |
| 31 | With the latest edition of the ISC, it is now considered a breach of the rules to 'make and display any political, religious and personal statements or comments that violate the general principle of neutrality promoted by the FIA under its Statutes.' | Reports and quotes rule changes without the author's own judgment, request, proposal or personal account. |
| 36 | The most recent podium with drivers not anymore with us - Portugal 1985 (Photo credit: Classic team Lotus) | Factual historical photo caption, without one of the four author purposes. |
| 54 | FREE Q&A with professional Formula 1 Photographers! | Promotional event announcement and registration link, rather than a taxonomy-purpose discussion. |
| 79 | Meta Discussion Thread - Post 2022 Edition | Recurring moderator meta-discussion thread, outside the dataset scope. |
| 88 | Red Bull Touge? | Mainly shares an external filming link with a brief reaction; insufficient standalone text for the scoped dataset. |
| 98 | Formula 1 2022 Championship standings if they were based purely on race pace | Describes a calculation and links its results without a substantive judgment, proposal, request or personal fan event. |
| 111 | The 2022 /r/Formula1 Flair Championship - Round 22 - Abu Dhabi | Recurring subreddit flair-statistics report, outside the four-purpose scope. |
| 123 | There has only been 1 driver to ever have an official fastest lap who has never scored a point. Meet Brian Henton. | Mainly narrates another driver's historical career and statistic, not the author's personal experience or a central argument. |
| 133 | The 2022 season ends the streak of German drivers earning at least one podium in each of the previous 30 consecutive seasons. (1992-2021) | Mainly reports a historical statistical streak with a season-by-season list; a brief reaction is secondary. |
| 134 | The 2022 r/formula1 census | Recurring community census announcement rather than a scoped author-purpose post. |
| 135 | 2022 F1 drivers anagrams | Creative wordplay list, with no question, proposal, personal experience or judgment. |
| 137 | Evolution of cumulative points over the season expressed as a percentage of the championship leader (WDC and WCC). | Image-based data display with only a descriptive caption. |
| 140 | The winner of the 2022 F1 Driver’s Championship but you can’t win it more than once is… George Russell! | Reports a novelty standings calculation, without advocating the rule or making a substantive judgment. |
| 145 | Alonso is 2022 Overtakes Champion with 71 Overtakes this Season. Abu Dhabi GP had 79 Overtakes. Full Data in Post. | Mainly reports overtaking counts and methodology; isolated comments do not change the data-report purpose. |
| 154 | F1 2022 Elimination Championship: Round 22 (Abu Dhabi Grand Prix) | Recurring fictional elimination-championship results; narrative questions are not a central request or real rule proposal. |
| 158 | Weeked Warm-up Pundit Prediction final standings | Mainly reports pundit-prediction tables and computed standings; review_required: includes brief interpretations but the statistical report dominates. |
| 161 | A Letter from Daniel - DR’s letter sent to fans | Reproduces a driver's letter; its first-person experiences belong to the quoted driver, not the Reddit author. |
| 166 | Max may not have beaten Merc but… | Reports a points comparison without a substantive author judgment. |
| 167 | How the final constructor's championship shaped up compared to Sky Sports predictions | Displays actual standings against published predictions without an author argument. |
| 172 | For the first time in F1 history, the podium placings in the final race of the season reflect its final WDC standings | Reports a podium-versus-championship statistic. |
| 174 | Charles Leclerc and Sergio Pérez are the first Monégasque and Mexican drivers, respectively, to finish in the WDC top 3 | Reports nationality and championship-placement milestones. |
| 183 | Qualifying battles 2022 revisited: comparing gaps per race | Image and comparison links without substantive standalone text. |
| 195 | Will any of the outgoing drivers score points at the Abu Dhabi GP? | Recurring Predictions Tournament poll using a standard announcement template. |
| 196 | Who will finish 2nd in the Drivers' Championship? | Recurring Predictions Tournament poll using a standard announcement template. |
| 197 | Who will finish 2nd in the Constructors' Championship? | Recurring Predictions Tournament poll using a standard announcement template. |
| 198 | Who will win the Abu Dhabi GP? | Recurring Predictions Tournament poll using a standard announcement template. |
| 199 | Who will start in Pole Position for the Abu Dhabi GP? | Recurring Predictions Tournament poll using a standard announcement template. |

## Ambiguous AI labels to review first

These are priorities, not the only rows requiring review. Every AI-labeled row has a short reason in its note.

| Candidate | Suggested label | Boundary or reason |
|---:|---|---|
| 23 | question | Asks whether the damper would work and invites technical correction; alternative=proposal because the body suggests fitting dampers. |
| 27 | opinion | Develops the author's counterfactual interpretation of numbering history; alternative=proposal, but no present-day adoption is clearly requested. |
| 32 | opinion | Develops the view that downsizing F1 engines has negligible climate impact; alternative=question because the title asks why. |
| 33 | proposal | Specifies indefinite accumulation and changes to penalty points; review_required: opening update retracts the original proposal, making the final stance mixed. |
| 37 | question | The purchase experience explains a request for customer-service help; alternative=experience. |
| 40 | opinion | Interprets bankruptcy filings to infer Mercedes may be owed money; review_required: close to a factual news report, but the author adds their own inference. |
| 49 | opinion | Develops a personal ideal-grid wish list; alternative=question because it also invites readers' lists, and proposal because it imagines team changes. |
| 55 | question | Provides news context then explicitly requests predictions for vacant roles; review_required: most of the body is a news roundup. |
| 56 | question | Asks how the appointment will affect driver treatment; alternative=opinion because it includes speculation about Sainz. |
| 58 | opinion | Develops the author's race preferences and supporting reasons; alternative=question because readers are also invited to name favourites. |
| 63 | question | Asks why footage is absent without supplying a settled explanation; alternative=opinion because the omission is criticised. |
| 70 | question | Quotes someone else's sprint proposal to solicit views while withholding endorsement; alternative=proposal, but the quoted speaker is not the author. |
| 73 | opinion | Interprets a simulation and concludes extra points are not really worthwhile; alternative=proposal because a concrete alternative is explored. |
| 74 | proposal | Lays out a specific DRS rule change for consideration; alternative=question because the title asks if it works. |
| 75 | experience | Tells a personal near-miss story around acquaintances meeting drivers; review_required: the actual meetings are second-hand, so check the personal-event scope. |
| 78 | proposal | Advocates points for every finisher through rhetorical questions and a consistency argument; alternative=question. |
| 81 | question | Describes a wrong order to ask for help with contacting the shop; alternative=experience. |
| 84 | question | Explicitly withholds a full verdict and asks other readers for their assessment; alternative=opinion because it includes initial impressions. |
| 87 | proposal | Advocates retaining combustion engines using hydrogen or alternative fuel; alternative=question because feasibility is also raised. |
| 89 | opinion | Explains a preference for clearer year-based car names; alternative=proposal because it asks teams to name cars differently, or question because it invites shared difficulties. |
| 94 | proposal | Endorses a specific regional schedule and championship-points scheme; review_required: most wording is attributed to another person's comment. |
| 96 | opinion | Uses a rewatch to argue an alternative cause of Hamilton losing the title; alternative=experience. |
| 97 | opinion | Argues Kolles would be suitable under a cost cap; alternative=proposal because hiring him is implied rather than explicitly requested. |
| 103 | opinion | Evaluates multiple candidates and their strengths rather than clearly advocating one appointment; alternative=proposal. |
| 105 | opinion | Uses prices and past attendance to argue the increases are an unjustified money grab; alternative=experience. |
| 108 | opinion | Presents a personal dream calendar as a preference; alternative=proposal, but no adoption is clearly urged. |
| 110 | question | Asks whether a windshield is feasible or likely, without arguing a settled recommendation; alternative=proposal. |
| 112 | question | Asks why reversible tracks are not used and what prevents them; alternative=proposal because the author likes the idea. |
| 113 | opinion | Explains the author's desired Bottas-to-Ferrari move; alternative=question because the title requests readers' choices. |
| 119 | opinion | Interprets overtaking comparisons to argue the regulations' overall effect remains uncertain; review_required: close to a factual data report. |
| 124 | opinion | Uses old broadcasts to argue poor direction is longstanding; alternative=question because it invites counterexamples. |
| 130 | opinion | Interprets poll findings and expresses surprise about the audience overlap; alternative=out_of_scope factual report. |
| 139 | opinion | Interprets the comparison as showing two drivers in their own league; alternative=question because it asks about additional metrics. |
| 143 | opinion | Presents the author's speculative future predictions before inviting others; alternative=question. |
| 146 | question | Requests examples of weak race winners and offers initial candidates; alternative=opinion because Panis is the author's initial favourite. |
| 155 | opinion | Develops the preferred Ricciardo-to-Mercedes scenario and its rationale; alternative=question because it invites other choices. |
| 156 | opinion | Argues why Leclerc's Copse pass should be overtake of the season; alternative=question. |
| 160 | opinion | Develops the author's case that Ocon was underrated; alternative=question because it invites other picks. |
| 163 | opinion | Expresses hopes for Mercedes and Hamilton and assesses his motivation; alternative=question because it invites predictions. |
| 168 | opinion | Uses broken streaks to argue Alonso deserved better and was faster than Ocon; alternative=question or factual report. |
| 173 | opinion | Interprets statistical streaks as non-coincidental; review_required: very thin judgment attached to a statistical report, possibly out of scope. |
| 177 | opinion | Argues about the points system and then revises that judgment in an edit; alternative=question, but no concrete replacement rule is proposed. |
| 179 | opinion | Interprets telemetry to attribute time loss to braking and tyre overheating; review_required: mixed technical data report and promotional material. |
| 187 | opinion | States and explains a mixed but positive assessment of the regulations; alternative=question because it invites other assessments. |
| 190 | proposal | Calls for more challenging interviews and lists specific questions to implement that approach; alternative=opinion because much of the body criticises journalism. |
| 192 | opinion | Interprets driver ages to contrast Haas's strategy with other teams' young foundations; review_required: close to a factual age report. |
| 200 | opinion | Argues that meaningful help for Perez is unlikely and the promise is mostly symbolic; alternative=question. |

## Earlier proposed next steps (superseded by final user decision)

1. Review the suggested labels and exclusions in `labels.csv`; correct labels based on the written taxonomy. For each reviewed AI row, change `needs_human_review` to `human_reviewed`, and record any correction in the note.
2. Resolve the three cold-label discussion points while retaining the original snapshot and recording any revisions.
3. Collect replacement candidates and more proposals/experiences, then review the class balance again.
4. After review, retain only accepted labeled records in `labels.csv`, preserving an exclusion log. Do not train on blank-label rows.
5. Disclose that the first 20 were user cold labels and the remaining labels were AI suggestions reviewed and corrected by the user only when that review has actually happened.
