# Quality assessment rubric anchors

The six dimensions and the 0 to 3 (or 0 to 1) anchor points below operationalise the rubric so that two independent raters can apply it to the same full text and reach consistent scores.

## D1. Controller design clarity (0-3)

- 3 = fully reproducible: rule base (number of rules or structure), membership function types and parameters, inference method, and defuzzification method all stated; gain design (LMI or synthesis) is transparent.
- 2 = mostly clear: most of the above stated; one element implicit but inferable; reader can reproduce with minor effort.
- 1 = partial: some elements stated but key design choices (e.g. inference or membership functions) vague or omitted.
- 0 = vague: design described only at high level (e.g. "T-S fuzzy controller" with no rule base, no MFs, no synthesis detail).

## D2. Stability analysis rigor (0-3)

- 3 = complete proof: Lyapunov function explicit plus derivative analysis plus LMI or sufficient conditions derived plus closed-loop asymptotic or exponential stability established; theorem with full proof (sketch OK if standard steps).
- 2 = Lyapunov-based: candidate and non-trivial bound on V-dot; proof has minor gaps (MFs assumed away, rank conditions not fully checked) or only local or reduced-system stability shown.
- 1 = informal: stability claimed, Lyapunov candidate named but derivation incomplete, or only BIBO or passivity argued.
- 0 = none: no stability analysis, or only simulation claim.

## D3. Descriptor / singular formulation (0-2)

- 2 = detailed: explicit descriptor structure (E singular, or closed-loop singular form E = diag{I, I, 0} type), with at least one of regularity, impulse-freeness, index, or admissibility addressed in a theorem or proposition.
- 1 = basic: descriptor form used (augmented E, sector-nonlinearity descriptor, descriptor redundancy) but regularity, impulse, or index not discussed; or descriptor is only implicit in the plant equation.
- 0 = not used as descriptor: SP model without descriptor or singular-E formulation, or descriptor aspect only in passing.

## D4. Experimental validation (0-2)

- 2 = hardware: at least one experiment on a physical robot (Sim + HW), with reported platform.
- 1 = simulation with realism: simulation only, but with disturbance injection, noise, parameter variation, or baseline comparison.
- 0 = simulation only, nominal: pure simulation under nominal conditions, single trajectory, no baseline or disturbance.

## D5. Performance metrics reporting (0-2)

- 2 = comprehensive: at least two quantitative metrics with numerical values (e.g. RMSE plus settling time, plus H-infinity bound), or one metric with a full comparison table across conditions or baselines.
- 1 = partial: one quantitative metric (e.g. one error number, or one plot with a number) but limited coverage, or qualitative plots only with no aggregate number.
- 0 = none: only qualitative plots with no numerical values, or no performance reporting at all.

## D6. Reproducibility (0-1)

- 1 = yes: code released, or parameters plus dataset plus detailed algorithmic steps sufficient to reproduce all reported results.
- 0 = no: not stated, or insufficient detail to reproduce.

## Total

Sum over the six dimensions, max 13.
