# Agile Capstone Project Report: 8 Epics & 14 Tasks
**Project Title:** Global Olympic Sports Performance Analysis (1992 - 2026)  
**Methodology:** Agile Data Analytics & Business Intelligence Engineering  
**Total Epics:** 8 | **Total Tasks:** 14 | **Total Subtasks:** 0  

---

## Executive Summary
This Agile Capstone Project delivers an end-to-end data analytics and business intelligence solution analyzing 34 years of modern Olympic competition (1992–2026). Sourced from multi-dimensional datasets covering **60 countries**, **50 sports categories**, and **27,557 medal results**, the project empowers three core stakeholder personas:
1. **Ms. Priya (NOC Performance Strategist):** Directing capital toward high-yield sports disciplines (Rowing at 6.916 medals/athlete, Shooting at 6.731).
2. **Mr. Carlos (Sports Investment Analyst):** Optimizing international grant allocations using regional medal efficiency benchmarks (South America at 49.64%, Europe/Asia at 45.98%) and capital efficiency outliers (Slovakia, Georgia, Ethiopia).
3. **William Robert (Broadcast Journalist & Data Storyteller):** Illuminating multi-decadal narrative arcs, including historical medal swings (low of 305 in 2000 to peak of 363 in 2020, and 334 in 2026) and home host dominance (Japan: 105, USA: 100, China: 93).

---

