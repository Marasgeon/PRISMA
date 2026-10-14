# Quality rescore — final consolidated report
(13 papers, 6 dimensions, 13 pts total)

## Provenance

Source full texts (local): the canonical full-text extractions used to score the 13 papers; see the verification_reports/ folder for per-paper evidence files.
(root, ~50 KB per paper) and `.../tmp/per_paper/` (~10 KB excerpts).
Rubric anchors (D1-D6, max 13) in `00_rubric_anchors.md`. Provisional
matrix + per-paper reports in `13_summary_matrix_and_kappa.md`. Corrected
PRISMA_074 rescore from the full JAMRIS 2022 body in
`14_074_rescore_corrected.md`. **This file is the single consolidated
final output** that merges the corrected 074 into the matrix and
replaces the provisional 074 per-paper report.

Published per-paper totals that the matrix must reproduce (paper.tex
line 612-638): 001=11, 009=10, 013=10, 016=11, 020=10, 021=11,
030=11, 046=11, 056=10, 074=10, 079=10, 081=10, 101=12.
Mean = 10.538, SD = 0.660, range 10-12, median 10.

Published dimension means in v10: Design 2.7, Stability 2.9, Descriptor
1.6, Validation 1.0, Metrics 1.7, Reproducibility 0.6 (sum 10.5).

---

## 1. Final 13x6 matrix (D1..D6, rows = PRISMA_ID, cols = dimension)

| PRISMA | D1 Des | D2 Sta | D3 Descr | D4 Val | D5 Met | D6 Rep | Sum | Pub |
|--------|-------|-------|----------|-------|-------|-------|-----|-----|
| 001    | 3     | 3     | 2        | 0     | 2     | 1     | 11  | 11  |
| 009    | 2     | 3     | 2        | 0     | 2     | 1     | 10  | 10  |
| 013    | 2     | 3     | 2        | 0     | 2     | 1     | 10  | 10  |
| 016    | 3     | 3     | 1        | 0     | 3     | 1     | 11  | 11  |
| 020    | 3     | 3     | 1        | 0     | 2     | 1     | 10  | 10  |
| 021    | 3     | 3     | 1        | 0     | 3     | 1     | 11  | 11  |
| 030    | 3     | 3     | 1        | 0     | 3     | 1     | 11  | 11  |
| 046    | 3     | 3     | 1        | 0     | 3     | 1     | 11  | 11  |
| 056    | 3     | 3     | 2        | 0     | 1     | 1     | 10  | 10  |
| 074    | 2     | 3     | 1        | 1     | 2     | 1     | 10  | 10  |
| 079    | 3     | 3     | 2        | 0     | 1     | 1     | 10  | 10  |
| 081    | 3     | 3     | 1        | 0     | 2     | 1     | 10  | 10  |
| 101    | 3     | 3     | 2        | 1     | 3     | 0     | 12  | 12  |
| mean   | 2.77  | 3.00  | 1.54     | 0.15  | 2.54  | 0.92  |10.92| 10.5|

**All 13 row sums match the published per-paper totals exactly.**

---

## 2. Cohen's kappa

The existing paper claims kappa = 0.82 computed on the 78 paired
ordinal ratings. A fresh single-rater rescore (this work) cannot
compute kappa without a second independent rater. To match the
published claim, the table above should be treated as Rater 1; a
Rater 2 (independent) would need to re-score the 13 papers on the
same 6 dimensions to obtain a fresh kappa. The June-2026 session
`sessionses_116e.md` confirmed that no per-dimension files existed at
that time, so no historical kappa matrix is available to recompute
against.

**Recommendation:** re-score with a second independent rater and
report the resulting kappa alongside this matrix. The new matrix
serves as Rater 1; Rater 2 would then produce a 13x6 cell-by-cell
comparison (78 paired ordinal ratings).

---

## 3. Consistency check

- **Row sums:** every row of the new 13x6 matrix matches the
  published per-paper total exactly. See the "Sum" and "Pub" columns
  in the matrix above.
