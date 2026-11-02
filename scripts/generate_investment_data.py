import csv
import os
import json

BASE_DIR = r"C:\Users\Ajay Choudhary\.gemini\antigravity\scratch\olympic_performance_analysis"
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")

# 1. 60 Countries with exact regional classification & investment metrics
# South America: 4 nations whose mean Medal_Efficiency_Pct is exactly 49.64%
# (52.40 + 48.20 + 50.12 + 47.84) / 4 = 49.64%
# Europe/Asia: mean Medal_Efficiency_Pct is exactly 45.98%
# Overperforming bubble outliers: Slovakia, Georgia, Ethiopia

countries_data = [
    # Top Giants
    {"Country": "United States", "NOC": "USA", "Region": "North America", "Investment_M": 1250, "Medals": 735, "Efficiency": 44.50},
    {"Country": "China", "NOC": "CHN", "Region": "Europe/Asia", "Investment_M": 1180, "Medals": 696, "Efficiency": 44.80},
    {"Country": "Great Britain", "NOC": "GBR", "Region": "Europe/Asia", "Investment_M": 540, "Medals": 340, "Efficiency": 47.50},
    {"Country": "Germany", "NOC": "GER", "Region": "Europe/Asia", "Investment_M": 510, "Medals": 325, "Efficiency": 46.20},
    {"Country": "Australia", "NOC": "AUS", "Region": "Oceania", "Investment_M": 480, "Medals": 295, "Efficiency": 46.10},
    {"Country": "Japan", "NOC": "JPN", "Region": "Europe/Asia", "Investment_M": 560, "Medals": 260, "Efficiency": 45.10},
    {"Country": "France", "NOC": "FRA", "Region": "Europe/Asia", "Investment_M": 490, "Medals": 250, "Efficiency": 44.90},
    {"Country": "Italy", "NOC": "ITA", "Region": "Europe/Asia", "Investment_M": 420, "Medals": 240, "Efficiency": 45.80},
    {"Country": "South Korea", "NOC": "KOR", "Region": "Europe/Asia", "Investment_M": 380, "Medals": 210, "Efficiency": 45.20},
    {"Country": "Netherlands", "NOC": "NED", "Region": "Europe/Asia", "Investment_M": 320, "Medals": 185, "Efficiency": 46.80},
    {"Country": "Canada", "NOC": "CAN", "Region": "North America", "Investment_M": 360, "Medals": 175, "Efficiency": 43.80},
    {"Country": "Hungary", "NOC": "HUN", "Region": "Europe/Asia", "Investment_M": 180, "Medals": 145, "Efficiency": 48.10},
    
    # South America (Average exactly 49.64%)
    {"Country": "Brazil", "NOC": "BRA", "Region": "South America", "Investment_M": 210, "Medals": 130, "Efficiency": 52.40},
    {"Country": "Argentina", "NOC": "ARG", "Region": "South America", "Investment_M": 120, "Medals": 68, "Efficiency": 48.20},
    {"Country": "Colombia", "NOC": "COL", "Region": "South America", "Investment_M": 85, "Medals": 52, "Efficiency": 50.12},
    {"Country": "Chile", "NOC": "CHI", "Region": "South America", "Investment_M": 65, "Medals": 34, "Efficiency": 47.84},
    
    # Overperforming Bubble Outliers (Low Investment, Disproportionately High Efficiency)
    {"Country": "Slovakia", "NOC": "SVK", "Region": "Europe/Asia", "Investment_M": 45, "Medals": 36, "Efficiency": 62.40},
    {"Country": "Georgia", "NOC": "GEO", "Region": "Europe/Asia", "Investment_M": 35, "Medals": 38, "Efficiency": 65.50},
    {"Country": "Ethiopia", "NOC": "ETH", "Region": "Africa", "Investment_M": 25, "Medals": 32, "Efficiency": 68.20},
    {"Country": "Kenya", "NOC": "KEN", "Region": "Africa", "Investment_M": 30, "Medals": 45, "Efficiency": 67.50},

    # Additional Europe/Asia nations carefully calibrated to hit EXACTLY 45.98% average!
    {"Country": "Spain", "NOC": "ESP", "Region": "Europe/Asia", "Investment_M": 280, "Medals": 120, "Efficiency": 45.00},
    {"Country": "Sweden", "NOC": "SWE", "Region": "Europe/Asia", "Investment_M": 220, "Medals": 115, "Efficiency": 46.00},
    {"Country": "Norway", "NOC": "NOR", "Region": "Europe/Asia", "Investment_M": 240, "Medals": 140, "Efficiency": 47.20},
    {"Country": "Switzerland", "NOC": "SUI", "Region": "Europe/Asia", "Investment_M": 210, "Medals": 105, "Efficiency": 45.60},
    {"Country": "Poland", "NOC": "POL", "Region": "Europe/Asia", "Investment_M": 190, "Medals": 98, "Efficiency": 45.10},
    {"Country": "Czech Republic", "NOC": "CZE", "Region": "Europe/Asia", "Investment_M": 160, "Medals": 85, "Efficiency": 46.50},
    {"Country": "Romania", "NOC": "ROU", "Region": "Europe/Asia", "Investment_M": 140, "Medals": 75, "Efficiency": 46.00},
    {"Country": "Ukraine", "NOC": "UKR", "Region": "Europe/Asia", "Investment_M": 150, "Medals": 92, "Efficiency": 48.00},
    {"Country": "Denmark", "NOC": "DEN", "Region": "Europe/Asia", "Investment_M": 170, "Medals": 80, "Efficiency": 45.20},
    {"Country": "Greece", "NOC": "GRE", "Region": "Europe/Asia", "Investment_M": 130, "Medals": 58, "Efficiency": 44.80},
    {"Country": "Belgium", "NOC": "BEL", "Region": "Europe/Asia", "Investment_M": 155, "Medals": 62, "Efficiency": 44.60},
    {"Country": "Austria", "NOC": "AUT", "Region": "Europe/Asia", "Investment_M": 165, "Medals": 70, "Efficiency": 45.30},
    {"Country": "Croatia", "NOC": "CRO", "Region": "Europe/Asia", "Investment_M": 80, "Medals": 48, "Efficiency": 49.00},
    {"Country": "Serbia", "NOC": "SRB", "Region": "Europe/Asia", "Investment_M": 75, "Medals": 42, "Efficiency": 48.50},
    {"Country": "Turkey", "NOC": "TUR", "Region": "Europe/Asia", "Investment_M": 145, "Medals": 60, "Efficiency": 44.20},
    {"Country": "Ireland", "NOC": "IRL", "Region": "Europe/Asia", "Investment_M": 95, "Medals": 40, "Efficiency": 44.90},
    {"Country": "Portugal", "NOC": "POR", "Region": "Europe/Asia", "Investment_M": 90, "Medals": 32, "Efficiency": 43.80},
    {"Country": "Finland", "NOC": "FIN", "Region": "Europe/Asia", "Investment_M": 120, "Medals": 50, "Efficiency": 44.50},
    {"Country": "India", "NOC": "IND", "Region": "Europe/Asia", "Investment_M": 160, "Medals": 35, "Efficiency": 39.50},
    {"Country": "Kazakhstan", "NOC": "KAZ", "Region": "Europe/Asia", "Investment_M": 110, "Medals": 52, "Efficiency": 46.20},
    {"Country": "Uzbekistan", "NOC": "UZB", "Region": "Europe/Asia", "Investment_M": 85, "Medals": 44, "Efficiency": 48.00},
    {"Country": "Iran", "NOC": "IRI", "Region": "Europe/Asia", "Investment_M": 95, "Medals": 46, "Efficiency": 47.10},
    {"Country": "Indonesia", "NOC": "INA", "Region": "Europe/Asia", "Investment_M": 80, "Medals": 32, "Efficiency": 43.20},
    {"Country": "Chinese Taipei", "NOC": "TPE", "Region": "Europe/Asia", "Investment_M": 90, "Medals": 34, "Efficiency": 44.00},
    {"Country": "Thailand", "NOC": "THA", "Region": "Europe/Asia", "Investment_M": 75, "Medals": 30, "Efficiency": 43.50},
    {"Country": "Bulgaria", "NOC": "BUL", "Region": "Europe/Asia", "Investment_M": 70, "Medals": 35, "Efficiency": 46.80},
    {"Country": "Slovenia", "NOC": "SLO", "Region": "Europe/Asia", "Investment_M": 65, "Medals": 32, "Efficiency": 47.50},
    {"Country": "Azerbaijan", "NOC": "AZE", "Region": "Europe/Asia", "Investment_M": 60, "Medals": 30, "Efficiency": 47.00},
    
    # Other North America
    {"Country": "Mexico", "NOC": "MEX", "Region": "North America", "Investment_M": 130, "Medals": 42, "Efficiency": 42.10},
    {"Country": "Cuba", "NOC": "CUB", "Region": "North America", "Investment_M": 70, "Medals": 85, "Efficiency": 55.40},
    {"Country": "Jamaica", "NOC": "JAM", "Region": "North America", "Investment_M": 40, "Medals": 68, "Efficiency": 58.20},
    {"Country": "Dominican Republic", "NOC": "DOM", "Region": "North America", "Investment_M": 35, "Medals": 22, "Efficiency": 45.00},

    # Other Africa
    {"Country": "South Africa", "NOC": "RSA", "Region": "Africa", "Investment_M": 90, "Medals": 48, "Efficiency": 46.20},
    {"Country": "Egypt", "NOC": "EGY", "Region": "Africa", "Investment_M": 65, "Medals": 32, "Efficiency": 45.00},
    {"Country": "Nigeria", "NOC": "NGR", "Region": "Africa", "Investment_M": 50, "Medals": 25, "Efficiency": 44.10},
    {"Country": "Morocco", "NOC": "MAR", "Region": "Africa", "Investment_M": 45, "Medals": 24, "Efficiency": 45.50},
    {"Country": "Algeria", "NOC": "ALG", "Region": "Africa", "Investment_M": 40, "Medals": 20, "Efficiency": 44.80},

    # Oceania
    {"Country": "New Zealand", "NOC": "NZL", "Region": "Oceania", "Investment_M": 160, "Medals": 95, "Efficiency": 48.80},
    {"Country": "Fiji", "NOC": "FIJ", "Region": "Oceania", "Investment_M": 20, "Medals": 12, "Efficiency": 52.00}
]

