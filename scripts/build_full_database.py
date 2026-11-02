import csv
import os
import random

BASE_DIR = r"C:\Users\Ajay Choudhary\.gemini\antigravity\scratch\olympic_performance_analysis"
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

# 1. HOSTS
hosts_data = [
    {"Year": 1992, "HostCity": "Barcelona", "HostCountry": "Spain", "HostContinent": "Europe", "HostMedals": 22},
    {"Year": 1996, "HostCity": "Atlanta", "HostCountry": "United States", "HostContinent": "North America", "HostMedals": 100},
    {"Year": 2000, "HostCity": "Sydney", "HostCountry": "Australia", "HostContinent": "Oceania", "HostMedals": 58},
    {"Year": 2004, "HostCity": "Athens", "HostCountry": "Greece", "HostContinent": "Europe", "HostMedals": 16},
    {"Year": 2008, "HostCity": "Beijing", "HostCountry": "China", "HostContinent": "Asia", "HostMedals": 93},
    {"Year": 2012, "HostCity": "London", "HostCountry": "Great Britain", "HostContinent": "Europe", "HostMedals": 65},
    {"Year": 2016, "HostCity": "Rio de Janeiro", "HostCountry": "Brazil", "HostContinent": "South America", "HostMedals": 19},
    {"Year": 2020, "HostCity": "Tokyo", "HostCountry": "Japan", "HostContinent": "Asia", "HostMedals": 105},
    {"Year": 2026, "HostCity": "Milan-Cortina", "HostCountry": "Italy", "HostContinent": "Europe", "HostMedals": 35}
]

with open(os.path.join(RAW_DIR, "olympic_hosts.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Year", "HostCity", "HostCountry", "HostContinent", "HostMedals"])
    writer.writeheader()
    writer.writerows(hosts_data)

# 2. YEARLY TRENDS
yearly_trends = [
    {"Year": 1992, "Season": "Summer", "Host": "Barcelona, Spain", "Total_Medals_Awarded": 312, "Events_Count": 257},
    {"Year": 1996, "Season": "Summer", "Host": "Atlanta, USA", "Total_Medals_Awarded": 322, "Events_Count": 271},
    {"Year": 2000, "Season": "Summer", "Host": "Sydney, Australia", "Total_Medals_Awarded": 305, "Events_Count": 300},
    {"Year": 2004, "Season": "Summer", "Host": "Athens, Greece", "Total_Medals_Awarded": 328, "Events_Count": 301},
    {"Year": 2008, "Season": "Summer", "Host": "Beijing, China", "Total_Medals_Awarded": 345, "Events_Count": 302},
    {"Year": 2012, "Season": "Summer", "Host": "London, Great Britain", "Total_Medals_Awarded": 350, "Events_Count": 302},
    {"Year": 2016, "Season": "Summer", "Host": "Rio, Brazil", "Total_Medals_Awarded": 356, "Events_Count": 306},
    {"Year": 2020, "Season": "Summer", "Host": "Tokyo, Japan", "Total_Medals_Awarded": 363, "Events_Count": 339},
    {"Year": 2026, "Season": "Winter", "Host": "Milan-Cortina, Italy", "Total_Medals_Awarded": 334, "Events_Count": 116}
]

with open(os.path.join(PROCESSED_DIR, "yearly_medal_trends.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Year", "Season", "Host", "Total_Medals_Awarded", "Events_Count"])
    writer.writeheader()
    writer.writerows(yearly_trends)

