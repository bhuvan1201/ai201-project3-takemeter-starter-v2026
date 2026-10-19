# Acceptance criteria — TakeMeter

Five criteria that say what "working" means for this classifier, written in
unit 5 **before** anything was trained.

**All five are yours this time.** None are given. You've had two projects of
practice.

An acceptance criterion names a number. *"The model is accurate"* is an
opinion. *"Every label has an F1 of at least 0.60 on the held-out set"* is a
criterion.

Under each, write a sentence or two on **why that number**. A reason that says
something about your data or your taxonomy earns credit — *"I picked 0.60 F1
for `reaction` because it's my smallest label and I only have about 50
examples of it"*. A reason that could be attached to any project does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

Not numbers that sound impressive. Three labels means a coin-flip guesser gets
about 33%, so a target of 0.40 is barely a target. Your number should sit
somewhere you'd honestly call useful.

**Cover at least three of these five areas.** They're here as prompts, not as a
form to fill in — a criterion that fits none of them is fine if it names a
number.

| Area | A question it could answer |
|---|---|
| Overall accuracy | How often does it need to be right to be worth using? |
| Per-label performance | Is one label allowed to be much worse than the others? |
| Balance | How lopsided can your label counts get before it's a problem? |
| Consistency | If someone else labelled the same posts, how often should you agree? |
| Confidence | Should a confident prediction be right more often than an unsure one? |

Two things worth knowing before you pick numbers, because both will affect
whether you hit them:

- **Your smallest label will have the jumpiest score.** If a label has 50
  examples, about 8 land in the test split. An F1 computed on 8 examples moves
  a lot between seeds. A target for that label should be looser than one for
  your biggest label, and saying so is a good reason.
- **Unit 6 tests across three seeds, and the target has to hold across all
  three.** A target of 0.65 against results of 0.71, 0.62, 0.68 is a **miss**.
  Pick with that in mind — it is stricter than it first sounds.

---

## 1. Overall accuracy

The trained classifier must achieve at least 0.75 accuracy on the held-out test set in each of the three runs using seeds 42, 7, and 2024. Accuracy is the number of predictions matching the reference labels divided by the total number of test posts; every run must meet the target, not just their average.

**Why this target:**

I would use the classifier to suggest labels that I review, so I want at least three out of four suggestions to be correct and would accept correcting up to one in four. The tyre-chat post and practice post 8 showed me that `question` versus `opinion` and `experience` versus `opinion` can overlap, so this target leaves room for those difficult cases while requiring the same minimum performance across all three runs.

---

## 2. Per-label performance

Each label—`question`, `proposal`, `experience`, and `opinion`—must achieve an F1 score of at least 0.65 on the held-out test set in each run using seeds 42, 7, and 2024. Every label must meet the target in every run; an average across labels or runs does not count as passing.

**Why this target:**

I want all four labels to give useful suggestions, so strong results for one label should not hide a weakness in another. I chose 0.65 as the minimum for the weakest label because I will review the predictions manually, and the tyre-chat and event-value examples showed that opinion posts can overlap with questions and personal experiences. With about 200 posts, the test set will also be small, so a few mistakes can noticeably change a label’s F1; requiring the target in all three runs checks whether it holds consistently.

---

## 3. Dataset balance

In the final `labels.csv`, before splitting the data, each of the four labels must represent at least 20% and no more than 40% of all labeled posts. Calculate each share as the number of posts with that label divided by the total number of labeled posts. All four labels must meet the range.

**Why this target:**

I want enough examples of every label, rather than mostly collecting questions or opinions because they are easier to find. With 200 posts, this range means 40–80 examples per label: the minimum protects the smaller categories, while the maximum allows some variation without letting one label dominate. This is a deliberately balanced dataset, not an estimate of how common each type is on r/formula1. I will collect more genuine examples of underrepresented labels rather than change labels to meet the counts.

---

## 4. Independent labeling agreement

On my first 20 real posts labeled, a second person must independently assign the same label as me on at least 16 of 20 posts (80%), using the same written definitions and boundary rules. Save my original labels before sharing the posts, hide those labels from the reviewer, and calculate agreement from both sets of original labels before we discuss or resolve any disagreements.

**Why this target:**
The 80% target allows up to four disagreements on boundaries such as `question` versus `opinion`, but more disagreement would make me question whether my definitions are clear enough to produce consistent training labels. This measures agreement rather than correctness; both of us could still make the same mistake.

---

## 5. Accuracy of high-confidence predictions

In each run using seeds 42, 7, and 2024, predictions with a confidence score of at least 0.80 must achieve at least 0.85 accuracy on the held-out test set. Confidence is the model’s predicted probability for its chosen label. Calculate accuracy among these predictions as the number matching the reference labels divided by the total number qualifying. Each run must contain at least 10 qualifying predictions; otherwise, record insufficient evidence and do not mark the criterion as met. All three runs must meet both the count and accuracy requirements.

**Why this target:**

I want confident suggestions to be more reliable than the 75% overall accuracy required by criterion 1, because I might be less likely to question them. I chose 85% accuracy for predictions scoring at least 0.80 to check that confidence is supported by correct answers, especially on the overlapping `question`, `opinion`, and `experience` labels. Requiring at least 10 predictions prevents a pass based on only one or two confident answers, although this is still a small sample and does not prove that the confidence scores are calibrated.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 6 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Every label performs acceptably

         The model performs well on all labels.

         **Why this target:** ...

         > **Revised in unit 6:** Every label has an F1 of at least 0.60 on
         > the held-out set.
         >
         > **Why revised:** "performs well" gave me nothing to check. I
         > couldn't produce a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "Overall accuracy of at least 0.65" → "at least 0.55", because
            0.65 turned out to be optimistic for 200 examples.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
