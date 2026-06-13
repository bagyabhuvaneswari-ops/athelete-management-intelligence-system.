import math

# --- STEP 1: DEFINE HOW TO CALCULATE SCORES ---
def calculate_metrics(role, runs, wickets, economy, followers, engagement):
    # Calculate on-field sports performance
    if role == "Batter":
        performance_score = (runs / 50) + 20
    elif role == "Bowler":
        performance_score = (wickets * 0.4) + ((10 - economy) * 5)
    elif role == "All-Rounder":
        performance_score = (runs / 100) + (wickets * 0.5)
        
    # Calculate off-field social media brand power
    social_reach = math.log10(followers) * 10 if followers > 0 else 0
    brand_power = (social_reach * 0.5) + (engagement * 2)
    
    # Final combined score out of 100 max
    total_score = (performance_score * 0.6) + (brand_power * 0.4)
    return round(min(total_score, 100), 1)

# --- STEP 2: ENTER THE PLAYER DATA ---
players_roster = [
    {"name": "Tilak Varma", "role": "Batter", "runs": 1858, "wickets": 0, "economy": 0, "followers": 6500000, "engagement": 11.9},
    {"name": "Jasprit Bumrah", "role": "Bowler", "runs": 50, "wickets": 165, "economy": 6.8, "followers": 12000000, "engagement": 3.2},
    {"name": "Hardik Pandya", "role": "All-Rounder", "runs": 2955, "wickets": 82, "economy": 8.1, "followers": 28000000, "engagement": 5.1}
]

# --- STEP 3: PRINT THE RESULTS DASHBOARD ---
print("\n=======================================================")
print("       RISE WORLDWIDE - TALENT INTELLIGENCE PORTAL     ")
print("=======================================================")
print(f"{'Player Name':<16} | {'Role':<12} | {'Valuation Score'}")
print("-------------------------------------------------------")

for p in players_roster:
    final_score = calculate_metrics(
        p["role"], p["runs"], p["wickets"], 
        p["economy"], p["followers"], p["engagement"]
    )
    print(f"{p['name']:<16} | {p['role']:<12} | {final_score} / 100")

print("=======================================================\n")
      
