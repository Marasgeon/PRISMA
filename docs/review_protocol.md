Background & Rationale
---
Robotic manipulators frequently exhibit descriptor/singular dynamics due to constraints, under-actuation or algebraic equations embedded in their kinematic/dynamic models. Classical control methods (PID, LQR, sliding mode) struggle with index-0 and higher singular systems because of implicit state variables and constraint handling.

Fuzzy Logic Control (FLC) offers rule-based, model-free design that has proven effective for nonlinear, uncertain, or poorly-modeled plants. However, only scattered work exists at the intersection of FLC _and_ descriptor dynamics in robotics. A systematic mapping is therefore required to:

1. Clarify which fuzzy controller structures have been adapted to singular systems.
2. Identify how descriptor characteristics are incorporated (e.g., index handling, constraint enforcement).
3. Summarise application settings (simulation vs hardware) and performance metrics used.
4. Highlight methodological gaps that future work should address.

Query
---
Original Query:
```
("fuzzy controller" OR "fuzzy logic controller" OR "FLC") AND ("control system" OR "robotic control") AND ("manipulator") AND ("singular" OR "descriptor")
```
NO_FLC:
```
("control system" OR "robotic control") AND ("manipulator") AND ("singular" OR "descriptor")
```
NO_MANIPULATOR:
```
("fuzzy controller" OR "fuzzy logic controller" OR "FLC") AND ("control system" OR "robotic control") AND ("singular" OR "descriptor")
```
NO_SINGULAR:
```
("fuzzy controller" OR "fuzzy logic controller" OR "FLC") AND ("control system" OR "robotic control") AND ("manipulator")
```
Research Questions
---

| RQ      | Focus                                                                                                                                       | Relevance                                                                                          |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| RQ1 | _What fuzzy controller architectures have been applied to descriptor/singular systems in robotic manipulators?_                             | Identifies the breadth of control paradigms (Mamdani, Sugeno, adaptive FLCs, neuro-fuzzy hybrids). |
| RQ2 | _How are descriptor characteristics (index order, rank deficiency, algebraic constraints) incorporated into controller design or analysis?_ | Reveals modelling and stability strategies tailored to singular dynamics.                          |
| RQ3 | _What application domains (simulation vs hardware), performance metrics, and evaluation procedures have been employed?_                     | Gauges practical impact and evidence quality.                                                      |
| RQ4 | _What gaps exist in theory development, experimental validation, or integration with existing robotic platforms?_                           | Highlights research priorities for future work.                                                    |

Objectives
---

| Objective     | Description                                                                                                                                                                                                                                  |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Primary   | Map all peer-reviewed literature that combines fuzzy controllers with descriptor/singular systems for robotic manipulators, following PRISMA-ScR methodology.                                                                                |
| Secondary | (i) Classify controller architectures and design strategies; <br> (ii) Analyse how singularity/descriptor aspects are addressed; <br> (iii) Summarise evaluation settings & metrics; <br> (iv) Identify research gaps and future directions. |

Inclusion & Exclusion Criteria
---

| Criterion                  | Inclusion (✓)                                                                                                                                       | Exclusion (✗)                                                                                                      |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Population / System    | Studies that explicitly involve a robotic manipulator _or_ an equivalent mechanical arm, and the plant model contains descriptor/singular dynamics. | Works on non-robotic systems or purely continuous-time state-space models without singularity.                     |
| Intervention (Control) | Fuzzy logic controller(s) – Mamdani, Sugeno, adaptive, neuro-fuzzy, etc.                                                                            | Pure PID, LQR, sliding mode without fuzzy elements; studies that only mention fuzzy control as a peripheral topic. |
| Outcome                | Any quantitative or qualitative assessment of controller performance (stability, tracking error, robustness).                                       | Papers lacking evaluation data or purely theoretical proofs with no simulation/experiment.                         |
| Study Design           | Peer-reviewed journal articles, conference proceedings, PhD dissertations, and technical reports (English language).                                | Editorials, short notes (<2 pages), non-peer-reviewed blogs, patents, white papers.                                |
| Time Frame             | 1970–present (inclusive).                                                                                                                           | Earlier works before 1970; future works beyond the search window.                                                  |
| Language               | English only.                                                                                                                                       | Non-English language unless a full translation is available.                                                       |
Information Sources & Search Strategy
---