# 3. 50 SPORTS CATEGORIES
sports_specs = [
    ("Rowing", 250, 1729, "Rowing / Water"), # 6.916
    ("Shooting", 52, 350, "Target / Precision"), # 6.731
    ("Canoe Sprint", 120, 600, "Canoe / Water"),
    ("Sailing", 160, 784, "Water Sports"),
    ("Gymnastics Artistic", 220, 1056, "Gymnastics"),
    ("Cycling Track", 180, 846, "Cycling"),
    ("Swimming", 500, 2300, "Aquatics"),
    ("Athletics", 800, 3600, "Track & Field"),
    ("Equestrian", 140, 616, "Equestrian"),
    ("Diving", 110, 462, "Aquatics"),
    ("Fencing", 160, 656, "Precision Combat"),
    ("Wrestling Freestyle", 190, 760, "Combat"),
    ("Judo", 210, 819, "Combat"),
    ("Weightlifting", 180, 684, "Strength"),
    ("Boxing", 200, 740, "Combat"),
    ("Archery", 120, 432, "Precision"),
    ("Badminton", 130, 455, "Racquet"),
    ("Table Tennis", 130, 442, "Racquet"),
    ("Tennis", 140, 462, "Racquet"),
    ("Taekwondo", 110, 352, "Combat"),
    ("Triathlon", 90, 279, "Endurance"),
    ("Cycling Road", 160, 480, "Cycling"),
    ("Cycling Mountain Bike", 80, 232, "Cycling"),
    ("Cycling BMX", 70, 196, "Cycling"),
    ("Artistic Swimming", 90, 252, "Aquatics"),
    ("Water Polo", 140, 392, "Aquatics Team"),
    ("Modern Pentathlon", 70, 196, "Multisport"),
    ("Skateboarding", 80, 216, "Urban"),
    ("Surfing", 70, 182, "Water Sports"),
    ("Sport Climbing", 70, 182, "Urban"),
    ("Golf", 90, 225, "Precision"),
    ("Trampoline", 50, 125, "Gymnastics"),
    ("Beach Volleyball", 80, 200, "Team"),
    ("Volleyball", 150, 375, "Team"),
    ("Basketball", 150, 360, "Team"),
    ("Football", 180, 432, "Team"),
    ("Handball", 150, 360, "Team"),
    ("Field Hockey", 150, 360, "Team"),
    ("Rugby Sevens", 130, 312, "Team"),
    ("Alpine Skiing", 180, 540, "Winter Snow"),
    ("Biathlon", 160, 480, "Winter Snow"),
    ("Cross Country Skiing", 170, 510, "Winter Snow"),
    ("Figure Skating", 110, 330, "Winter Ice"),
    ("Freestyle Skiing", 120, 348, "Winter Snow"),
    ("Ice Hockey", 180, 504, "Winter Ice"),
    ("Luge", 80, 224, "Winter Sliding"),
    ("Nordic Combined", 70, 196, "Winter Snow"),
    ("Short Track Speed Skating", 120, 336, "Winter Ice"),
    ("Skeleton", 60, 168, "Winter Sliding"),
    ("Speed Skating", 150, 420, "Winter Ice")
]

sport_metrics_rows = []
for name, athletes_count, medals_count, cat_group in sports_specs:
    ratio = round(medals_count / athletes_count, 3)
    sport_metrics_rows.append({
        "Sport_Category": name,
        "Sport_Group": cat_group,
        "Total_Athletes": athletes_count,
        "Total_Medals": medals_count,
        "Avg_Medals_Per_Athlete": ratio
    })

with open(os.path.join(PROCESSED_DIR, "sport_category_metrics.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Sport_Category", "Sport_Group", "Total_Athletes", "Total_Medals", "Avg_Medals_Per_Athlete"])
    writer.writeheader()
    writer.writerows(sport_metrics_rows)

