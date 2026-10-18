# Milestone 2 — Review and stress-test the labels

## Current status

The chosen direction is what the author is doing, rather than how well they support an argument. The README now has four labels: `question`, `proposal`, `experience`, and `opinion`.

The fourth label covers judgments that do not request information, recommend a change, or recount a personal event. It is not a catch-all for unrelated or purely factual posts. The full scope and boundary rules are in the README.

AI helped draft the definitions, assign candidate real examples, and generate the exercises below. I classified the eight practice posts, then revised two boundary decisions after discussing the feedback with AI. This exercise is separate from the later independent labeling of real dataset posts. Reddit access was limited: the examples rely on original-post text available through indexed results and the earlier reading. Open and review the full originals before accepting their assignments. The cost-cap opinion example was added during this review.

## Real boundary case: both arguments

Read [Do you hate tyre chat?](https://www.reddit.com/r/formula1/comments/yim7f3) without its comments.

- **Case for `question`:** the author explicitly asks whether others dislike tyre discussions and what they prefer. Their own preference can be read as context for learning other viewers’ preferences.
- **Case for `opinion`:** the body explains why the author finds tyre discussions interesting, including technical commentary and strategy. The final questions can be read as an invitation to respond to that position.

Both readings are possible. I used the main purpose of the body to decide, rather than the question in the title.

**My initial label:** `question`.

**My final label:** `opinion`. I still consider this a borderline post.

**Boundary explanation:** The body develops the author’s preference for tyre discussions, and the questions invite responses to that view. Using that interpretation puts it in the same category as practice post 2. The main-purpose rule stays the same; the initial assignment changes.

## Eight practice posts

These are fictional, AI-generated examples. They are not Reddit posts, real race reports, dataset rows, or part of the later 20 cold-labeled real examples. No answer key is supplied: use the README definitions and write one label and one reason for each. If two labels fit, record both and the rule that breaks the tie.

### 1

> I started watching F1 last month. I understand that hard tyres last longer, but why can staying out on them beat making another stop for softs? I cannot work out where the time is saved.

### 2

> Why do broadcasters apologize for discussing tyres? That is the most interesting part of the coverage for me. It explains why a faster driver sometimes stays behind instead of attacking. The technical discussions make the race easier to follow. Does anyone else enjoy them?

### 3

> Sprint weekends feel rushed. I think F1 should put every sprint in the first half of the season, so teams are not weighing late-season damage against the championship. Would anyone support that schedule?

### 4

> Sprint weekends feel rushed and leave me less interested in Sunday. I understand why some fans enjoy the extra competitive session, but I prefer the buildup of a normal weekend. I do not have a replacement format to suggest.

### 5

> At my first Grand Prix, I arrived before the gates opened and still ended up stuck behind a fence. Later I found a spot where I could see the braking zone, and hearing the cars there made the trip worth it. Did anyone else have a chaotic first visit?

### 6

> I bought a grandstand ticket, but my confirmation email does not show the seat number. The seller has not replied for two days. Where can I check whether the ticket is valid before I travel?

### 7

> I queued for water for forty minutes at the race. The organizers should put free refill stations beside every grandstand and mark them on the ticket map. That change would stop people missing sessions just to get a drink.

### 8

> I queued for water for forty minutes at the race, and that is why I think the event was poor value. A ticket that expensive should not come with such basic problems. The racing was enjoyable, but it does not make the overall event worth the price.

## My initial classifications

Recorded from my responses. These are initial choices; any later revisions should be recorded separately.

| Case | My label | Other label considered | Text or rule that decides it |
|---|---|---|---|
| 1 | question | Not recorded | He is asking a question because he is confused. |
| 2 | opinion | Not recorded | A strong opinion is stated. |
| 3 | proposal | Not recorded | He is telling someone to change something. |
| 4 | opinion | Not recorded | He is stating his preference; there is no proposal. |
| 5 | experience | Not recorded | He is sharing his moments first. |
| 6 | question | Not recorded | He is asking for clarification. |
| 7 | proposal | Not recorded | He is recommending a change. |
| 8 | experience | Not recorded | He is sharing a bad experience. |

## Review of the initial choices

AI feedback, not changes to my labels:

- Cases 1, 3, 4, 5, 6, and 7 fit the current definitions. For case 5, the reason should focus on the whole post telling a personal story, not just what comes first.
- Case 2 can fit `opinion` because the body develops the author's preference. A strong tone alone is not the test. The real tyre-chat post also develops a preference and asks readers for their views, so the different labels need a specific textual reason or a revision.
- Case 8 is debatable, but the current rule points toward `opinion`: the queue is used to support a judgment about the event's value. Calling every negative personal account `experience` would miss that distinction. My original `experience` label is preserved above.

**Resolution of tyre chat versus case 2:** I changed tyre chat from `question` to `opinion`, while keeping case 2 as `opinion`. Tyre chat remains borderline, but both develop the author’s view before inviting discussion.

**Resolution of case 8:** I changed `experience` to `opinion` after reviewing the distinction. The queue is a personal example supporting the wider judgment that the event was poor value. The initial answer stays in the table above.

## Final practice labels

| Case | Final label | Reason under the rule |
|---|---|---|
| 1 | question | Requests an explanation of a strategy the author does not understand. |
| 2 | opinion | Develops a preference for tyre discussions and invites agreement. |
| 3 | proposal | Recommends changing when sprint races are held. |
| 4 | opinion | Expresses a preference without recommending a specific change. |
| 5 | experience | The whole post recounts the author’s first visit; its closing question invites similar stories. |
| 6 | question | The ticket problem provides context for a request for help. |
| 7 | proposal | Recommends refill stations and a map change. |
| 8 | opinion | Uses the queue as evidence for a judgment about value. |

The exercise is complete. The two revisions resolve the identified inconsistencies under the current rules; they do not prove that every future post will be easy to classify.

## Before committing Milestone 2 as complete

- Review the four definitions and the two real examples for each in the README.
- Done: initial classifications, feedback, final labels, and the two revisions are recorded above.
- Done: the main-purpose boundary rules are retained and the README records the decisions. The four definitions match label_definitions.txt.
- If four labels remain hard to separate, simplify rather than forcing unclear distinctions.
- Confirm the Milestone 1 requirement to personally read 30–40 posts has been met; the conversation has not yet confirmed that count.
- Commit the reviewed taxonomy. Criteria are Milestone 3; data collection and the first 20 unaided labels are Milestone 4.