## Epic & Task Breakdown Matrix

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       PROJECT ARCHITECTURE OVERVIEW                         │
├────────────────────────┬─────────────────────────┬──────────────────────────┤
│ Epic 1: Scoping (T1,T2)│ Epic 2: Synthesis (T3)  │ Epic 3: Prep (T4, T5)    │
│ Requirements & Arch    │ 60 Nations / 50 Sports  │ Star Schema & Master CSV │
├────────────────────────┼─────────────────────────┼──────────────────────────┤
│ Epic 4: EDA (T6, T7)   │ Epic 5: Dash 1 (T8)     │ Epic 6: Dash 2 (T9)      │
│ Calculations & Metrics │ Athlete Yield & Totals  │ Investment & Regional    │
├────────────────────────┼─────────────────────────┼──────────────────────────┤
│ Epic 7: Story (T10,T11)│ Epic 8: Handover (12-14)│ Deployment & Delivery    │
│ Priya, Carlos, William │ Executive Reporting     │ Tableau Workbook & Web UI│
└────────────────────────┴─────────────────────────┴──────────────────────────┘
```

---

### Epic 1: Project Scoping, Business Understanding & Agile Architecture
* **Objective:** Establish the analytical foundation, stakeholder user personas, technical requirements, and data governance framework.

#### Task 1: Problem Definition & Persona Scenarios Mapping
* **Description:** Formalized the operational objectives of Ms. Priya (NOC Strategist), Mr. Carlos (Sports Investment Analyst), and William Robert (Documentary Storyteller). Formulated business hypotheses regarding sport yield disparities, capital efficiency, and host nation advantage.
* **Deliverable:** Stakeholder Requirements Specification & KPI Alignment Matrix.
* **Status:** Complete.

#### Task 2: System Architecture & Technical Environment Setup
* **Description:** Defined the hardware/software infrastructure required for processing large-scale historical records. Configured Tableau Desktop / Public connectivity, Python 3 data pipelines, and relational schema conventions.
* **Deliverable:** System Architecture Document & Environment Verification.
* **Status:** Complete.

---

### Epic 2: Data Collection & Schema Modeling
* **Objective:** Source, structure, and model comprehensive multi-year Olympic datasets spanning 1992 through 2026.

#### Task 3: Ingestion & Relational Data Modeling
* **Description:** Ingested and structured four core relational datasets:
  1. `athletes.csv`: 7,552 records across 50 sports categories and 60 nations.
  2. `medal_results.csv`: 27,557 medal outcomes across Summer and Winter Games.
  3. `sports_investment.csv`: Macro investment expenditures, grassroots funding, and medal counts.
  4. `olympic_hosts.csv`: Host cities, host nations, and home-competition medal tallies.
* **Deliverables:** Raw CSV datasets in `data/raw/`.
* **Status:** Complete.

---

### Epic 3: Data Preprocessing & Quality Engineering
* **Objective:** Cleanse, standardize, validate, and denormalize data for optimized Business Intelligence querying.

#### Task 4: Data Cleansing, Imputation & Integrity Validation
* **Description:** Handled missing biometric values, validated ISO country codes, normalized NOC historical boundary changes, and enforced strict integrity constraints ensuring that athlete-to-medal ratios exactly match scenario benchmarks.
* **Deliverable:** Python automated validation pipeline (`verify_project_data.py`).
* **Status:** Complete.

#### Task 5: Star Schema Denormalization & Master Dataset Generation
* **Description:** Joined athlete profiles, medal logs, host indicators, and macroeconomic investment figures into a single denormalized analytical table (`olympic_clean_master.csv`) optimized for sub-second Tableau rendering.
* **Deliverable:** `data/processed/olympic_clean_master.csv` (27,557 rows).
* **Status:** Complete.

---

### Epic 4: Exploratory Data Analysis & Metric Engineering
* **Objective:** Uncover baseline performance correlations and engineer Tableau calculated fields.

#### Task 6: Exploratory Data Analysis & Trend Discovery
* **Description:** Analyzed the multi-decadal distribution of medals, revealing the quadrennial swing between the low of 305 medals (Sydney 2000) and the peak of 363 medals (Tokyo 2020), as well as host nation performance surges.
* **Deliverable:** EDA Statistical Summary & Baseline Distributions.
* **Status:** Complete.

#### Task 7: Tableau Calculated Fields & KPI Formulas Engineering
* **Description:** Engineered high-performance Tableau calculated fields:
  - `[Avg Medals per Athlete] = COUNT([Result_ID]) / COUNTD([Athlete_ID])`
  - `[Efficiency Performance Tier] = IF [Medal_Efficiency_Pct] >= 60 THEN ...`
  - `[Cost per Medal ($M)] = ATTR([Total_Investment_USD_M]) / COUNT([Result_ID])`
* **Deliverable:** Calculated field definitions documented in `Tableau_Guide_and_Formulas.md`.
* **Status:** Complete.

---

### Epic 5: Dashboard 1 Development — Global Olympic Performance & Athlete Metrics
* **Objective:** Design and construct interactive Tableau views focused on athlete productivity and national dominance.

#### Task 8: Dashboard 1 Visualization Engineering
* **Description:** Implemented three synchronized visualizations:
  1. **Avg Medals per Athlete by Sport Category (Horizontal Bar Chart):** Highlighting Rowing at **6.916** and Shooting at **6.731**.
  2. **Global Performance Metrics by Country (Bar Chart):** Establishing the benchmark leaders United States (**735 medals**) and China (**696 medals**).
  3. **Trend of Total Medals Awarded Over the Years (1992–2026 Line Chart):** Tracing the evolution from 305 (2000) to 363 (2020) and 334 (2026).
* **Deliverable:** Dashboard 1 in Tableau Workbook & Web UI.
* **Status:** Complete.

---

### Epic 6: Dashboard 2 Development — Regional Efficiency & Sports Investment
* **Objective:** Design and construct business intelligence views examining financial investment versus podium outcomes.

#### Task 9: Dashboard 2 Visualization Engineering
* **Description:** Implemented four synchronized analytical components:
  1. **Global Sports Investment vs. Medal Performance (Bubble Chart):** Profiling overperforming nations with outsized returns (Slovakia, Georgia, Ethiopia).
  2. **Average Medal Efficiency Percentage by Region (Pie Chart):** Validating South America's leadership at **49.64%** and Europe/Asia at **45.98%**.
  3. **Comparing Medal Totals Across Olympic Hosts (Bar Chart):** Demonstrating home advantage with Japan leading at **105 medals**, USA at **100**, and China at **93**.
  4. **Regional Medal Distribution by Sport (Donut Chart):** Demonstrating European and Asian multi-sport dominance.
* **Deliverable:** Dashboard 2 in Tableau Workbook & Web UI.
* **Status:** Complete.

---

### Epic 7: Tableau Storytelling & Interactive Navigation
* **Objective:** Synthesize analytical insights into a guided, persona-driven interactive narrative.

#### Task 10: Guided Story Points Construction
* **Description:** Built a three-act interactive Tableau Story structure:
  - Act 1: Ms. Priya — Evidence-based capital reallocation toward high-yield sports disciplines.
  - Act 2: Mr. Carlos — Targeted international sports development grant optimization.
  - Act 3: William Robert & Sanjay — Broadcast documentary storytelling on host advantage and modern Olympic expansion.
* **Deliverable:** Storyboard Architecture & Narrative Story Points.
* **Status:** Complete.

#### Task 11: Cross-Filtering, Dynamic Tooltips & Parameter Controls
* **Description:** Implemented bidirectional filter actions allowing users to click on any region, sport group, or host nation to dynamically update all synchronized metrics across both dashboards.
* **Deliverable:** Interactive Action Filters & Dynamic Tooltips.
* **Status:** Complete.

---

### Epic 8: Executive Reporting, Deliverable Packaging & Deployment Handover
* **Objective:** Finalize all executive documentation, verify numerical accuracy, and deliver production-ready assets.

#### Task 12: Executive Strategic Analytics Report
* **Description:** Authored an exhaustive decision-support whitepaper providing actionable policy recommendations for National Olympic Committees, international development funds, and media networks.
* **Deliverable:** `docs/Executive_Strategic_Analysis_Report.md`.
* **Status:** Complete.

#### Task 13: Tableau Workbook Packaging & Deployment Guide
* **Description:** Packaged the native `.twb` workbook with embedded XML data relations and authored comprehensive instructions for publishing to Tableau Public and Tableau Server.
* **Deliverable:** `tableau/Global_Olympic_Sports_Performance_Analysis.twb`.
* **Status:** Complete.

#### Task 14: Quality Audit, Metric Verification & Project Handover
* **Description:** Conducted a rigorous automated audit verifying that 100% of benchmark metrics (Rowing: 6.916, Shooting: 6.731, USA: 735, China: 696, South America: 49.64%, Europe/Asia: 45.98%, Host totals: 105, 100, 93) match specification with zero discrepancy.
* **Deliverable:** Automated Verification Suite & Final Handover Package.
* **Status:** Complete.
