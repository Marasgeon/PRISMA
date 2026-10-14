# PRISMA_101 — RQ4 Robustness Analysis

**Citation**: Navid Vafamand, "Global Non-Quadratic Lyapunov-based Stabilization of T-S Fuzzy Systems: A Descriptor Approach," *Journal of Vibration and Control*, vol. 26, no. 19–20, pp. 1765–1778, 2020, DOI: 10.1177/1077546320904817.
**PRISMA ID**: PRISMA_101
**Fuzzy Type**: Takagi–Sugeno (T–S) with constant delayed premise variables and non-PDC (non-Parallel Distributed Compensation) controller
**System Type**: Descriptor (descriptor form $E\dot{\hat{x}} = \hat{A}\hat{x} + \hat{D}w$ augmenting state and input vectors)
**Validation**: Simulation only (flexible joint robot and two-link robot case studies)

## 1. Types of Uncertainty Addressed
- **L2-bounded external disturbance input** $w(t) \in L_2$ (modeled explicitly in the T–S plant via disturbance matrices $D_i$).
- **L∞-bounded disturbance** (the framework accommodates any bounded disturbance, not just persistent bounded).
- **Unmodeled system dynamics and exotic perturbations** (treated as additive white-noise disturbance in simulation).
- **Parameter variation / nonlinearity** (captured exactly via the sector-nonlinearity T–S representation of the underlying robotic system, e.g. $\sin(x_1)$ in the flexible-joint robot and the inverse-inertia $M^{-1}(q)$ in the two-link robot).
- **Flexible-joint coupling stiffness and friction terms** ($f_v$, $f_c$) embedded inside the T–S subsystems.

## 2. Robustness/Compensation Mechanism
Three layered mechanisms are deployed together:
- **H∞ performance criterion:** The controller is designed to satisfy $\sup \frac{\|y(t)\|}{\|w(t)\|} < \gamma$, i.e. attenuate the L2 gain from disturbance to output below a prescribed level $\gamma$ (Theorem 2).
- **Descriptor representation with slack matrices:** By augmenting $E\dot{\hat{x}} = \hat{A}\hat{x} + \hat{D}w$ and introducing slack matrices $L_{1jk}, L_{2jk}, G_{jk}, P_{2jk}, P_{3jk}$ through the Delmotte decoupling lemma, additional degrees of freedom are injected into the LMIs, reducing conservativeness and enlarging the feasible design region.
- **α-delay non-PDC controller with NQLF:** A modified non-quadratic Lyapunov function $V(\hat{x}) = \hat{x}^T E \Lambda^{-1} \hat{x}$ containing an integral term $v_i = \frac{1}{\alpha}\int_{t-\alpha}^{t} h_i(z(\tau))d\tau$ replaces the time-derivative of membership functions (which causes only local stability) with constant-delayed membership terms, achieving *global* stability and removing the requirement that $\dot{h}_i$ be bounded.

## 3. Formal Guarantees
- **Theorem 1 (non-disturbed case):** Global exponential stabilization with prescribed decay rate $\sigma$, i.e. $\dot{V}(x) + 2\sigma V(x) < 0$, via LMI conditions in equation (26).
- **Theorem 2 (disturbed case):** Global stability with a predefined L2–L2 gain $\gamma$, i.e. $\dot{V}(x) + y^T y - \gamma^2 w^T w < 0$, via LMI conditions in equation (36) including disturbance matrices $D_i$ and Schur-complement blocks.
- **Proposition 1:** $P_i = P_i^T > 0$ are sufficient conditions for the descriptor NQLF (11) to be a valid Lyapunov candidate, yielding $V(x) = x^T \Gamma^{-1} x \ge 0$.

## 4. Key Equations and Methods
- Descriptor NQLF: $V(\hat{x}) = \hat{x}^T E \Lambda^{-1} \hat{x}$ with $\Lambda = \mathrm{diag}\!\left(\sum_{i=1}^{r} v_i P_i,\; \sum_{i,j} v_j P_{2ij},\; \sum_{i,j} v_j P_{3ij}\right)$.
- α-delay non-PDC law: $u(t) = -\sum_{i,j,k} h_i(z(t)) h_j(z(t-\alpha)) v_k(z(t)) F_{ijk} \Gamma^{-1} x$.
- Closed-loop exponential decay: $\dot{V} + 2\sigma V < 0$ (Theorem 1, eq. 24).
- H∞ LMI block (Theorem 2, eq. 36) embeds the Schur complement of $C_i P_k$ and $D_i P_k$ terms, enforcing $\|G_{yw}\|_\infty < \gamma$.

## 5. Validation of Robustness
- **Scenario 1 (flexible-joint robot):** Theorem 2 yields minimum H∞ attenuation $\gamma_{\min} = 3.9937\times 10^{-5}$; states and control efforts are compared against a backstepping baseline (Chang et al., 2018) showing superior tracking.
- **Scenario 2 (disturbance injection):** White noise with zero mean and three variance levels (0, 2, 4) added to each dynamic equation; the proposed controller alleviates disturbance effect on $x_1$ and other states.
- **Feasibility region comparison:** Wider feasible parameter region than QLF (Tanaka, 2001), LLF (Márquez et al., 2013), and delay-dependent NQLF (Márquez et al., 2016).
- **Complexity comparison (Table 1):** $r+r^3=68$ LMIs vs. 260 for Márquez et al. (2016), confirming less conservative and more compact design.
- **Two-link robot case (Example 3):** Regulates joint positions $q_1, q_2$ to $\pi/2, \pi/3$ under uncertainty and external disturbance.
- No hardware experiments, no parameter Monte-Carlo sweep, no statistical robustness indices.

## 6. RQ4 Synthesis
This paper answers RQ4 by providing a globally stabilizing, robust H∞ T–S fuzzy controller for descriptor representations of robotic manipulators, addressing both L2 and L∞ bounded disturbances, unmodeled dynamics, and parameter variation. Robustness is achieved through three coupled mechanisms: a descriptor-form NQLF that converts problematic membership-function time-derivatives into delayed terms (enabling global rather than local stability), slack matrices from a decoupling lemma that reduce LMI conservativeness, and a prescribed H∞ attenuation level. Formal guarantees are global exponential stability (Theorem 1) and a tunable L2–L2 disturbance-attenuation bound (Theorem 2), validated on a flexible-joint robot and a two-link robot under white-noise disturbance injection in simulation.
