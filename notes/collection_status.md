# Dataset collection status

Milestone 4 collection and review are complete under the documented time-limit fallback:

- 200 archive candidates collected; 172 labeled posts retained in `labels.csv`.
- 28 excluded candidates preserved in `excluded_posts.csv` with source links and reasons.
- First 20 cold labels preserved in `cold_labels_first20.csv`.
- User accepted 150 AI pre-labels and assigned `opinion` to two proposed exclusions.
- Final counts: 89 questions, 67 opinions, 12 proposals, 4 experiences.
- No label exceeds 70%; the separate 20–40% acceptance criterion is missed and unchanged.
- README documents the source, workflow, fallback and three label-boundary cases.

The collector's JSON report records the earlier 200-candidate collection stage, not the final 172-post dataset. The old `labels_review.xlsx` is a stale labeling aid, not the training input.

---

# Initial export inspection (historical)

Source checked: `/Users/bhuvan/Downloads/posts.json`, a public archive export of r/formula1 posts.

Records inspected: 100. Eligible dataset posts: 0.

| Exclusion reason | Count |
|---|---|
| Removed or deleted body | 97 |
| Empty body | 2 |
| Automated daily-discussion thread | 1 |

At the time of this initial inspection, `labels.csv` contained only the required `text,label,note` header. No titles were substituted for missing bodies, and no labels were assigned. The automated thread is outside the scope defined in the README.

At that stage collection was not complete. Full title-and-body text from eligible posts is still needed. The first 20 must remain unlabelled until the independent cold-labeling exercise; they have not been collected or labeled yet.
