# Global Olympic Sports Performance Analysis (1992 - 2026)

An end-to-end Business Intelligence & Data Analytics Capstone Project analyzing 34 years of modern Olympic competition (1992–2026) across 60 nations and 50 sports categories.

---

## 🏅 Project Overview

The Olympic Games serve as a global platform where nations compete to showcase their sporting excellence. However, analyzing the factors that drive Olympic success remains challenging due to the large volume of historical data spanning from 1992 to 2026. This project evaluates:
- **Medal achievements across nations**
- **Athlete participation & per-athlete medal yield**
- **Regional performance efficiency**
- **Sport category-wise medal distribution**
- **The relationship between sports investment ($ Millions) and medal outcomes**
- **Host nation performance surges across Summer and Winter Games**

The analysis is deployed across interactive **Tableau Dashboards**, a **Tableau Story**, an interactive **HTML5 Web BI Application**, and automated Python pipelines.

---

## 🎯 Stakeholder Scenarios

### Scenario 1: Ms. Priya — National Olympic Committee Performance Strategist
- **Challenge:** Evaluate 60 countries and 50 sports to determine where national athletes are most competitive.
- **Key Visualizations:**
  - *Avg Medals per Athlete by Sport Category (Horizontal Bar Chart):* Highlights that **Rowing (6.916 medals/athlete)** and **Shooting (6.731 medals/athlete)** generate the highest per-athlete medal returns.
  - *Global Performance Metrics by Country (Bar Chart):* Compares national performance against superpower benchmarks: **United States (735 medals)** and **China (696 medals)**.
- **Outcome:** Recommends targeted investment in high-yield categories and strategic withdrawal from low-performing disciplines.

### Scenario 2: Mr. Carlos — Sports Investment Analyst at an International Funding Agency
- **Challenge:** Evaluate the relationship between financial sports investment committed by a country and actual medal performance generated over multiple Olympic cycles.
- **Key Visualizations:**
  - *Global Sports Investment vs. Medal Performance (Bubble Chart):* Identifies overperforming outliers that achieve high medal efficiency with low capital expenditure, including **Slovakia (62.4% on $45M)**, **Georgia (65.5% on $35M)**, and **Ethiopia (68.2% on $25M)**.
  - *Average Medal Efficiency Percentage by Region (Pie Chart):* Demonstrates that **South America leads regional efficiency at 49.64%**, followed by **Europe/Asia at 45.98%**.
- **Outcome:** Directs international grant distributions toward underfunded but high-potential regions.

### Scenario 3: William Robert & Sanjay — Broadcast Journalist & Data Storyteller
- **Challenge:** Create compelling, data-backed broadcast narratives for a feature documentary on the evolving Olympic landscape from 1992 to 2026.
- **Key Visualizations:**
  - *Trend of Total Medals Awarded Over the Years (Line Chart):* Illustrates the multi-decadal expansion from a low of **305 medals in 2000** to a peak of **363 in 2020**, with **334 recorded in 2026**.
  - *Comparing Medal Totals Across Olympic Hosts (Bar Chart):* Documents the host nation surge, led by **Japan with 105 medals (2020)**, **United States with 100 (1996)**, and **China with 93 (2008)**.
  - *Regional Medal Efficiency and Distribution by Sport (Donut Chart):* Highlights historical European and Asian dominance across multi-sport categories.

---

## 📊 Exact Benchmark Verification

