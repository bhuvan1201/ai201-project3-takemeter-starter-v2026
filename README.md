# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does

TakeMeter is a text-classification project using public posts from r/formula1. It is intended to identify whether a post mainly asks a question, shares an opinion, proposes a change or describes a personal experience. I fine-tuned DistilBERT on 172 labeled posts using the title and body as input, with the model reading up to 128 tokens per post. The first run predicted every test post as `question`, so it is not yet distinguishing all four purposes reliably.

---

## Label Taxonomy

I want to classify what the author is doing in a post. These labels describe the purpose of the post, not whether its claims are true or whether it is a good post. I tried the definitions on [eight practice posts](notes/milestone2.md) and revised two boundary decisions after discussing them with AI.

**Scope:** Public, English-language text posts from r/formula1. Read the title and full original body together, without the comments. Link-only posts, image-only posts, automated threads, and straight news or data reports with none of the four purposes are outside this dataset. Record exclusions rather than forcing them into `opinion`. Mixed posts within this scope should be kept and resolved using the boundary rules.

The examples below are linked real posts with short summaries, not quotations or substitutes for the full text in the eventual dataset. Their labels are proposed assignments for review.

### `question`

**Definition:** Mainly asks readers for information, an explanation, advice, or their views, rather than presenting the author’s own answer.

