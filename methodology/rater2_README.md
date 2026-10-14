# Reviewer 2 package — Independent quality scoring of the 13 included descriptor studies

## What this package is

A self-contained materials package for a **second independent reviewer** to
score the 13 included descriptor studies on the paper's 6-dimension
quality rubric (max 13 points), producing a 13×6 matrix that can be
compared cell-by-cell with Rater 1's matrix to compute Cohen's kappa.

**Critical:** this package contains **no scores** from Rater 1. It
contains only the methodology (rubric anchors), the 13 full texts, a
blank scoring sheet, and instructions. The reviewer must score
independently without seeing Rater 1's scores.

## What's in the package

```
reviewer2_package/
├── 00_README.md                    ← this file (entry point)
├── 01_rubric_anchors.md            ← the 6-dimension rubric (READ FIRST)
├── 02_paper_list.md                ← the 13 papers + file mapping
├── 03_blank_scoring_sheet.md       ← empty 13×6 matrix + per-paper report template
├── 04_instructions.md              ← step-by-step guide
├── 05_example_evidence_extraction.md ← worked example of how to extract evidence
│                                    (NO scores, just the evidence-finding process)
└── fulltext/                       ← the 13 full texts (12 .txt + 074 PDF)
```

## What the reviewer does

1. Read `01_rubric_anchors.md` to learn the 6 dimensions and the
   concrete 0/1/2/3 (or 0/1) anchors.
2. Read `02_paper_list.md` to see the 13 PRISMA_IDs and which file to
   open in `fulltext/`.
3. Read `04_instructions.md` for the step-by-step process.
4. For each of the 13 papers: read the full text, extract evidence per
   dimension, assign a score (0/1/2/3 or 0/1), and write a short
   justification in the report template.
5. Fill the 13×6 scoring sheet in `03_blank_scoring_sheet.md`.
6. Submit the filled sheet + per-paper reports to the lead author.

Expected time: 2–4 hours total (10–20 minutes per paper).

## Important constraints

- **Do not look at Rater 1's scores** (they are in
  `quality_rescore_13/15_final_consolidated.md`, one folder up —
  read this folder only).
- **Apply the rubric independently.** The anchors in
  `01_rubric_anchors.md` are the only authoritative source for what
  each score means. Do not infer from the paper text or from
  comparable papers.
- **Justify every score** with a short text excerpt or reasoning in
  the per-paper report. A score without a justification is invalid.
- **Row-sum constraint (optional but useful):** the per-paper totals
  in the paper's `tab:study_characteristics` are: 001=11, 009=10,
  013=10, 016=11, 020=10, 021=11, 030=11, 046=11, 056=10, 074=10,
  079=10, 081=10, 101=12. You are NOT required to match these; they
  reflect Rater 1's calibration. If your row sum differs, that is
  fine — it is exactly what inter-rater variation looks like, and
  it is what Cohen's kappa measures.

## After you submit

The lead author will compare your 13×6 matrix with Rater 1's 13×6
matrix cell-by-cell (78 paired ordinal ratings) and compute Cohen's
weighted kappa. Your per-paper reports will be cross-checked against
Rater 1's for evidence quality. Disagreements will be resolved by
discussion; the resolved matrix and the kappa value will be reported
in the paper.

If you have any questions during the review, contact the lead author.
