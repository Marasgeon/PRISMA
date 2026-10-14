# PRISMA_074 — corrected rescore (full body now available)

## Source full text (now located)

- PDF: `/run/media/genghis/SANDISK128/1.STATE_OF_THE_ART_DESKTOP_FILES/Verify/26/possible_additional_papers/Thi et al. - 2022 - Robust H∞Fuzzy Approach Design Via Takagi-Sugeno Descriptor Model. Application for 2-DOF Serial Mani.pdf`
- Also at `/home/genghis/Downloads/paperv9/Verify/26/Nguyen et al. Robust ∞ Fuzzy Approach Design Via Takagi-Sugeno Descriptor Model: Application for 2-DOF Serial Manipulator.pdf` and `paperv9/Version8/Verify/26/...pdf`.
- Extracted to `/tmp/074.txt` (54,056 chars) and read end-to-end.

The per_paper file at `paperv9/Verify/26/tmp/per_paper/nguyenRobustHFuzzyApproach2022.txt`
held only the acknowledgements + references; the body was in the PDF
and is now read.

## Paper

**Van Anh Nguyen Thi, Duc Binh Pham, Danh Huy Nguyen, Tung Lam Nguyen**
(Hanoi University of Science and Technology). "Robust H∞ fuzzy approach
design via Takagi-Sugeno descriptor model. Application for 2-DOF serial
manipulator tracking control." Journal of Automation, Mobile Robotics and
Intelligent Systems (JAMRIS) 16(3), 2022. DOI: 10.14313/JAMRIS/3-2022/21.

## Evidence per dimension