| Database                                    | Search Fields           | Example Query                                                                                                                                                                                            | Notes                                                                          |
| ------------------------------------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| IEEE Xplore                             | Title/Abstract/Keywords | `("fuzzy controller" OR "fuzzy logic controller" OR FLC) AND ("control system" OR "robotic control") AND manipulator AND (singular OR descriptor)`                                                       | Use Boolean operators exactly as shown; filter to “Conference & Journal” only. |
| Scopus                                  | Title/Abstract/Keywords | `TITLE-ABS-KEY("fuzzy controller" OR "fuzzy logic controller" OR FLC) AND TITLE-ABS-KEY("control system" OR "robotic control") AND TITLE-ABS-KEY(manipulator) AND TITLE-ABS-KEY(singular OR descriptor)` | Apply “Year 1970–2025” filter.                                                 |
| Web of Science                          | Title/Abstract/Keywords | `TS=("fuzzy controller" OR "fuzzy logic controller" OR FLC) AND TS=("control system" OR "robotic control") AND TS=manipulator AND TS=(singular OR descriptor)`                                           | Use “Timespan: 1970-2025”.                                                     |
| ACM Digital Library                     | Keywords                | `("fuzzy controller" OR "fuzzy logic controller" OR FLC) AND ("control system" OR "robotic control") AND manipulator AND (singular OR descriptor)`                                                       | Restrict to proceedings & journals.                                            |
| SpringerLink / Springer Nature          | Title/Abstract          | Same Boolean string as above.                                                                                                                                                                            | Use “All content” filter.                                                      |
| Elsevier ScienceDirect                  | Title/Abstract          | Same Boolean string.                                                                                                                                                                                     | Include both journal articles and conference papers.                           |
| MDPI (Sensors, Entropy)                 | Title/Abstract          | Same Boolean string.                                                                                                                                                                                     | Open-access; include proceedings if available.                                 |
| Google Scholar                          | Entire text             | Use the same query but add “fuzzy logic controller” + “descriptor system”                                                                                                                                | Manual screening for grey literature & theses.                                 |
| ProQuest / NDLTD (theses/dissertations) | Title/Abstract          | Same Boolean string                                                                                                                                                                                      | Search full-text where available.                                              |

All queries will be run in each database on the same date; results exported to Zotero with DOI and metadata fields.

---

Study Selection Process

1. Deduplication – Automatic removal of duplicates across databases using EndNote’s “Find Duplicates” function.
2. Title & Abstract Screening – Screen each record against the inclusion/exclusion criteria. 
3. Full-Text Retrieval & Assessment – Same process for full texts.
4. PRISMA Flow Diagram – Document counts at each stage; reasons for exclusion will be recorded in an Excel audit trail.

---

Data Extraction

A standardized extraction sheet (Microsoft Excel) will capture:

| Item                                                                                      | Description |
| ----------------------------------------------------------------------------------------- | ----------- |
| Bibliographic info (title, authors, year, venue, DOI)                                     |             |
| Study type (journal article, conference paper, thesis)                                    |             |
| Manipulator description (degrees-of-freedom, kinematic chain, actuation)                  |             |
| Descriptor system details (index, rank deficiency, algebraic constraints)                 |             |
| Fuzzy controller architecture (type, rule base, inference engine, adaptation mechanism)   |             |
| Design methodology (controller synthesis, stability analysis, constraint handling)        |             |
| Implementation platform (simulation software, real hardware, hybrid)                      |             |
| Performance metrics & evaluation results (tracking error, robustness, computational load) |             |
| Comparative baseline(s) (classical controller, other intelligent controllers)             |             |
| Reported limitations / future work suggestions                                            |             |
