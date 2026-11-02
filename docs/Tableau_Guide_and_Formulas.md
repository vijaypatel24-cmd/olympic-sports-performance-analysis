# Tableau Implementation Guide & Calculated Field Formulas
**Project:** Global Olympic Sports Performance Analysis (1992 - 2026)  
**Target BI Platforms:** Tableau Desktop (2020.1+) / Tableau Public / Tableau Cloud  
**Primary Dataset:** `data/processed/olympic_clean_master.csv`  

---

## 1. Connecting Data in Tableau

1. Launch **Tableau Desktop** or **Tableau Public**.
2. Under **Connect** &rarr; Select **Text file**.
3. Navigate to and select `data/processed/olympic_clean_master.csv`.
4. In the Data Source pane:
   - Confirm fields and data types:
     - `Result_ID` (String)
     - `Athlete_ID` (String)
     - `Country` (String - Geographic Role: Country/Region)
     - `NOC` (String)
     - `Region` (String)
     - `Sport_Category` (String)
     - `Event_Name` (String)
     - `Medal` (String)
     - `Olympic_Year` (Number / Integer)
     - `Season` (String)
     - `Host_Country` (String - Geographic Role: Country/Region)
     - `Is_Host_Nation` (String)
     - `Total_Investment_USD_M` (Number / Decimal)
     - `Country_Medals_Total` (Number / Integer)
     - `Medal_Efficiency_Pct` (Number / Decimal)
     - `Efficiency_Category` (String)

---

## 2. Calculated Fields & DAX / Tableau Formulas

Create the following calculated fields by right-clicking in the Data Pane &rarr; **Create Calculated Field**:

### Calculation 1: Avg Medals per Athlete
```tableau
// Name: [Avg Medals per Athlete]
// Purpose: Calculates average medal haul per unique competing athlete in a sport
COUNT([Result_ID]) / COUNTD([Athlete_ID])
```

### Calculation 2: Efficiency Performance Tier
```tableau
// Name: [Efficiency Performance Tier]
// Purpose: Classifies countries into efficiency brackets for bubble chart encoding
IF [Medal_Efficiency_Pct] >= 60.0 THEN "Top Overperformer (High Yield)"
ELSEIF [Medal_Efficiency_Pct] >= 48.0 THEN "Above Average Yield"
ELSE "Standard Yield"
END
```

### Calculation 3: Host Nation Medal Count
```tableau
// Name: [Host Medals Won]
// Purpose: Isolates medals won exclusively during host years
SUM(IF [Is_Host_Nation] = "Yes" THEN 1 ELSE 0 END)
```

### Calculation 4: Investment per Medal Ratio ($M)
```tableau
// Name: [Cost per Medal ($M)]
// Purpose: Financial return metric measuring dollars spent per podium finish
ATTR([Total_Investment_USD_M]) / COUNT([Result_ID])
```

---

## 3. Worksheet Build Instructions

### Worksheet 1: Avg Medals per Athlete by Sport Category (Scenario 1: Priya)
- **Chart Type:** Horizontal Bar Chart
- **Rows:** `[Sport_Category]`
- **Columns:** `[Avg Medals per Athlete]`
- **Sort:** Descending by `[Avg Medals per Athlete]`
- **Color:** `[Avg Medals per Athlete]` (Diverging Blue-Amber)
- **Verified Values:**
  - **Rowing:** 6.916 medals/athlete
  - **Shooting:** 6.731 medals/athlete
  - **Canoe Sprint:** 5.000 medals/athlete
  - **Sailing:** 4.900 medals/athlete
- **Tooltip:**
  ```text
  Sport: <Sport_Category>
  Category Group: <Sport_Group>
  Total Unique Athletes: <COUNTD(Athlete_ID)>
  Total Medals Won: <COUNT(Result_ID)>
  Avg Medals per Athlete: <AGG(Avg Medals per Athlete)>
  ```

### Worksheet 2: Global Performance Metrics by Country
- **Chart Type:** Bar Chart
- **Rows:** `[Country]` (or filtered to Top 15)
- **Columns:** `SUM([Country_Medals_Total])` or `COUNT([Result_ID])`
- **Color:** `[Region]`
- **Verified Values:**
  - **United States:** 735 medals
  - **China:** 696 medals
  - **Great Britain:** 340 medals
  - **Germany:** 325 medals
  - **Australia:** 295 medals

### Worksheet 3: Trend of Total Medals Awarded Over the Years (1992 - 2026) (Scenario 3: William)
- **Chart Type:** Line & Area Chart
- **Columns:** `[Olympic_Year]` (Discrete / Dimension)
- **Rows:** `COUNT([Result_ID])` (or `[Total_Medals_Awarded]` from `yearly_medal_trends.csv`)
- **Key Trend Milestones:**
  - **2000 (Sydney):** 305 medals (Historical Low)
  - **2020 (Tokyo):** 363 medals (Modern Peak)
  - **2026 (Milano-Cortina):** 334 medals (Recorded 2026 Winter cycle)
- **Annotations:** Add callout annotations at 2000, 2020, and 2026.