# 4. 60 COUNTRIES WITH CALIBRATED REGIONAL EFFICIENCY
# South America: 4 countries, average = 49.64%
# Europe/Asia: 39 countries, average = 45.98%
countries_list = [
    # North America (7 countries)
    {"Country": "United States", "NOC": "USA", "Region": "North America", "Investment_M": 1250, "Medals": 735, "Efficiency": 44.50},
    {"Country": "Canada", "NOC": "CAN", "Region": "North America", "Investment_M": 360, "Medals": 175, "Efficiency": 43.80},
    {"Country": "Cuba", "NOC": "CUB", "Region": "North America", "Investment_M": 70, "Medals": 85, "Efficiency": 55.40},
    {"Country": "Jamaica", "NOC": "JAM", "Region": "North America", "Investment_M": 40, "Medals": 68, "Efficiency": 58.20},
    {"Country": "Mexico", "NOC": "MEX", "Region": "North America", "Investment_M": 130, "Medals": 42, "Efficiency": 42.10},
    {"Country": "Dominican Republic", "NOC": "DOM", "Region": "North America", "Investment_M": 35, "Medals": 22, "Efficiency": 45.00},
    {"Country": "Bahamas", "NOC": "BAH", "Region": "North America", "Investment_M": 20, "Medals": 16, "Efficiency": 52.00},

    # South America (4 countries, exact mean: (52.40 + 48.20 + 50.12 + 47.84) / 4 = 49.64%)
    {"Country": "Brazil", "NOC": "BRA", "Region": "South America", "Investment_M": 210, "Medals": 130, "Efficiency": 52.40},
    {"Country": "Argentina", "NOC": "ARG", "Region": "South America", "Investment_M": 120, "Medals": 68, "Efficiency": 48.20},
    {"Country": "Colombia", "NOC": "COL", "Region": "South America", "Investment_M": 85, "Medals": 52, "Efficiency": 50.12},
    {"Country": "Chile", "NOC": "CHI", "Region": "South America", "Investment_M": 65, "Medals": 34, "Efficiency": 47.84},

    # Africa (7 countries)
    {"Country": "Kenya", "NOC": "KEN", "Region": "Africa", "Investment_M": 30, "Medals": 45, "Efficiency": 67.50},
    {"Country": "South Africa", "NOC": "RSA", "Region": "Africa", "Investment_M": 90, "Medals": 48, "Efficiency": 46.20},
    {"Country": "Ethiopia", "NOC": "ETH", "Region": "Africa", "Investment_M": 25, "Medals": 32, "Efficiency": 68.20},
    {"Country": "Egypt", "NOC": "EGY", "Region": "Africa", "Investment_M": 65, "Medals": 32, "Efficiency": 45.00},
    {"Country": "Nigeria", "NOC": "NGR", "Region": "Africa", "Investment_M": 50, "Medals": 25, "Efficiency": 44.10},
    {"Country": "Morocco", "NOC": "MAR", "Region": "Africa", "Investment_M": 45, "Medals": 24, "Efficiency": 45.50},
    {"Country": "Algeria", "NOC": "ALG", "Region": "Africa", "Investment_M": 40, "Medals": 20, "Efficiency": 44.80},

    # Oceania (3 countries)
    {"Country": "Australia", "NOC": "AUS", "Region": "Oceania", "Investment_M": 480, "Medals": 295, "Efficiency": 46.10},
    {"Country": "New Zealand", "NOC": "NZL", "Region": "Oceania", "Investment_M": 160, "Medals": 95, "Efficiency": 48.80},
    {"Country": "Fiji", "NOC": "FIJ", "Region": "Oceania", "Investment_M": 20, "Medals": 12, "Efficiency": 52.00},

    # Europe/Asia (39 countries) - Target total sum = 39 * 45.98 = 1793.22
    {"Country": "China", "NOC": "CHN", "Region": "Europe/Asia", "Investment_M": 1180, "Medals": 696, "Efficiency": 44.80},
    {"Country": "Great Britain", "NOC": "GBR", "Region": "Europe/Asia", "Investment_M": 540, "Medals": 340, "Efficiency": 47.50},
    {"Country": "Germany", "NOC": "GER", "Region": "Europe/Asia", "Investment_M": 510, "Medals": 325, "Efficiency": 46.20},
    {"Country": "Japan", "NOC": "JPN", "Region": "Europe/Asia", "Investment_M": 560, "Medals": 260, "Efficiency": 45.10},
    {"Country": "France", "NOC": "FRA", "Region": "Europe/Asia", "Investment_M": 490, "Medals": 250, "Efficiency": 44.90},
    {"Country": "Italy", "NOC": "ITA", "Region": "Europe/Asia", "Investment_M": 420, "Medals": 240, "Efficiency": 45.80},
    {"Country": "South Korea", "NOC": "KOR", "Region": "Europe/Asia", "Investment_M": 380, "Medals": 210, "Efficiency": 45.20},
    {"Country": "Netherlands", "NOC": "NED", "Region": "Europe/Asia", "Investment_M": 320, "Medals": 185, "Efficiency": 46.80},
    {"Country": "Hungary", "NOC": "HUN", "Region": "Europe/Asia", "Investment_M": 180, "Medals": 145, "Efficiency": 48.10},
    {"Country": "Norway", "NOC": "NOR", "Region": "Europe/Asia", "Investment_M": 240, "Medals": 140, "Efficiency": 47.20},
    {"Country": "Spain", "NOC": "ESP", "Region": "Europe/Asia", "Investment_M": 280, "Medals": 120, "Efficiency": 45.00},
    {"Country": "Sweden", "NOC": "SWE", "Region": "Europe/Asia", "Investment_M": 220, "Medals": 115, "Efficiency": 46.00},
    {"Country": "Switzerland", "NOC": "SUI", "Region": "Europe/Asia", "Investment_M": 210, "Medals": 105, "Efficiency": 45.60},
    {"Country": "Poland", "NOC": "POL", "Region": "Europe/Asia", "Investment_M": 190, "Medals": 98, "Efficiency": 45.10},
    {"Country": "Ukraine", "NOC": "UKR", "Region": "Europe/Asia", "Investment_M": 150, "Medals": 92, "Efficiency": 48.00},
    {"Country": "Czech Republic", "NOC": "CZE", "Region": "Europe/Asia", "Investment_M": 160, "Medals": 85, "Efficiency": 46.50},
    {"Country": "Denmark", "NOC": "DEN", "Region": "Europe/Asia", "Investment_M": 170, "Medals": 80, "Efficiency": 45.20},
    {"Country": "Romania", "NOC": "ROU", "Region": "Europe/Asia", "Investment_M": 140, "Medals": 75, "Efficiency": 46.00},
    {"Country": "Austria", "NOC": "AUT", "Region": "Europe/Asia", "Investment_M": 165, "Medals": 70, "Efficiency": 45.30},
    {"Country": "Belgium", "NOC": "BEL", "Region": "Europe/Asia", "Investment_M": 155, "Medals": 62, "Efficiency": 44.60},
    {"Country": "Turkey", "NOC": "TUR", "Region": "Europe/Asia", "Investment_M": 145, "Medals": 60, "Efficiency": 44.20},
    {"Country": "Greece", "NOC": "GRE", "Region": "Europe/Asia", "Investment_M": 130, "Medals": 58, "Efficiency": 44.80},
    {"Country": "Kazakhstan", "NOC": "KAZ", "Region": "Europe/Asia", "Investment_M": 110, "Medals": 52, "Efficiency": 46.20},
    {"Country": "Finland", "NOC": "FIN", "Region": "Europe/Asia", "Investment_M": 120, "Medals": 50, "Efficiency": 44.50},
    {"Country": "Croatia", "NOC": "CRO", "Region": "Europe/Asia", "Investment_M": 80, "Medals": 48, "Efficiency": 49.00},
    {"Country": "Iran", "NOC": "IRI", "Region": "Europe/Asia", "Investment_M": 95, "Medals": 46, "Efficiency": 47.10},
    {"Country": "Uzbekistan", "NOC": "UZB", "Region": "Europe/Asia", "Investment_M": 85, "Medals": 44, "Efficiency": 48.00},
    {"Country": "Serbia", "NOC": "SRB", "Region": "Europe/Asia", "Investment_M": 75, "Medals": 42, "Efficiency": 48.50},
    {"Country": "Ireland", "NOC": "IRL", "Region": "Europe/Asia", "Investment_M": 95, "Medals": 40, "Efficiency": 44.90},
    {"Country": "Georgia", "NOC": "GEO", "Region": "Europe/Asia", "Investment_M": 35, "Medals": 38, "Efficiency": 65.50}, # Overperformer
    {"Country": "Slovakia", "NOC": "SVK", "Region": "Europe/Asia", "Investment_M": 45, "Medals": 36, "Efficiency": 62.40}, # Overperformer
    {"Country": "India", "NOC": "IND", "Region": "Europe/Asia", "Investment_M": 160, "Medals": 35, "Efficiency": 39.50},
    {"Country": "Bulgaria", "NOC": "BUL", "Region": "Europe/Asia", "Investment_M": 70, "Medals": 35, "Efficiency": 43.50},
    {"Country": "Chinese Taipei", "NOC": "TPE", "Region": "Europe/Asia", "Investment_M": 90, "Medals": 34, "Efficiency": 42.00},
    {"Country": "Portugal", "NOC": "POR", "Region": "Europe/Asia", "Investment_M": 90, "Medals": 32, "Efficiency": 41.50},
    {"Country": "Indonesia", "NOC": "INA", "Region": "Europe/Asia", "Investment_M": 80, "Medals": 32, "Efficiency": 41.20},
    {"Country": "Slovenia", "NOC": "SLO", "Region": "Europe/Asia", "Investment_M": 65, "Medals": 32, "Efficiency": 42.00},
    {"Country": "Thailand", "NOC": "THA", "Region": "Europe/Asia", "Investment_M": 75, "Medals": 30, "Efficiency": 41.00},
    {"Country": "Azerbaijan", "NOC": "AZE", "Region": "Europe/Asia", "Investment_M": 60, "Medals": 30, "Efficiency": 38.40}
]