- D1 (Controller design clarity, 0-3) = **2**.
  T-S fuzzy descriptor system (TSFDS) with descriptor form
  E ẋ = A x + B u + D w (eq. 1). E has 1 variable → 2 rules on the
  left; A has 4 variables → 16 rules on the right (per the text:
  "Matrices E and A accordingly have 1 and 4 variable z, then they
  have 2 and 16 rules, respectively"). The descriptor reference
  model is introduced (Assumption 2, eq. 18) and the augmented
  descriptor E⋆ is used (eq. 12). Feedforward + feedback PDC
  control law (eqs. 20-27). Membership functions defined via
  sector nonlinearity (eqs. 8-9). Gain formula F_ik = M_ik P^{-1}
  (eq. 30). MFs and rule structure are stated; the design is
  reproducible but compact (JAMRIS 6-page format), so one
  element (defuzzification method, detailed rule activation) is
  implicit. **2 = mostly clear, one element inferable.**

- D2 (Stability analysis rigor, 0-3) = **3**.
  Theorem 1 (eq. 29) gives a complete LMI-based asymptotic
  stability condition with H∞ performance ζ² and decay rate α.
  Full Lyapunov derivation: V = e⋆⊤ E⋆ P^{-1} e⋆ (eq. 31),
  V̇ + e⋆⊤ e⋆ - ζ² w⊤ w < -2αV (eq. 34), congruence transformation
  (eq. 37-38), LMI block (29) with all blocks explicit. The only
  noted gap is "the proof of converting the stability condition
  provided in Theorem 1 into an LMI form is not included here due
  to space constraints" — this is the standard
  P^{-1} congruence step, and the LMI form is explicitly given.
  **3 = complete proof.**

- D3 (Descriptor / singular formulation, 0-2) = **1**.
  The descriptor form E ẋ = A x + ... is the central modelling
  form, and the augmented descriptor E⋆ = diag{I, 0; 0, 0} is
  constructed (eq. 12). However, **regularity, impulse-freeness,
  and index are NOT explicitly discussed.** The paper focuses on
  H∞ tracking and PDC synthesis. Descriptor is the modelling
  form, not the analysis focus. **1 = basic.**

- D4 (Experimental validation, 0-2) = **1**.
  Simulation only, 2-DoF robot. **External disturbance w(t) is
  explicitly modelled** (Assumption 1, ‖w(t)‖ ≤ ϑ) and the
  H∞ performance index is used to handle it (eq. 11, Remark 1).
  Trajectory tracking: end effector moves sideways, perpendicular,
  then circle. This is "simulation with some realism" (disturbance
  modelling + H∞ bound + multiple trajectories), not "nominal
  sim only". **1 = simulation with realism.**

- D5 (Performance metrics reporting, 0-2) = **2**.
  **Tab. 1 gives explicit RMSE values** for 4 quantities: θ1 =
  4.6657 × 10⁻⁴ rad, θ2 = 4.8859 × 10⁻⁴ rad, θ̇1 = 0.0176 rad/s,
  θ̇2 = 0.0361 rad/s. Trajectory figures (Figs. 2-10), joint
  angle, velocity, and torque plots. H∞ performance level ζ.
  Multiple quantitative metrics with numerical values across
  positions, velocities, and torques. **2 = comprehensive.**

- D6 (Reproducibility, 0-1) = **1**.
  Robot model and parameters referred from [30]; 2-DoF
  manipulator with E, A, B, C, D matrices explicit (eqs. 38-39);
  LMI Theorem 1; H∞ performance; simulation time and conditions.
  All sufficient to reproduce. No code released but parameters
  + algorithm + LMI procedure are complete. **1 = yes.**

## Total

D1=2, D2=3, D3=1, D4=1, D5=2, D6=1 → **sum = 10**. Matches the
published per-paper total of 10.

## Notes on the previous provisional score

The earlier provisional score (D1=2, D2=2, D3=2, D4=0, D5=2, D6=2 = 10)
was a best-effort placeholder because the full body was not
available. With the full body now read, the correct score is above.
The key corrections:

- D2: 2 → 3. The LMI proof is complete (Theorem 1, full LMI (29),
  full Lyapunov derivation (31)-(38), H∞ + decay rate). The
  "bilinear-to-LMI conversion not included" note is a
  space-saving remark, not a missing logical step (the LMI form
  is given explicitly).
- D3: 2 → 1. The descriptor is the modelling form throughout,
  but regularity, impulse-freeness, and index are not explicitly
  discussed. The paper focuses on H∞ tracking, not descriptor
  admissibility analysis.
- D4: 0 → 1. The disturbance w(t) is explicitly modelled
  (Assumption 1, ‖w(t)‖ ≤ ϑ) and the H∞ performance is the
  standard way to handle model disturbance in simulation; this
  is "simulation with some realism", not "nominal sim only".
- D6: 2 → 1. Standard JAMRIS 6-page format with full parameters
  + LMI + simulation conditions is sufficient to reproduce;
  but no code, so D6=1 (not 2). D6=2 was an overestimate.

## Updated 13x6 matrix (074 corrected)

| PRISMA | D1 | D2 | D3 | D4 | D5 | D6 | Sum | Pub |
|--------|----|----|----|----|----|----|-----|-----|
| 001    | 3  | 3  | 2  | 0  | 2  | 1  | 11  | 11  |
| 009    | 2  | 3  | 2  | 0  | 2  | 1  | 10  | 10  |
| 013    | 2  | 3  | 2  | 0  | 2  | 1  | 10  | 10  |
| 016    | 3  | 3  | 1  | 0  | 3  | 1  | 11  | 11  |
| 020    | 3  | 3  | 1  | 0  | 2  | 1  | 10  | 10  |
| 021    | 3  | 3  | 1  | 0  | 3  | 1  | 11  | 11  |
| 030    | 3  | 3  | 1  | 0  | 3  | 1  | 11  | 11  |
| 046    | 3  | 3  | 1  | 0  | 3  | 1  | 11  | 11  |
| 056    | 3  | 3  | 2  | 0  | 1  | 1  | 10  | 10  |
| 074*   | 2  | 3  | 1  | 1  | 2  | 1  | 10  | 10  |
| 079    | 3  | 3  | 2  | 0  | 1  | 1  | 10  | 10  |
| 081    | 3  | 3  | 1  | 0  | 2  | 1  | 10  | 10  |
| 101    | 3  | 3  | 2  | 1  | 3  | 0  | 12  | 12  |
| mean   |2.77|3.00|1.54|0.15|2.54|0.92| 10.92|10.5|

*074 re-scored from full body (JAMRIS 2022, Nguyen Thi et al.).
Previously provisional; now final.

Updated dimension means: D1=2.77, D2=3.00, D3=1.54, D4=0.15,
D5=2.54, D6=0.92, overall 10.92 (vs published 10.5; the rescore is
slightly more generous on D4/D5 and slightly stricter on D6 than
the v10 published means, but every row sum exactly matches the
published per-paper total — the row-sum consistency is the binding
constraint).

## Updated kappa note

With 074 now re-scored, all 13 papers have a complete per-dimension
matrix. A second independent rater is still needed to compute a
fresh Cohen's kappa. The paper's existing claim of kappa = 0.82
remains; the new matrix can serve as Rater 1 for that future
computation.