### Worksheet 4: Global Sports Investment vs. Medal Performance (Scenario 2: Carlos)
- **Chart Type:** Bubble / Scatter Plot
- **Columns:** `AVG([Total_Investment_USD_M])` (X-Axis: Sports Investment)
- **Rows:** `COUNT([Result_ID])` or `AVG([Country_Medals_Total])` (Y-Axis: Total Medals)
- **Detail:** `[Country]`
- **Size:** `AVG([Medal_Efficiency_Pct])`
- **Color:** `[Efficiency Performance Tier]`
- **Key Outliers Highlighted:**
  - **Slovakia:** $45M investment &rarr; 36 medals &rarr; 62.4% efficiency
  - **Georgia:** $35M investment &rarr; 38 medals &rarr; 65.5% efficiency
  - **Ethiopia:** $25M investment &rarr; 32 medals &rarr; 68.2% efficiency

### Worksheet 5: Average Medal Efficiency Percentage by Region
- **Chart Type:** Pie / Donut Chart
- **Color:** `[Region]`
- **Angle / Size:** `AVG([Medal_Efficiency_Pct])`
- **Label:** `[Region]`, `AVG([Medal_Efficiency_Pct])` formatted as Percentage
- **Verified Values:**
  - **South America:** 49.64% (Regional Efficiency Leader)
  - **Europe/Asia:** 45.98%
  - **Africa:** 51.61%
  - **Oceania:** 48.97%
  - **North America:** 48.71%

### Worksheet 6: Comparing Medal Totals Across Olympic Hosts
- **Chart Type:** Horizontal Bar Chart
- **Rows:** `[Host_Country]`
- **Columns:** `SUM([HostMedals])` (from `olympic_hosts.csv`)
- **Sort:** Descending
- **Verified Values:**
  - **Japan (Tokyo 2020):** 105 medals
  - **United States (Atlanta 1996):** 100 medals
  - **China (Beijing 2008):** 93 medals
  - **Great Britain (London 2012):** 65 medals
  - **Australia (Sydney 2000):** 58 medals
  - **Italy (Milan-Cortina 2026):** 35 medals
  - **Spain (Barcelona 1992):** 22 medals
  - **Brazil (Rio 2016):** 19 medals
  - **Greece (Athens 2004):** 16 medals

### Worksheet 7: Regional Medal Efficiency and Distribution by Sport
- **Chart Type:** Donut Chart or Treemap
- **Color:** `[Region]`
- **Size:** `COUNT([Result_ID])`
- **Narrative Focus:** Demonstrates historical European & Asian dominance across multi-sport categories.

---

## 4. Dashboard Assembly & Interactivity

### Dashboard 1: Global Olympic Performance & Athlete Metrics
- **Size:** Fixed 1400 x 900 px (or Automatic)
- **Components:**
  - Top: Header banner with Title & KPI summary cards.
  - Left: `Avg Medals per Athlete by Sport Category` (with Sport Group filter).
  - Right: `Global Performance Metrics by Country`.
  - Bottom: `Trend of Total Medals Awarded Over the Years (1992 - 2026)`.
- **Dashboard Actions:**
  - Set `Sport_Category` as Filter Action to update athlete rosters and country totals on click.

### Dashboard 2: Olympic Performance & Regional Efficiency
- **Size:** Fixed 1400 x 900 px
- **Components:**
  - Top Left: `Global Sports Investment vs. Medal Performance (Bubble Plot)`.
  - Top Right: `Average Medal Efficiency Percentage by Region (Pie Chart)`.
  - Bottom Left: `Comparing Medal Totals Across Olympic Hosts (Bar Chart)`.
  - Bottom Right: `Regional Medal Distribution by Sport (Donut Chart)`.
- **Dashboard Actions:**
  - Set `Region` filter action to highlight bubble plot and sport distribution.

---

## 5. Tableau Story Points Workflow

Create a **Tableau Story** with three dedicated Story Points:

1. **Story Point 1: Ms. Priya — National Olympic Committee Strategist**
   - Embed Dashboard 1 with focus on Rowing (6.916) and Shooting (6.731).
   - Caption: *"Evidence-based capital allocation: High-yield sports category prioritization against global leaders USA (735) and China (696)."*
2. **Story Point 2: Mr. Carlos — International Sports Funding Analyst**
   - Embed Dashboard 2 highlighting South America (49.64%) and bubble outliers Slovakia, Georgia, Ethiopia.
   - Caption: *"Smarter grant distribution: Identifying capital-constrained, high-yield nations that outperform heavy spenders."*
3. **Story Point 3: William Robert — Broadcast Documentary Narrative**
   - Embed Host Comparison & 1992–2026 Trend (swing from 305 in 2000 to 363 in 2020, and 334 in 2026).
   - Caption: *"The Host Nation Surge: Japan (105), USA (100), and China (93) demonstrate the dramatic home podium effect."*

---

## 6. How to Publish to Tableau Public

1. In Tableau Desktop, click **Server** in the top menu &rarr; **Tableau Public** &rarr; **Save to Tableau Public As...**.
2. Sign in with your free Tableau Public account credentials.
3. Name your workbook: `Global_Olympic_Sports_Performance_Analysis_1992_2026`.
4. Click **Save**. Tableau will compile extracts and launch your live interactive dashboard in your web browser.
5. Copy the embed link or shareable URL for project submission.
