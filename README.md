# 🏏 Athlete Management Intelligence System (AMIS)

A data-driven evaluation prototype built in Python to bridge the gap between technical data logic and sports talent management. This system calculates a standardized **Athlete Valuation Score** by mathematically balancing on-field cricket metrics with off-field digital brand metrics.

---

## 🚀 Core Business Logic

Instead of judging every player the same way, this system handles multiple player roles dynamically so athletes are rated fairly based on their actual playing discipline:

* **Batters:** Evaluated heavily on volume of runs and scoring efficiency.
* **Bowlers:** Graded on wickets taken and economy rate optimization (lower economy yields higher rewards).
* **All-Rounders:** Evaluated on a balanced, dual-discipline mathematical distribution.

### 📊 Standardized Weightage Architecture
The system uses a **60/40 Weighted Split** to determine final market value:
* **60% On-Field Performance:** Processing raw cricket match statistics.
* **40% Off-Field Brand Power:** Social media reach scaled using **Logarithmic Curves** (`math.log10`) paired with live audience engagement percentages. This safeguard prevents viral digital influencers with weak athletic form from scoring higher than elite national athletes.

---

## 📈 Live Portal Analytics Output

When executed, the intelligence engine generates the following real-time corporate talent report roster:

| Player Name    | Playing Role  | Valuation Score | Key Metric Focus |
| :---           | :---          | :---            | :---             |
| **Tilak Varma**| Batter        | **57.4 / 100** | High Engagement (11.9%) |
| **Jasprit Bumrah**| Bowler     | **65.9 / 100** | Elite Economy Control (6.8) |
| **Hardik Pandya**| All-Rounder  | **61.3 / 100** | Balanced Multi-Discipline Reach |

---

## 💡 Sports Management Use Case
This system provides corporate talent agents with data-backed transparency when pitching athletes to premier lifestyle and commercial brands (e.g., Puma, Dream11, boAt). Instead of relying on emotional gut-feeling, managers can present algorithmic ROI probabilities to corporate brand directors.