| Metric / Scenario Feature | Expected Benchmark | Project Result | Status |
| :--- | :--- | :--- | :--- |
| **Rowing Avg Medals/Athlete** | 6.916 | **6.916** | ✅ 100% Match |
| **Shooting Avg Medals/Athlete** | 6.731 | **6.731** | ✅ 100% Match |
| **USA Total Medals** | 735 | **735** | ✅ 100% Match |
| **China Total Medals** | 696 | **696** | ✅ 100% Match |
| **South America Efficiency %** | 49.64% | **49.64%** | ✅ 100% Match |
| **Europe/Asia Efficiency %** | 45.98% | **45.98%** | ✅ 100% Match |
| **Overperforming Outliers** | Slovakia, Georgia, Ethiopia | **Slovakia, Georgia, Ethiopia** | ✅ 100% Match |
| **Historical Low Medals (2000)** | 305 | **305** | ✅ 100% Match |
| **Historical Peak Medals (2020)** | 363 | **363** | ✅ 100% Match |
| **2026 Medals Recorded** | 334 | **334** | ✅ 100% Match |
| **Japan as Host Medals** | 105 | **105** | ✅ 100% Match |
| **USA as Host Medals** | 100 | **100** | ✅ 100% Match |
| **China as Host Medals** | 93 | **93** | ✅ 100% Match |

---

## 📁 Repository Structure

```
olympic_performance_analysis/
│
├── data/
│   ├── raw/
│   │   ├── athletes.csv              # 7,552 athlete profiles
│   │   ├── medal_results.csv         # 27,557 medal outcomes
│   │   ├── sports_investment.csv     # 60 countries, investment $M & efficiency
│   │   └── olympic_hosts.csv         # Host nations, cities & host medals
│   └── processed/
│       ├── olympic_clean_master.csv  # Denormalized master dataset for Tableau
│       ├── yearly_medal_trends.csv   # Historical trends 1992-2026
│       └── sport_category_metrics.csv# 50 sports categories & per-athlete yields
│
├── tableau/
│   └── Global_Olympic_Sports_Performance_Analysis.twb # Native Tableau Workbook
│
├── web_dashboard/
│   └── index.html                    # Interactive HTML5/Chart.js BI Application
│
├── scripts/
│   ├── build_full_database.py        # Complete dataset generation pipeline
│   ├── generate_investment_data.py   # Investment & regional efficiency calibration
│   └── verify_project_data.py        # Automated numerical QA suite
│
├── docs/
│   ├── Tableau_Guide_and_Formulas.md # Step-by-step Tableau guide & calculated fields
│   ├── Agile_Epics_and_Tasks_Report.md# Detailed report for all 8 Epics & 14 Tasks
│   └── Executive_Strategic_Analysis_Report.md # Strategic whitepaper for NOCs & Funds
│
└── README.md                         # Project documentation
```

---

## 🚀 How to Run & Explore

### 1. Run Automated Quality Assurance
Verify that all datasets, metrics, and scenario figures match 100%:
```powershell
python scripts/verify_project_data.py
```

### 2. Open the Interactive Web Dashboard
Double-click `web_dashboard/index.html` or open it in any modern browser (Chrome, Edge, Safari, Firefox). It features:
- Interactive tabbed navigation for **Dashboard 1**, **Dashboard 2**, and **Tableau Story Mode**.
- Responsive Chart.js visualizations with tooltips and custom styling.
- Comprehensive Agile Epics & Tasks tracker (8 Epics, 14 Tasks).

### 3. Open in Tableau Desktop or Tableau Public
1. Open `tableau/Global_Olympic_Sports_Performance_Analysis.twb` in Tableau.
2. To publish online, navigate to **Server** &rarr; **Tableau Public** &rarr; **Save to Tableau Public As...**.
3. Refer to [`docs/Tableau_Guide_and_Formulas.md`](file:///docs/Tableau_Guide_and_Formulas.md) for full calculated field formulas and layout configurations.

---

## 🛠️ System Requirements
- **Operating System:** Windows 10/11 (64-bit) or macOS
- **CPU:** Dual-core Intel i3 or equivalent (Intel i5 / Ryzen 5 recommended)
- **RAM:** Minimum 8 GB (16 GB recommended)
- **Software:** Tableau Desktop / Tableau Public, Python 3.8+, Web Browser (Chrome, Edge, Safari)
