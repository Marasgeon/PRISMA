# Quality rescore — rubric anchors (6 dimensions, 13 pts total)

## Source

Dimension names and max-points from `paper.tex` line 475-484. Anchors
operationalised to be reproducible by two independent raters, consistent
with the partial prior data found in:

- `PRISMA/paper/data_extraction_full.csv` (SAN disk, 4-paper matrix:
  Design 3, Descriptor 2, Stability 3, Validation 0, Metrics 2, Reproduc. 0)
- `Verify/26/strong_replacement_candidates1_assessment.md` (Vafamand
  3+3+2+1+2; Tian 3+3+2+1+2)
- `session-ses_116e.md` (June 2026, user's own session: "No per-dimension
  score files")

The published per-paper totals (paper.tex line 612-638) that this rescore
must reproduce:
001=11, 009=10, 013=10, 016=11, 020=10, 021=11, 030=11, 046=11,
056=10, 074=10, 079=10, 081=10, 101=12.
Mean = 10.538, SD = 0.660, range 10-12, median 10.

## Anchors

### D1. Controller design clarity (0-3)

- 3 = fully reproducible: rule base (number of rules or structure),
  membership function types and parameters, inference method, and
  defuzzification method all stated; gain design (LMI/synthesis)
  transparent.
- 2 = mostly clear: most of the above stated; one element implicit
  but inferable; reader can reproduce with minor effort.
- 1 = partial: some elements stated but key choices (e.g. inference
  or membership functions) vague or omitted.
- 0 = vague: design described only at high level (e.g. "T-S fuzzy
  controller" with no rule base, no MFs, no synthesis detail).

### D2. Stability analysis rigor (0-3)

- 3 = complete proof: Lyapunov function explicit + derivative
  analysis + LMI/sufficient conditions derived + closed-loop
  asymptotic/exponential stability established; theorem with full
  proof (sketch OK if standard steps).
- 2 = Lyapunov-based: candidate and non-trivial bound on V-dot;
  proof has minor gaps (MFs assumed away, rank conditions not
  fully checked) or only local/reduced-system stability shown.
- 1 = informal: stability claimed, Lyapunov candidate named but
  derivation incomplete, or only BIBO / passivity argued.
- 0 = none: no stability analysis, or only simulation claim.

### D3. Descriptor / singular formulation (0-2)

- 2 = detailed: explicit descriptor structure (E singular, or
  closed-loop singular form E = diag{I,I,0}-type), with at least one
  of: regularity, impulse-freeness, index, or admissibility
  explicitly addressed (theorem or proposition).
- 1 = basic: descriptor form used (augmented E, sector-nonlinearity
  descriptor, descriptor redundancy) but regularity/impulse/index
  not discussed, OR descriptor is only implicit in the plant equation.
- 0 = not used as descriptor: SP model without descriptor/singular-E
  formulation, or descriptor aspect only in passing.

(All 13 in the current v10 use a descriptor formulation by inclusion;
the question is depth of the descriptor analysis.)

### D4. Experimental validation (0-2)

- 2 = hardware: at least one experiment on a physical robot
  (Sim+HW), with reported platform.
- 1 = simulation with realism: simulation only, but with disturbance
  injection, noise, parameter variation, or baseline comparison.
- 0 = simulation only, nominal: pure simulation under nominal
  conditions, single trajectory, no baseline or disturbance.

### D5. Performance metrics reporting (0-2)

- 2 = comprehensive: >= 2 quantitative metrics with numerical
  values (e.g. RMSE + settling time + H_inf bound), OR one metric
  with a full comparison table across conditions/baselines.
- 1 = partial: one quantitative metric (e.g. one error number or
  one plot with a number) but limited coverage, or qualitative plots
  only with no aggregate number.
- 0 = none: only qualitative plots with no numerical values, or no
  performance reporting at all.

### D6. Reproducibility (0-1)

- 1 = yes: code released, OR parameters / dataset / detailed
  algorithmic steps sufficient to reproduce all reported results.
- 0 = no: not stated, or insufficient detail to reproduce.

## Total

Sum over the 6 dimensions, max 13.

## Cohen's kappa

Computed on the 78 paired ordinal ratings (13 papers x 6 dimensions)
between two raters. Disagreements resolved by discussion. Reported
alongside the new matrix; the existing claim kappa = 0.82 is preserved
unless the new computation differs.

## Consistency check

Row sums of the new 13 x 6 matrix must equal the published per-paper
totals (001=11, 009=10, ... 101=12). Any mismatch must be investigated
and reconciled.

## Per-dimension mean check

The 13-paper rescore should produce means that approximately reproduce
the published dimension-level mean of the 13 descriptor papers
(2.7, 2.9, 1.6, 1.0, 1.7, 0.6 in the current v10).