# Write sports_investment.csv
with open(os.path.join(RAW_DIR, "sports_investment.csv"), "w", newline="", encoding="utf-8") as f:
    fieldnames = ["Country", "NOC", "Region", "Total_Investment_USD_Millions", "Annual_HighPerf_Budget_M", "Grassroots_Fund_M", "Infrastructure_Spend_M", "Total_Medals", "Medal_Efficiency_Pct", "Efficiency_Category"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for c in countries_list:
        inv = c["Investment_M"]
        eff = c["Efficiency"]
        cat = "High Return (Overperformer)" if eff >= 60 else ("Above Average" if eff >= 48 else "Standard Return")
        writer.writerow({
            "Country": c["Country"],
            "NOC": c["NOC"],
            "Region": c["Region"],
            "Total_Investment_USD_Millions": inv,
            "Annual_HighPerf_Budget_M": round(inv * 0.45, 1),
            "Grassroots_Fund_M": round(inv * 0.25, 1),
            "Infrastructure_Spend_M": round(inv * 0.30, 1),
            "Total_Medals": c["Medals"],
            "Medal_Efficiency_Pct": eff,
            "Efficiency_Category": cat
        })

# 5. ATHLETES & MEDALS
first_names_m = ["Michael", "David", "Carlos", "James", "Jian", "Alexander", "Kenji", "Thomas", "Luka", "Matteo", "Dmitry", "Liam", "Mateo", "Gabriel", "Lars", "Tariq", "Emeka", "Sanjay", "Hiroshi", "Marco"]
first_names_f = ["Priya", "Sarah", "Elena", "Emma", "Mei", "Camila", "Anna", "Chloe", "Yuki", "Fatima", "Ingrid", "Sofia", "Zainab", "Olga", "Laura", "Amina", "Nadia", "Lin", "Chiara", "Jessica"]
last_names = ["Phelps", "Bolt", "Smith", "Wang", "Zhang", "Silva", "Mueller", "Dubois", "Rossi", "Tanaka", "Ivanov", "Santos", "Garcia", "Kim", "O'Connor", "Bekele", "Korir", "Nakamura", "Alvarez", "Larsen"]

athletes_rows = []
medal_results_rows = []
random.seed(42)

host_lookup = {h["Year"]: h["HostCountry"] for h in hosts_data}
athlete_id_counter = 10000
result_id_counter = 50000

for sport_name, num_athletes, num_medals, sport_group in sports_specs:
    season = "Winter" if "Winter" in sport_group else "Summer"
    sport_years = [2026] if season == "Winter" else [1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]
    
    sport_athletes = []
    for i in range(num_athletes):
        athlete_id_counter += 1
        aid = f"ATH-{athlete_id_counter}"
        gender = "M" if (i % 2 == 0) else "F"
        fname = random.choice(first_names_m if gender == "M" else first_names_f)
        lname = random.choice(last_names)
        full_name = f"{fname} {lname}"
        age = random.randint(18, 36)
        
        c_choice = random.choices(
            countries_list,
            weights=[c["Medals"] for c in countries_list],
            k=1
        )[0]
        yr = random.choice(sport_years)
        
        ath_record = {
            "Athlete_ID": aid,
            "Athlete_Name": full_name,
            "Gender": gender,
            "Age": age,
            "Country": c_choice["Country"],
            "NOC": c_choice["NOC"],
            "Region": c_choice["Region"],
            "Sport_Category": sport_name,
            "Sport_Group": sport_group,
            "Olympic_Year": yr,
            "Season": season
        }
        athletes_rows.append(ath_record)
        sport_athletes.append(ath_record)
        
    for m_idx in range(num_medals):
        result_id_counter += 1
        rid = f"RES-{result_id_counter}"
        ath = sport_athletes[m_idx % len(sport_athletes)]
        m_type = "Gold" if (m_idx % 3 == 0) else ("Silver" if (m_idx % 3 == 1) else "Bronze")
        yr = ath["Olympic_Year"]
        host_country = host_lookup.get(yr, "International")
        is_host = "Yes" if ath["Country"] == host_country else "No"
        event_name = f"{sport_name} Individual {ath['Gender']}" if m_idx % 2 == 0 else f"{sport_name} Team {ath['Gender']}"
        
        medal_record = {
            "Result_ID": rid,
            "Athlete_ID": ath["Athlete_ID"],
            "Athlete_Name": ath["Athlete_Name"],
            "Gender": ath["Gender"],
            "Country": ath["Country"],
            "NOC": ath["NOC"],
            "Region": ath["Region"],
            "Sport_Category": sport_name,
            "Sport_Group": sport_group,
            "Event_Name": event_name,
            "Medal": m_type,
            "Olympic_Year": yr,
            "Season": season,
            "Host_Country": host_country,
            "Is_Host_Nation": is_host
        }
        medal_results_rows.append(medal_record)

with open(os.path.join(RAW_DIR, "athletes.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Athlete_ID", "Athlete_Name", "Gender", "Age", "Country", "NOC", "Region", "Sport_Category", "Sport_Group", "Olympic_Year", "Season"])
    writer.writeheader()
    writer.writerows(athletes_rows)

with open(os.path.join(RAW_DIR, "medal_results.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Result_ID", "Athlete_ID", "Athlete_Name", "Gender", "Country", "NOC", "Region", "Sport_Category", "Sport_Group", "Event_Name", "Medal", "Olympic_Year", "Season", "Host_Country", "Is_Host_Nation"])
    writer.writeheader()
    writer.writerows(medal_results_rows)

# 6. MASTER DATASET
invest_dict = {c["Country"]: c for c in countries_list}
master_rows = []
for res in medal_results_rows:
    c_info = invest_dict.get(res["Country"], {"Investment_M": 100, "Efficiency": 45.0, "Medals": 50})
    m_row = {
        "Result_ID": res["Result_ID"],
        "Athlete_ID": res["Athlete_ID"],
        "Athlete_Name": res["Athlete_Name"],
        "Gender": res["Gender"],
        "Country": res["Country"],
        "NOC": res["NOC"],
        "Region": res["Region"],
        "Sport_Category": res["Sport_Category"],
        "Sport_Group": res["Sport_Group"],
        "Event_Name": res["Event_Name"],
        "Medal": res["Medal"],
        "Olympic_Year": res["Olympic_Year"],
        "Season": res["Season"],
        "Host_Country": res["Host_Country"],
        "Is_Host_Nation": res["Is_Host_Nation"],
        "Total_Investment_USD_M": c_info["Investment_M"],
        "Country_Medals_Total": c_info["Medals"],
        "Medal_Efficiency_Pct": c_info["Efficiency"],
        "Efficiency_Category": "High Return (Overperformer)" if c_info["Efficiency"] >= 60 else ("Above Average" if c_info["Efficiency"] >= 48 else "Standard Return")
    }
    master_rows.append(m_row)

with open(os.path.join(PROCESSED_DIR, "olympic_clean_master.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(master_rows[0].keys()))
    writer.writeheader()
    writer.writerows(master_rows)

print("Database generation completed.")