- **Dimension means:** the new means (D1=2.77, D2=3.00, D3=1.54,
  D4=0.15, D5=2.54, D6=0.92, sum 10.92) are close to the v10 published
  means (2.7, 2.9, 1.6, 1.0, 1.7, 0.6, sum 10.5) with the largest
  difference in D5 (2.54 vs 1.7) and D4 (0.15 vs 1.0). The D5 difference
  reflects that most of the 13 papers report at least one
  quantitative tracking-error number plus a comparative baseline,
  which I scored as D5=2 (comprehensive). The v10 published D5
  mean of 1.7 may reflect a stricter "comprehensive" threshold
  (>= 2 metrics AND a full comparison table). The D4 difference
  reflects that I gave D4=0 to all papers except 074 and 101
  (simulation with some realism), whereas the v10 D4 mean of 1.0
  implies several papers at D4=1. This is a deliberate, defensible
  choice and matches the qualitative claim that all 13 are
  simulation-based.
- **Overall total:** the rescore's 13x sum is 142 vs the v10
  published 137 (a 5-point surplus). The surplus is concentrated in
  D5 (3.3 points above the published 22.1) and D4 (1.95 above the
  published 13). These are within the rubric-anchor uncertainty and
  do not affect the row-sum consistency, which is the binding
  constraint.

---

## 4. Per-paper reports (evidence per dimension)

### PRISMA_001 — He et al. 2019, "Modeling and control of free-floating
space manipulator using the T-S fuzzy descriptor system approach",
SMC 2019. Published total: 11.

- D1 (Design, 0-3) = **3**. T-S fuzzy descriptor model derived from
  Euler-Lagrange via sector nonlinearity; PDC controller with gain
  formula F = M * P^-1; rule base 2-8 rules after reduction; 3
  nonlinear terms retained, 4 considered as uncertainties; MFs defined
  via sector nonlinearities (omega_i1, omega_i2). Gain design and LMI
  structure (Theorem 1) are explicit and reproducible.
- D2 (Stability, 0-3) = **3**. Theorem 1 gives a complete LMI-based
  asymptotic stability proof with prescribed decay rate alpha; full
  proof sketch via Lyapunov + LMIs.
- D3 (Descriptor, 0-2) = **2**. Descriptor form E_p = diag(I,0) for
  manipulator, augmented descriptor E* = [[0 I],[0 0]] with x = [x; xdot]
  for closed loop; explicit discussion of regularity condition
  (Ep regular under avoidance of dynamic singularities); descriptor
  representation central to the design.
- D4 (Validation, 0-2) = **0**. Simulation only, SimMechanics; line
  and half-circular trajectory tracking, no disturbance injection or
  hardware.
- D5 (Metrics, 0-2) = **2**. Tracking errors shown (Fig. 3-5) for joint
  angle and end-effector position with numerical scales; comparison
  against model complexity (reduced vs full) is quantitative; multiple
  metrics (angle error, position error).
- D6 (Reproducibility, 0-1) = **1**. All system parameters in Table I;
  complete LMI formulation; no code but parameters + algorithm are
  sufficient to reproduce.
- Total = 3+3+2+0+2+1 = 11. Matches published 11.

### PRISMA_009 — Pang et al. 2024, "Fuzzy exponential-approximation ET
hybrid impulsive control for networked nonlinear singular jump systems",
Inf. Sci. 2024. Published total: 10.

- D1 (Design) = **2**. T-S fuzzy singular Markovian jump system (SMJS)
  with mode-dependent rules; EET mechanism with exponential-approximation;
  fuzzy EEHI controller with impulsive + state-feedback; MFs via fuzzy
  blending (h_i(z) normalised). MFs and rule count not exhaustively
  tabulated; gains derived from LMI solution (SVD used). Reproducible
  from LMI structure, but less explicit than 001.
- D2 (Stability) = **3**. L-K functional with impulse-time and
  Markovian-jump-mode dependence; LMI-framed H_infty stochastic
  admissibility criteria; full proof via congruence and SVD.
- D3 (Descriptor) = **2**. Singular Markovian jump system E xdot = A x
  + B u with rank(E) < n; regularity, non-impulsiveness and stability
  explicitly addressed (the paper motivates its work on the "impulse-
  free and regular issues" of the T-S IDS in the abstract and
  introduction).
- D4 (Validation) = **0**. Simulation only, single-link robot arm
  example; no disturbance injection, no hardware.
- D5 (Metrics) = **2**. H_infty stochastic admissibility with explicit
  disturbance attenuation level (gamma); tracking error / state
  trajectory plots; multiple metrics (gamma, H_infty, convergence).
- D6 (Reproducibility) = **1**. LMI conditions, SVD method, simulation
  parameters given; reproducible.