# Adjust Europe/Asia efficiencies slightly to ensure the mean is EXACTLY 45.98%
ea_nations = [c for c in countries_data if c["Region"] == "Europe/Asia"]
current_ea_sum = sum(c["Efficiency"] for c in ea_nations)
target_ea_sum = round(45.98 * len(ea_nations), 2)
diff = round(target_ea_sum - current_ea_sum, 2)
ea_nations[0]["Efficiency"] = round(ea_nations[0]["Efficiency"] + diff, 2)

# Check South America
sa_nations = [c for c in countries_data if c["Region"] == "South America"]
sa_avg = sum(c["Efficiency"] for c in sa_nations) / len(sa_nations)

# Check Europe/Asia
ea_avg = sum(c["Efficiency"] for c in ea_nations) / len(ea_nations)

print(f"Total countries configured: {len(countries_data)}")
print(f"South America Avg Efficiency: {sa_avg:.2f}% (Expected: 49.64%)")
print(f"Europe/Asia Avg Efficiency: {ea_avg:.2f}% (Expected: 45.98%)")

# Write sports_investment.csv
investment_path = os.path.join(RAW_DIR, "sports_investment.csv")
with open(investment_path, "w", newline="", encoding="utf-8") as f:
    fieldnames = ["Country", "NOC", "Region", "Total_Investment_USD_Millions", "Annual_HighPerf_Budget_M", "Grassroots_Fund_M", "Infrastructure_Spend_M", "Total_Medals", "Medal_Efficiency_Pct", "Efficiency_Category"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for c in countries_data:
        inv = c["Investment_M"]
        eff = c["Efficiency"]
        cat = "High Return (Overperformer)" if eff >= 55 else ("Moderate Return" if eff >= 45 else "Developing Return")
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

print("sports_investment.csv generated successfully.")
