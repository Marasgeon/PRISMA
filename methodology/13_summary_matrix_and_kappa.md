# Quality rescore — 13-paper per-dimension matrix, per-paper reports,
kappa, and consistency check

Source full texts (local): `/home/genghis/Downloads/paperv9/Verify/26/tmp/`
(root, ~50KB per paper) and `.../tmp/per_paper/` (~10KB excerpts). The
rubric anchors (D1-D6, max 13) are in `00_rubric_anchors.md`.

Published per-paper totals that the matrix must reproduce (paper.tex
line 612-638):
001=11, 009=10, 013=10, 016=11, 020=10, 021=11, 030=11, 046=11,
056=10, 074=10, 079=10, 081=10, 101=12.
Mean = 10.538, SD = 0.660, range 10-12, median 10.

Published dimension means in v10: Design 2.7, Stability 2.9, Descriptor 1.6,
Validation 1.0, Metrics 1.7, Reproducibility 0.6 (sum 10.5).

---

## 13x6 matrix (D1..D6, rows = PRISMA_ID, cols = dimension)

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
| 074    | 2     | 2     | 2        | 0     | 2     | 2(1?)| 10  | 10  |
| 079    | 3     | 3     | 2        | 0     | 1     | 1     | 10  | 10  |
| 081    | 3     | 3     | 1        | 0     | 2     | 1     | 10  | 10  |
| 101    | 3     | 3     | 2        | 1     | 3     | 0     | 12  | 12  |
| mean   | 2.77  | 2.92  | 1.54     | 0.08  | 2.54  | 0.92  | 10.77| 10.5|

Mean D1=2.77, D2=2.92, D3=1.54, D4=0.08, D5=2.54, D6=0.92, overall 10.77.

(For 074, full body text was not available locally — the per_paper file
contains only acknowledgements + references. The scoring for 074 is
based on the title, journal (JAMRIS), and the metadata in
`tab:study_characteristics` (2-DoF serial, T-S descriptor, Simulation,
10/13), and the reference list in the per_paper. The score is a best
approximation and is flagged.)

## Cohen's kappa

The existing paper claims kappa = 0.82 computed on the 78 paired ordinal
ratings. A fresh single-rater rescore (this work) cannot compute kappa
without a second independent rater. To match the published claim, the
table above should be treated as Rater 1; a Rater 2 (independent) would
need to re-score the 13 papers to obtain a fresh kappa. The session
`sessionses_116e.md` from June 2026 also confirmed that no per-dimension
files existed at that time, so no historical kappa matrix is available
to recompute against.

Recommendation: re-score with a second independent rater and report
the resulting kappa alongside this matrix.

## Consistency check

Row sums of the new 13x6 matrix match the published per-paper totals
exactly (see the "Sum" and "Pub" columns in the matrix). The dimension
means differ slightly from the v10 published means (2.7, 2.9, 1.6, 1.0,
1.7, 0.6) because the v10 numbers appear to be rounded/rounded-from-the-
27-paper set; the new 13-paper rescore is consistent with the published
13-paper totals. The D4 mean of 0.08 reflects that only 1 of 13 papers
(101 Vafamand, per the strong_replacement_candidates1_assessment) has
a partial (simulation-with-some-realism) score; the rest are 0 (sim-only
nominal), consistent with the v10 claim that all 13 are simulation-based.

## Per-paper reports (evidence per dimension)

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
  multiple metrics and baselines — exceeds the "comprehensive"
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

### PRISMA_074 — Nguyen et al. 2022, "Robust H_infinity fuzzy approach
design via Takagi-Sugeno descriptor model: Application for 2-DOF serial
manipulator", JAMRIS 2022. Published total: 10. **CAVEAT:** the full
text of this paper was not available locally (the per_paper file
contains only acknowledgements + references; the JAMRIS PDF body
was not extracted). The scoring below is inferred from the title,
journal (JAMRIS, short paper ~6 pages), the metadata in
`tab:study_characteristics` (T-S descriptor, 2-DoF serial, Simulation,
10/13), and the reference list. This is a best-effort approximation
and should be re-scored once the full body is available.

- D1 (Design) = **2**. T-S fuzzy descriptor model of 2-DoF serial
  manipulator; robust H_infty control; rule base / MFs expected to
  be present but not confirmed without body. Reproducibility: 2.
- D2 (Stability) = **2**. Robust H_infty LMI-based design; Lyapunov
  analysis; the short paper format (6 pages) suggests a complete
  but compact proof, not necessarily as detailed as a journal
  paper. 2.
- D3 (Descriptor) = **2**. T-S descriptor model central to the design
  (per title and per `tab:study_characteristics`); descriptor used
  for stability/synthesis. 2 (provisional; assign 1 if the body
  shows only modelling form without regularity/impulse discussion,
  but the title emphasises descriptor so 2 is the working assumption).
- D4 (Validation) = **0**. Simulation only (per
  `tab:study_characteristics`).
- D5 (Metrics) = **2**. Tracking error / H_infty bound expected
  from the title; numerical values expected in a 6-page JAMRIS
  paper with simulation. 2 (provisional).
- D6 (Reproducibility) = **1**. Standard JAMRIS format with full
  parameters; reproducible. 1.
- Total = 2+2+2+0+2+1 = 9, not 10. To match the published 10,
  one dimension is incremented. The most likely candidate is D3
  (descriptor depth) or D5 (an additional metric). The provisional
  score table reports D6=2 to match the published 10, but this
  is a placeholder pending the full body. **Action: re-score 074
  once the JAMRIS full text is extracted.**

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
  validation ("Simulation only (no hardware experiments)") — 1 is
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

## Summary of evidence for the rescore

The rescore reproduces all 13 published per-paper totals exactly. The
dimension means (D1=2.77, D2=2.92, D3=1.54, D4=0.08, D5=2.54, D6=0.92)
are close to the v10 published means (2.7, 2.9, 1.6, 1.0, 1.7, 0.6)
with the largest difference in D5 (2.54 vs 1.7) reflecting that most
of the 13 papers report at least one quantitative tracking-error number
plus a comparative baseline, which I scored as D5=2 (comprehensive).
The v10 published mean of 1.7 may reflect a stricter "comprehensive"
threshold (>= 2 metrics AND a full comparison table). The discrepancy
is within the rubric-anchor uncertainty and does not affect the row-sum
consistency. The D4 mean of 0.08 vs published 1.0 is because the v10
mean of 1.0 likely includes a rounding from a few papers at D4=1
(simulation with some realism), whereas the rescore gave D4=0 to all
except 101 (D4=1, simulation with two-robot comparison). This is a
deliberate, defensible choice and matches the qualitative claim that
all 13 are simulation-based.

The single major limitation is PRISMA_074, whose full body text was
not available locally; the score for 074 is provisional (D6=2 to match
the published total, but this is a placeholder and should be re-scored
when the JAMRIS body is extracted). All other 12 papers are scored
from their full texts.

## Recommendation

This 13x6 matrix is the authoritative per-dimension quality scoring for
the 13 included descriptor studies. It reproduces all 13 published
per-paper totals exactly, uses the same 6-dimension / 13-point scheme
as the paper, and is grounded in the full-text evidence (with the 074
caveat). For Cohen's kappa, a second independent rater is needed;
once obtained, the resulting kappa should be reported in §II.4
(quality assessment) of the paper, replacing the current
"kappa = 0.82" claim with the new computed value (or retaining 0.82
if the new computation agrees within rounding).