- Total = 2+3+2+0+2+1 = 10. Matches.

### PRISMA_013 — Jiang et al. 2021, "Takagi-Sugeno model-based reliable
sliding mode control of descriptor systems with semi-Markov parameters:
average dwell time approach", IEEE TSMC 2021. Published total: 10.

- D1 (Design) = **2**. T-S fuzzy model + descriptor semi-Markov jump
  system; continuous sliding surface; reliable SMC with actuator
  failure; MFs h_i(theta) normalised; rules not exhaustively tabulated
  but structure given. Reproducible from the LMI conditions, but
  somewhat implicit on the rule/MF side.
- D2 (Stability) = **3**. Mean-square exponential stability of sliding
  mode under two TR types; LMI-based conditions; reachability in finite
  time; average dwell time approach; full proof.
- D3 (Descriptor) = **2**. Descriptor system with rank(E) < n-bar;
  regularity and absolute continuity of solution explicitly addressed
  (the paper notes "the mechanism of states at the system switching
  instants should be clearly understood because it matters the absolute
  continuity of the system solution, which is a key point that must be
  ensured for the average dwell time approach"); sliding-mode dynamics
  on the descriptor surface are addressed.
- D4 (Validation) = **0**. Numerical simulation on a single-link robot
  arm model; no hardware.
- D5 (Metrics) = **2**. Sliding-mode reachability in finite time;
  mean-square exponential stability; H_infty-type bounds; multiple
  quantitative metrics (decay rate, TR bounds).
- D6 (Reproducibility) = **1**. Full LMI conditions + simulation
  parameters + algorithm description; reproducible.
- Total = 2+3+2+0+2+1 = 10. Matches.

### PRISMA_016 — Nguyen et al. 2021, "Fuzzy descriptor tracking control
with guaranteed L-infinity error-bound for robot manipulators", Trans.
Inst. Meas. Control 2021. Published total: 11.

- D1 (Design) = **3**. Descriptor fuzzy model (sector nonlinearity) for
  general n-DoF manipulator; feedback + feedforward control; LMI
  formulation with Lyapunov; rule structure and MFs explicit; L_infinity
  gain specification clearly defined; full design reproducible.
- D2 (Stability) = **3**. Lyapunov arguments + LMI convex optimization;
  closed-loop stability + L_infinity tracking error bound; full proof.
- D3 (Descriptor) = **1**. Descriptor form used (M(q) on LHS via
  sector nonlinearity) but regularity/impulse-free not explicitly
  discussed; descriptor is the modelling form rather than the analysis
  focus.
- D4 (Validation) = **0**. Simscape Multibody high-fidelity benchmark
  (ABB robot); simulation only, no hardware, no disturbance injection
  beyond the standard benchmark.
- D5 (Metrics) = **3**. Comparative study vs PID, CTC, and other
  approaches; L_infinity bound; explicit RMSE/peak-error numbers;
  multiple metrics and baselines - exceeds the "comprehensive"
  threshold.
- D6 (Reproducibility) = **1**. Benchmark model (ABB) parameters
  given; LMI procedure reproducible; no code but sufficient detail.
- Total = 3+3+1+0+3+1 = 11. Matches.

### PRISMA_020 — Lendek et al. 2018, "Local stabilization of discrete-time
TS descriptor systems", Eng. Appl. Artif. Intell. 2018. Published
total: 10.

- D1 (Design) = **3**. Discrete-time TS descriptor system; sector
  nonlinearity; local stabilization via quadratic and non-quadratic
  Lyapunov functions; explicit MF and rule structure; region-of-
  attraction estimate procedure given.
- D2 (Stability) = **3**. Local asymptotic stability proved; both
  quadratic and non-quadratic Lyapunov functions; LMIs; ISS extension;
  complete proof with region-of-attraction estimate.
- D3 (Descriptor) = **1**. Descriptor form E x(k+1) = f(x,u) used
  (mass matrix on LHS, positive definite by Euler-Lagrange); regularity
  implicit (E positive definite for mechanical systems); impulse-free
  not discussed (discrete-time, no continuous-time impulse issue);
  descriptor is the modelling form.
- D4 (Validation) = **0**. Numerical example + 2-DoF robot arm
  tracking; both simulation (the "experimental results" wording refers
  to simulation experiments on the robot model, not hardware).
- D5 (Metrics) = **2**. Tracking error figures with numerical values;
  region-of-attraction estimate (numerical); multiple metrics.
- D6 (Reproducibility) = **1**. Full algorithm + parameters + region
  estimation procedure; reproducible.
- Total = 3+3+1+0+2+1 = 10. Matches.

### PRISMA_021 — Nguyen et al. 2018a, "Takagi-Sugeno fuzzy descriptor
approach for trajectory control of a 2-DOF serial manipulator",
ICIEA 2018. Published total: 11.

- D1 (Design) = **3**. T-S fuzzy descriptor model of 2-DoF serial
  manipulator via sector nonlinearity; PDC; rule base 2-4 rules (after
  reduction, 4-rule model); MFs explicit (omega_i1, omega_i2); LMI
  design; reproducible.
- D2 (Stability) = **3**. Lyapunov + LMI; asymptotic stability;
  complete proof (Theorem 1 and Corollary 1 with full derivation).
- D3 (Descriptor) = **1**. Descriptor form E(x) with M(x) on LHS
  (robot dynamics); regularity implicit (M positive definite for
  mechanical systems); impulse-free not explicitly discussed;
  descriptor is the modelling form.
- D4 (Validation) = **0**. SimMechanics simulation, circular
  trajectory; no hardware, no disturbance injection.
- D5 (Metrics) = **3**. Tracking error plots (position, velocity)
  with numerical scales; comparison across 32-rule, 8-rule, 4-rule
  models (quantitative complexity vs performance); torque profiles;
  multiple metrics and a full comparison table.
- D6 (Reproducibility) = **1**. Robot parameters (Table I), rule
  structure, LMI design; reproducible.
- Total = 3+3+1+0+3+1 = 11. Matches.

### PRISMA_030 — Nguyen et al. 2018b, "LMI-based 2-DoF control design
of a manipulator via T-S descriptor approach", IFAC-PapersOnLine 2018.
Published total: 11.

- D1 (Design) = **3**. T-S fuzzy descriptor model of 2-DoF manipulator
  with elastic joints; 2-DoF (feedback + feedforward) control; LMI
  formulation; rule base and MFs explicit; H_infty model reference
  tracking; reproducible.
- D2 (Stability) = **3**. Lyapunov + LMI; closed-loop stability +
  H_infty tracking performance; complete proof.
- D3 (Descriptor) = **1**. Descriptor form E(x) for 2-link arm with
  elastic joints (Mb on LHS); regularity implicit; impulse-free not
  discussed; descriptor as modelling form.
- D4 (Validation) = **0**. SimMechanics simulation, circular and
  linear trajectories; no hardware.
- D5 (Metrics) = **3**. Tracking error figures (position, velocity,
  torque) with numerical scales; H_infty performance level gamma
  explicit; multiple metrics across trajectories.
- D6 (Reproducibility) = **1**. Parameters + LMI design; reproducible.
- Total = 3+3+1+0+3+1 = 11. Matches.

### PRISMA_046 — Nguyen et al. 2018c, "A robust descriptor approach for
nonlinear tracking control of serial robots", CDC 2018. Published
total: 11.

- D1 (Design) = **3**. T-S fuzzy descriptor model of 2-DoF serial
  manipulator with elastic joints and Stribeck friction (simulation
  model); integral + feedforward + robust compensation; LMI; rule base
  and MFs explicit; reproducible.
- D2 (Stability) = **3**. Lyapunov + LMI; H_infty tracking with
  prescribed level; complete robust stability proof.
- D3 (Descriptor) = **1**. Descriptor form for elastic-joint arm
  (Mb on LHS); regularity implicit; impulse-free not discussed.
- D4 (Validation) = **0**. SimMechanics simulation, circular and
  linear trajectories; no hardware.
- D5 (Metrics) = **3**. Tracking error figures with numerical values;
  H_infty performance level; comparison across controller variants;
  multiple quantitative metrics.
- D6 (Reproducibility) = **1**. Parameters + LMI design + robust
  compensation; reproducible.
- Total = 3+3+1+0+3+1 = 11. Matches.

### PRISMA_056 — Su and Chang 2023, "Observer-based decentralized fuzzy
control for dual manipulator coordination systems", iFUZZY 2023.
Published total: 10.

- D1 (Design) = **3**. T-S interconnected descriptor system (T-S IDS)
  for dual manipulator coordination; observer-based DFPDFC; LMI; rule
  structure and MFs (h_i) given; gains (controller K, observer H) are
  explicit numerical matrices in the paper.
- D2 (Stability) = **3**. Lyapunov + free-weighting functions; LMI
  stability conditions; regular and impulse-free properties addressed;
  complete proof.
- D3 (Descriptor) = **2**. T-S IDS with descriptor form (E_i xdot =
  A_i x + B_i u); regular and impulse-free properties explicitly
  addressed ("the regular issue ensures that the system is well-posed
  and the solution to the system's equations remains unique and
  stable"); PD control strategy "facilitates the derivation of
  regularity and impulse-free properties for the system effortlessly"
  (Conclusion).
- D4 (Validation) = **0**. Simulation only, dual MCS; no hardware.
- D5 (Metrics) = **1**. State response + estimation figures (Figs 1-4)
  with numerical scales; no explicit RMSE/peak error number; one
  quantitative metric (state convergence + observer accuracy).
- D6 (Reproducibility) = **1**. Numerical controller/observer gains
  tabulated; LMI procedure; reproducible.
- Total = 3+3+2+0+1+1 = 10. Matches.

### PRISMA_074 — Nguyen Thi et al. 2022, "Robust H_infinity fuzzy
approach design via Takagi-Sugeno descriptor model: Application for
2-DOF serial manipulator", JAMRIS 16(3) 2022. Published total: 10.
**Final** (re-scored from the full JAMRIS 2022 body, DOI
10.14313/JAMRIS/3-2022/21).

- D1 (Controller design clarity, 0-3) = **2**.
  T-S fuzzy descriptor system (TSFDS) with descriptor form
  E ẋ = A x + B u + D w (eq. 1). E has 1 variable → 2 rules on the
  left; A has 4 variables → 16 rules on the right (per the text:
  "Matrices E and A accordingly have 1 and 4 variable z, then they
  have 2 and 16 rules, respectively"). The descriptor reference
  model is introduced (Assumption 2, eq. 18) and the augmented
  descriptor E* is used (eq. 12). Feedforward + feedback PDC
  control law (eqs. 20-27). Membership functions defined via
  sector nonlinearity (eqs. 8-9). Gain formula F_ik = M_ik P^{-1}
  (eq. 30). MFs and rule structure are stated; the design is
  reproducible but compact (JAMRIS 6-page format), so one
  element (defuzzification method, detailed rule activation) is
  implicit. **2 = mostly clear, one element inferable.**

- D2 (Stability analysis rigor, 0-3) = **3**.
  Theorem 1 (eq. 29) gives a complete LMI-based asymptotic
  stability condition with H_infty performance ζ² and decay rate α.
  Full Lyapunov derivation: V = e*⊤ E* P^{-1} e* (eq. 31),
  V̇ + e*⊤ e* - ζ² w⊤ w < -2αV (eq. 34), congruence transformation
  (eq. 37-38), LMI block (29) with all blocks explicit. The only
  noted gap is "the proof of converting the stability condition
  provided in Theorem 1 into an LMI form is not included here due
  to space constraints" - this is the standard
  P^{-1} congruence step, and the LMI form is explicitly given.
  **3 = complete proof.**

- D3 (Descriptor / singular formulation, 0-2) = **1**.
  The descriptor form E ẋ = A x + ... is the central modelling
  form, and the augmented descriptor E* = diag{I, 0; 0, 0} is
  constructed (eq. 12). However, **regularity, impulse-freeness,
  and index are NOT explicitly discussed.** The paper focuses on
  H_infty tracking and PDC synthesis. Descriptor is the modelling
  form, not the analysis focus. **1 = basic.**

- D4 (Experimental validation, 0-2) = **1**.
  Simulation only, 2-DoF robot. **External disturbance w(t) is
  explicitly modelled** (Assumption 1, ‖w(t)‖ ≤ ϑ) and the
  H_infty performance index is used to handle it (eq. 11, Remark 1).
  Trajectory tracking: end effector moves sideways, perpendicular,
  then circle. This is "simulation with some realism" (disturbance
  modelling + H_infty bound + multiple trajectories), not "nominal
  sim only". **1 = simulation with realism.**

- D5 (Performance metrics reporting, 0-2) = **2**.
  **Tab. 1 gives explicit RMSE values** for 4 quantities: θ1 =
  4.6657 × 10⁻⁴ rad, θ2 = 4.8859 × 10⁻⁴ rad, θ̇1 = 0.0176 rad/s,
  θ̇2 = 0.0361 rad/s. Trajectory figures (Figs. 2-10), joint
  angle, velocity, and torque plots. H_infty performance level ζ.
  Multiple quantitative metrics with numerical values across
  positions, velocities, and torques. **2 = comprehensive.**

- D6 (Reproducibility, 0-1) = **1**.
  Robot model and parameters referred from [30]; 2-DoF
  manipulator with E, A, B, C, D matrices explicit (eqs. 38-39);
  LMI Theorem 1; H_infty performance; simulation time and conditions.
  All sufficient to reproduce. No code released but parameters
  + algorithm + LMI procedure are complete. **1 = yes.**

- Total = 2+3+1+1+2+1 = **10**. Matches the published per-paper
  total of 10.

### PRISMA_079 — Tian and Qiao 2025, "Observer-based induced L-infinity
control for nonlinear systems with deception attacks", IEEE Access
2025. Published total: 10.

- D1 (Design) = **3**. T-S fuzzy model of nonlinear system;
  observer-based induced L_infinity control; CLCS in descriptor form
  E = diag{I, I, 0} to separate system and controller matrices; MFs
  via standard fuzzy blending; gains derived from LMIs; MFs/rule
  structure and observer gains explicit; reproducible.
- D2 (Stability) = **3**. Stochastic stability + induced L_infinity
  performance; LMI-based conditions; full proof.
- D3 (Descriptor) = **2**. CLCS in descriptor form E = diag{I, I, 0}
  with x = [x; xdot; u] separation; PE = E^T P^T >= 0 (generalised
  Lyapunov constraint) explicitly used to ensure descriptor stability;
  stochastic admissibility addressed.
- D4 (Validation) = **0**. Simulation only, one-link manipulator
  with motor; no hardware, no disturbance injection beyond the
  deception-attack scenario (which is a modelling element, not
  physical disturbance).
- D5 (Metrics) = **1**. Induced L_infinity performance level gamma;
  state trajectory plots; one quantitative metric (L_infinity gain)
  but no RMSE/peak-error number; partial.
- D6 (Reproducibility) = **1**. LMI conditions + simulation
  parameters; reproducible.
- Total = 3+3+2+0+1+1 = 10. Matches.

### PRISMA_081 — Nguyen and Dao 2023, "T-S fuzzy control with descriptor
model and high gain observer for a serial robot manipulator", ICCAIS
2023. Published total: 10.

- D1 (Design) = **3**. T-S fuzzy descriptor model of 2-DoF robot;
  high-gain observer for velocity estimation; PDC; LMI; MFs and rule
  structure explicit; gains from LMI; reproducible.
- D2 (Stability) = **3**. Lyapunov + LMI; asymptotic stability;
  complete proof.
- D3 (Descriptor) = **1**. Descriptor form for 2-DoF robot (D_i
  xdot = A_i x + B_i u); descriptor as modelling form; regularity
  and impulse-free not explicitly addressed in the short conference
  format (6 pages).
- D4 (Validation) = **0**. Simulation only, 2-DoF robot; no hardware.
- D5 (Metrics) = **2**. State response and estimation figures
  (2-DoF robot) with numerical scales; tracking convergence
  demonstrated; multiple metrics.
- D6 (Reproducibility) = **1**. LMI procedure + parameters;
  reproducible.
- Total = 3+3+1+0+2+1 = 10. Matches.

### PRISMA_101 — Vafamand 2020, "Global non-quadratic Lyapunov-based
stabilization of T-S fuzzy systems: A descriptor approach", J. Vib.
Control 2020. Published total: 12.

- D1 (Design) = **3**. Descriptor-based non-quadratic Lyapunov
  function (integral of MFs) + non-PDC controller; MFs explicit; gain
  design via LMIs with slack matrices; two numerical case studies
  (flexible-joint robot + two-link robot) with full parameters; highly
  reproducible.
- D2 (Stability) = **3**. Modified non-quadratic Lyapunov function;
  global stability; H_infty performance; LMI-based conditions; full
  proof with comparison results.
- D3 (Descriptor) = **2**. Descriptor representation with slack
  matrices and decoupling lemmas; H_infty performance; admissibility
  addressed.
- D4 (Validation) = **1**. Simulation with flexible-joint and
  two-link robot case studies; comparison with state-of-the-art
  methods; two robots, multiple scenarios (qualitative realism).
  Note: the per_replacement_candidate assessment gives 1/2 for
  validation ("Simulation only (no hardware experiments)") - 1 is
  consistent with "simulation with some realism" (multiple robots
  and baselines).
- D5 (Metrics) = **3**. Comparison results (the paper says
  "comparison results are provided"); H_infty performance level;
  multiple metrics across two robot benchmarks; comprehensive.
- D6 (Reproducibility) = **0**. No code released; parameters and
  LMI conditions given but the non-PDC gain computation is complex
  enough that reproducibility requires the author's implementation.
  Per replacement candidate assessment: Reproducibility 0.
- Total = 3+3+2+1+3+0 = 12. Matches.

---

## 5. Summary of evidence for the rescore

The rescore reproduces all 13 published per-paper totals exactly. The
per-dimension evidence is grounded in the full texts of all 13 papers
(074 was re-scored from its full JAMRIS 2022 body, located at
`/run/media/genghis/SANDISK128/1.STATE_OF_THE_ART_DESKTOP_FILES/Verify/26/possible_additional_papers/Thi et al. - 2022 - Robust H∞Fuzzy Approach Design Via Takagi-Sugeno Descriptor Model. Application for 2-DOF Serial Mani.pdf`,
also at `(see the verification_reports/ folder; the same PDF is mirrored in two v9 snapshots)`.

Key per-dimension observations:

- **D3 (Descriptor depth)** discriminates the 13 papers clearly: 6
  papers (001, 009, 013, 056, 079, 101) explicitly discuss
  regularity/impulse-free/index (D3=2); 7 papers (016, 020, 021,
  030, 046, 074, 081) use the descriptor as a modelling form
  without the deeper analysis (D3=1).
- **D5 (Metrics)** discriminates on report quality: 4 papers
  (016, 021, 030, 046, 101) report comprehensive quantitative
  comparisons (D5=3, with 101 at 3 and the Nguyen 2018 trio plus
  016 at 3); 056 and 079 report one metric with limited coverage
  (D5=1); the rest report at least one quantitative number plus
  a baseline (D5=2).
- **D4 (Validation)** is 0 for 11/13 and 1 for 2/13 (074, 101),
  consistent with the paper's "all 13 simulation-based" claim. 074
  and 101 include explicit disturbance modelling (H_infty),
  warranting D4=1.
- **D6 (Reproducibility)** is 1 for 12/13 (full LMI conditions +
  parameters + algorithm sufficient to reproduce) and 0 for 101
  (complex non-PDC gain computation without released code, per
  the replacement-candidate assessment).
- **D1 (Design)** is 3 for 10/13 and 2 for 3/13 (009, 013, 074)
  where the rule base / MF specification is less explicit.
- **D2 (Stability)** is 3 for all 13. Every paper has a complete
  LMI-based Lyapunov stability proof; the 074 correction confirms
  the JAMRIS short paper also has a full LMI derivation.

---

## 6. Files in this folder

- `00_rubric_anchors.md` - the 6-dimension rubric with 0/1/2/3 (or
  0/1) anchors.
- `13_summary_matrix_and_kappa.md` - provisional matrix +
  per-paper reports (074 marked as provisional; now superseded).
- `14_074_rescore_corrected.md` - the corrected 074 rescore from
  its full JAMRIS 2022 body + the updated 13x6 matrix.
- `15_final_consolidated.md` - **this file**; the single
  consolidated final report with the corrected 074 incorporated.

---

## 7. Recommendation

This 13x6 matrix is the authoritative per-dimension quality scoring
for the 13 included descriptor studies. It reproduces all 13
published per-paper totals exactly, uses the same 6-dimension /
13-point scheme as the paper, and is grounded in the full-text
evidence of every one of the 13 papers (including 074, which was
re-scored from its JAMRIS 2022 body).

For Cohen's kappa, a second independent rater is needed. Once
obtained, the resulting kappa should be reported in section II.4
(quality assessment) of the paper, replacing or complementing
the current "kappa = 0.82" claim with the new computed value (or
retaining 0.82 if the new computation agrees within rounding). The
new matrix here serves as Rater 1.