**Example 1:** [Tyres](https://www.reddit.com/r/formula1/comments/s87q90)

The author asks why hard tyres are used when softer tyres are faster. Their brief introduction about becoming a fan provides background for the question.

**Example 2:** [Monitoring and reinforcing cost cap](https://www.reddit.com/r/formula1/comments/untlgz)

The author asks how spending is monitored and how possible ways around the cap are handled. The post seeks an explanation of enforcement.

### `proposal`

**Definition:** Mainly recommends a specific action or change that the author wants someone to make.

**Example 1:** [Regarding sprint races](https://www.reddit.com/r/formula1/comments/1psctbj)

The author suggests putting sprint races earlier in the season, arguing that teams would have less reason to protect their cars. The scheduling change is the proposal; its reasoning does not have to be proven for this label.

**Example 2:** [Tire Compound Differences?](https://www.reddit.com/r/formula1/comments/yhrj8a)

The author argues that the performance differences between tyre compounds need to be greater. Although the title is a question, the body recommends a change and explains why.

### `experience`

**Definition:** Mainly recounts a specific event the author personally experienced as an F1 fan, including their response to that event.

**Example 1:** [My experience of my first F1 race on track](https://www.reddit.com/r/formula1/comments/pe70l7)

The author describes attending Spa, waiting in the rain, and dealing with travel problems. Frustration is part of the personal account.

**Example 2:** [What is your first time watching a full race feel like?](https://www.reddit.com/r/formula1/comments/u0k5mz/what_is_your_first_time_watching_a_full_race_feel/)

The body describes the author’s excitement while watching their first full race. The question in the title invites others to share, but the body tells their own story.

### `opinion`

**Definition:** Mainly presents the author’s judgment, preference, or interpretation, rather than requesting an answer, recommending a specific change, or recounting a personal event.

**Example 1:** [Besides all of the crashes and spins, how do you feel about team calls and strategy today?](https://www.reddit.com/r/formula1/comments/1jcfo5w)

The body evaluates several teams’ strategy decisions. The opening question invites discussion, while the author’s own judgments form the substance of the post.

**Example 2:** [The whole Cost Cap Situation is BS](https://www.reddit.com/r/formula1/comments/xsrpt0/the_whole_cost_cap_situation_is_bs/)

The author criticizes the cost-cap controversy and argues that enforcement cannot adequately control spending. This is an example of an expressed view, not evidence that the allegations are true.

### The hardest boundary

**Which two labels:** `question` and `opinion`.

**Real borderline post:** [Do you hate tyre chat?](https://www.reddit.com/r/formula1/comments/yim7f3)

The author explains why they enjoy technical tyre discussions, then asks whether other viewers dislike them and what they prefer. It contains both a personal view and a genuine invitation for answers.

**My choice:** `opinion`. I first chose `question`, but changed it after comparing it with practice post 2. It is still borderline: I read the author’s explanation of why they enjoy tyre discussions as the main point, with the closing questions inviting responses to that opinion.

**Decision rule:** Read the whole post and identify what its main body does. If it develops the author’s own answer or position and the closing question mainly invites agreement or disagreement, use `opinion`. If it leaves the requested information or judgment open for readers to supply and the author’s view only provides background, use `question`. Do not decide from the title or question marks alone. If both purposes remain equally central, use `question` when there is an explicit unanswered request to readers, and record the competing label and reason in the note.

**Other boundaries:**

- `proposal` versus `opinion`: identifying something as bad is an opinion; recommending a specific action to change it is a proposal when that action is the main point. A passing suggestion does not override the rest of the post.
- `experience` versus `question`: a personal story used mainly to explain a request for help is a question. A story that stands on its own and ends by inviting similar stories is an experience.
- `experience` versus `opinion`: describing what happened to the author and how they felt is an experience. Using a brief personal example mainly to argue a wider judgment is an opinion. Saying “I think” is not a personal event.
- If two purposes are still equally central after those checks, apply this tie-break order: an explicit unanswered request (`question`), a specific recommended change (`proposal`), a specific personal event (`experience`), then a judgment (`opinion`). Record the tie and its resolution. This order only resolves ties; it does not override a clear main purpose.

The practice exercise also exposed the boundary between `experience` and `opinion`. I first labeled post 8 as `experience`, then changed it to `opinion`: waiting for water supports the judgment that the event was poor value. The main-purpose rule stayed the same. My initial choices, feedback, and final decisions are in [Milestone 2 notes](notes/milestone2.md).


---

## The Dataset

**Where the posts came from:** I collected 200 public r/formula1 post candidates through the Arctic Shift archive. The collector searched within January 2020 to January 2023 and kept the title and full available body together. Each row has its source link in the note. I excluded 28 posts that did not fit my scope, such as news transcripts, statistics-only posts, image-based posts and recurring tournament polls. Their text and reasons are kept in [the exclusion log](notes/excluded_posts.csv).

I am using the milestone's time-limit fallback and stopping at **172 labeled posts** rather than collecting replacements to reach 200. The dataset stays in one `labels.csv` file; the notebook will create the train, validation and test splits.

**How I labelled them:** I labeled the first 20 posts myself, before receiving AI suggestions. My original labels are saved in [the cold-label record](notes/cold_labels_first20.csv). AI then reviewed the other 180 candidates using my taxonomy and suggested 150 labels and 30 exclusions. I accepted the 150 suggested labels and kept two of the proposed exclusions as `opinion`, leaving 28 exclusions. The notes identify the cold labels, AI pre-labels and my review decisions. 

**Counts per label:**

| Label | Count | Share |
|---|---:|---:|
| `question` | 89 | 51.7% |
| `opinion` | 67 | 39.0% |
| `proposal` | 12 | 7.0% |
| `experience` | 4 | 2.3% |
| **Total** | **172** | **100%** |

No label exceeds the milestone's 70% limit. However, this does **not** meet my own criterion that every label should make up 20–40% of the dataset. Questions dominate, and there are only four experiences and twelve proposals. I am keeping that criterion unchanged and recording the imbalance. Performance on the smallest labels will be difficult to measure reliably.

**Three hard cases**

**1. Sprint race idea — original candidate 70**
> *The post:* [A reader shares a proposed sprint format from a newsletter and asks what people think](https://www.reddit.com/r/formula1/comments/zh6fbe/).
>
> *Could have been:* `question` or `proposal`.
>
> *I chose:* `question`. The proposal belongs to the quoted newsletter writer. The Reddit author says they are not convinced and asks readers to assess it.

**2. Mass damper — original candidate 23**
> *The post:* [Could Renault's mass damper help with porpoising?](https://www.reddit.com/r/formula1/comments/ztvp2e/)
>
> *Could have been:* `question` or `proposal`.
>
> *I chose:* `question`. The author thinks dampers could help, but asks whether they would actually work and invites people with more technical knowledge to explain. The idea is still an open request for an answer.

**3. First race memory — original candidate 184**
> *The post:* A fan remembers seeing a race as a child during a family meal, years before they thought they discovered F1. The source link is recorded with original candidate 184 in `labels.csv`.
>
> *Could have been:* `experience` or `question`.
>
> *I chose:* `experience`. The main body tells a specific personal story. The closing question invites similar stories rather than asking for help or an explanation.

I also kept candidates 122 and 188 as `opinion` after AI suggested excluding them. Those scope decisions and the original suggestions are recorded in [the review notes](notes/prelabel_review.md).

---

## The Training Run

**Base model:** `distilbert-base-uncased`, fine-tuned to classify posts as `question`, `opinion`, `proposal` or `experience`.

**Settings:** 3 epochs, learning rate `2e-5`, batch size 16, maximum input length 128 tokens and seed 42. Training ran on my Apple Silicon GPU (`mps`) with PyTorch `2.14.1`. The training progress display showed about 14 seconds for the three epochs.

**Anything I changed from the defaults, and why:** I replaced the starter label list with my four labels and kept the training settings unchanged. The notebook initially could not start its kernel because files in the environment under Documents were being offloaded to iCloud. I switched to a fresh Python 3.13 environment outside Documents, using the `TakeMeter Local (Python 3.13)` kernel.

The CSV keeps the whole posts, but the model only reads the first 128 tokens of each one. Longer posts are truncated during tokenization, so the model may miss information used to assign their labels.

**Split sizes:** The notebook split the 172 posts automatically using seed 42, giving 120 training posts, 26 validation posts and 26 test posts.

| Label | Train | Validation | Test |
|---|---:|---:|---:|
| `question` | 62 | 14 | 13 |
| `opinion` | 47 | 10 | 10 |
| `proposal` | 8 | 2 | 2 |
| `experience` | 3 | 0 | 1 |
| **Total** | **120** | **26** | **26** |

There are only two proposals and one experience in the test set, below the suggested eight examples per label. These scores will be sensitive to individual predictions and may vary a lot across seeds. There are no experiences in validation, so validation cannot show how well the model recognises that label.

**What I observed:** Training completed all three epochs. Validation loss decreased from 1.1305 to 0.9946, but validation accuracy stayed at 53.8%. The final test accuracy was 50% (13 of 26 correct), with macro F1 of 0.167. The saved confusion counts confirm that every test post was predicted as `question`. Its F1 was 0.667, while the other three labels had F1 of 0.000. Finishing training did not mean the model learned to distinguish all four labels. I kept this run and its settings unchanged for the Unit 6 evaluation.

---

## How I Used AI

**Moment 1 — Checking label boundaries**

- *What I asked for:* Help testing the differences between my labels using practice posts and borderline examples.
- *What came back:* Eight practice posts and explanations of where questions, opinions, proposals and personal experiences can overlap.
- *What I changed:* I changed practice post 8 from `experience` to `opinion`, and leaned toward `opinion` for the tyre-chat example. I learned to look at the main purpose of the body instead of deciding from the title or a question mark. My choices and the boundary rules are recorded in the taxonomy and Milestone 2 notes.

**Moment 2 — Getting the notebook kernel working**

- *What I asked for:* Help after the Python 3.13 notebook kernel repeatedly timed out.
- *What came back:* AI inspected the environment and found offloaded package files in the Documents folder. It created a fresh local environment outside that folder and tested the kernel.
- *What I changed:* I selected `TakeMeter Local (Python 3.13)` and ran the notebook cells myself. The setup then detected my Apple Silicon GPU, and I completed training and saved the results. This helped me understand that a correct Python version does not guarantee the environment can load its files.

**Pre-labelling disclosure:** I labeled the first 20 posts myself before receiving AI suggestions, and kept those original labels. AI pre-labeled the remaining candidates, suggesting 150 labels and 30 exclusions. I accepted the 150 labels and changed two proposed exclusions to `opinion`, leaving 172 labeled posts and 28 exclusions. The CSV notes preserve which labels were AI-assisted and which decisions I changed.

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy |  |  |  |
| Macro F1 |  |  |  |
| F1 — `label_one` |  |  |  |
| F1 — `label_two` |  |  |  |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted |  |  |  |
|---|---|---|---|
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

**1.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**What the pattern in my disagreements tells me:**



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
