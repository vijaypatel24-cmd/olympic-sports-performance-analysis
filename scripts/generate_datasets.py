import csv
import os
import random

# Base directory
BASE_DIR = r"C:\Users\Ajay Choudhary\.gemini\antigravity\scratch\olympic_performance_analysis"
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

# 1. Host dataset definition matching exact scenario specifications:
# Japan as host: 105 medals
# United States as host: 100 medals
# China as host: 93 medals
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

# Write olympic_hosts.csv
hosts_path = os.path.join(RAW_DIR, "olympic_hosts.csv")
with open(hosts_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Year", "HostCity", "HostCountry", "HostContinent", "HostMedals"])
    writer.writeheader()
    writer.writerows(hosts_data)

# 2. Trend of Total Medals Awarded Over the Years:
# Must include exact specifications:
# Year 2000: 305 medals (historical low)
# Year 2020: 363 medals (historical peak)
# Year 2026: 334 medals
# 8 years/cycles in scope: 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2026 (or 1992-2026)
yearly_medal_totals = {
    1992: 315,
    1996: 325,
    2000: 305, # Exact low
    2004: 328,
    2008: 345,
    2012: 350,
    2016: 358,
    2020: 363, # Exact peak
    2026: 334  # Exact 2026 recorded
}

# 3. Sports categories: 50 sports categories
# Exactly Rowing at 6.916 and Shooting at 6.731 avg medals per athlete!
# Let Rowing athletes = 250, medals = 1729 -> 1729 / 250 = 6.916!
# Let Shooting athletes = 26, medals = 175 -> 175 / 26 = 6.730769... rounds to 6.731!
# Or athletes = 52, medals = 350 -> 6.731.
# Or athletes = 1000, medals = 6731 -> 6.731 exact!
# Let's define the 50 sports categories with realistic medal counts and athletes.
sports_definitions = [
    ("Rowing", 250, 1729, "Rowing"), # 6.916
    ("Shooting", 100, 673, "Shooting"), # 673 / 100 = 6.73 -> Let's make it exactly 6.731 by using 175 medals / 26 athletes = 6.73077 (6.731)
    ("Athletics", 800, 3200, "Track & Field"), # 4.000
    ("Swimming", 600, 2520, "Aquatics"), # 4.200
    ("Gymnastics", 300, 1350, "Gymnastics"), # 4.500
    ("Cycling", 350, 1470, "Cycling"), # 4.200
    ("Sailing", 200, 960, "Water Sports"), # 4.800
    ("Canoe/Kayak", 220, 990, "Water Sports"), # 4.500
    ("Wrestling", 280, 1120, "Combat"), # 4.000
    ("Judo", 250, 1000, "Combat"), # 4.000
    ("Boxing", 240, 960, "Combat"), # 4.000
    ("Fencing", 180, 720, "Precision/Combat"), # 4.000
    ("Archery", 150, 570, "Precision"), # 3.800
    ("Weightlifting", 200, 760, "Strength"), # 3.800
    ("Equestrian", 160, 640, "Equestrian"), # 4.000
    ("Badminton", 140, 490, "Racquet"), # 3.500
    ("Table Tennis", 140, 490, "Racquet"), # 3.500
    ("Tennis", 150, 450, "Racquet"), # 3.000
    ("Taekwondo", 120, 420, "Combat"), # 3.500
    ("Triathlon", 100, 320, "Endurance"), # 3.200
    ("Volleyball", 180, 540, "Team"), # 3.000
    ("Basketball", 180, 540, "Team"), # 3.000
    ("Football", 200, 600, "Team"), # 3.000
    ("Field Hockey", 180, 540, "Team"), # 3.000
    ("Handball", 180, 540, "Team"), # 3.000
    ("Water Polo", 160, 480, "Aquatics/Team"), # 3.000
    ("Rugby Sevens", 150, 450, "Team"), # 3.000
    ("Modern Pentathlon", 80, 240, "Multisport"), # 3.000
    ("Skateboarding", 90, 270, "Urban"), # 3.000
    ("Surfing", 80, 240, "Water Sports"), # 3.000
    ("Sport Climbing", 80, 240, "Urban"), # 3.000
    ("Golf", 100, 280, "Precision"), # 2.800
    ("Diving", 120, 360, "Aquatics"), # 3.000
    ("Artistic Swimming", 100, 300, "Aquatics"), # 3.000
    ("Trampoline", 60, 180, "Gymnastics"), # 3.000
    ("Beach Volleyball", 80, 240, "Team"), # 3.000
    ("Alpine Skiing", 200, 680, "Winter Snow"), # 3.400
    ("Biathlon", 180, 630, "Winter Snow"), # 3.500
    ("Cross Country Skiing", 190, 665, "Winter Snow"), # 3.500
    ("Figure Skating", 120, 420, "Winter Ice"), # 3.500
    ("Freestyle Skiing", 140, 462, "Winter Snow"), # 3.300
    ("Ice Hockey", 200, 600, "Winter Ice"), # 3.000
    ("Luge", 90, 270, "Winter Sliding"), # 3.000
    ("Nordic Combined", 80, 240, "Winter Snow"), # 3.000
    ("Short Track Speed Skating", 130, 429, "Winter Ice"), # 3.300
    ("Skeleton", 70, 210, "Winter Sliding"), # 3.000
    ("Ski Jumping", 110, 352, "Winter Snow"), # 3.200
    ("Snowboard", 140, 448, "Winter Snow"), # 3.200
    ("Speed Skating", 160, 528, "Winter Ice"), # 3.300
    ("Bobsleigh", 120, 384, "Winter Sliding")  # 3.200
]

# Notice Shooting: 175 medals / 26 athletes = 6.730769 -> rounds to 6.731!
# Or athletes = 52, medals = 350 -> 6.730769 -> rounds to 6.731!
# Let's adjust Shooting in the list:
sports_definitions[1] = ("Shooting", 52, 350, "Precision")

print(f"Total sports configured: {len(sports_definitions)}")
print(f"Rowing ratio: {1729 / 250:.3f}")
print(f"Shooting ratio: {350 / 52:.3f}")
