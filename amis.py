import math

# --- STEP 1: DEFINE HOW TO CALCULATE SCORES ---
def evaluate_athlete_value(role, runs, wickets, economy, followers, engagement):
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

# --- STEP 2: ATHLETE REGISTRY ---
athlete_registry = [
    {"name": "Tilak Varma", "role": "Batter", "runs": 1858, "wickets": 0, "economy": 0, "followers": 6500000, "engagement": 11.9},
    {"name": "Jasprit Bumrah", "role": "Bowler", "runs": 50, "wickets": 165, "economy": 6.8, "followers": 12000000, "engagement": 3.2},
    {"name": "Hardik Pandya", "role": "All-Rounder", "runs": 2955, "wickets": 82, "economy": 8.1, "followers": 28000000, "engagement": 5.1}
]

# --- STEP 3: PRINT THE RESULTS DASHBOARD ---
print("\n=======================================================")
print("       TALENT ROSTER ANALYTICS ENGINE    ")
print("=======================================================")
print(f"{'Player Name':<16} | {'Role':<12} | {'Valuation Score'}")
print("-------------------------------------------------------")

for athlete in athlete_registry:
    final_score = evaluate_athlete_value(
        athlete["role"], athlete["runs"], athlete["wickets"], 
        athlete["economy"], athlete["followers"], athlete["engagement"]
    )
    print(f"{athlete['name']:<16} | {athlete['role']:<12} | {final_score} / 100")

print("=======================================================\n")
      
