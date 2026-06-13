# Athlete Management Intelligence System (AMIS)

This is a Python prototype I built to help analyze and evaluate cricket players for a sports talent agency setup. The project blends on-field cricket statistics with social media brand engagement metrics to calculate a final "Valuation Score" out of 100 for any player.

## How the Logic Works

Instead of judging every player by the same metrics, the code looks at the player's specific role so the scoring stays fair:

* **Batters:** Judged mainly on total career runs.
* **Bowlers:** Evaluated on total wickets taken balanced against their economy rate (lower economy gives a better score).
* **All-Rounders:** Takes a balanced mix of both runs and wickets.

### The 60/40 Formula Split
To calculate the final score, the script splits the weightage:
1.  **60% On-Field Stats:** Raw performance based on their match numbers.
2.  **40% Off-Field Brand Power:** Instagram follower counts combined with their engagement rate. 

*Note: I used math.log10 to scale down the followers. This prevents someone with massive social media numbers (like Virat Kohli) from completely breaking the 100-point limit and overriding actual match performance.*

---

## Sample Output Results

When you run the script, it automatically calculates and prints out this table roster:

| Player Name | Playing Role | Valuation Score | Notes |
| :--- | :--- | :--- | :--- |
| **Tilak Varma** | Batter | **57.4 / 100** | Massive boost from 11.9% engagement |
| **Jasprit Bumrah** | Bowler | **65.9 / 100** | High score due to low economy rate |
| **Hardik Pandya** | All-Rounder | **61.3 / 100** | Balanced across both skills |

---

## Why I Built This (Use Case)
As a BCA student aspiring to transition into sports management, I built this prototype to show how mordern talent managers can leverage basic software logic to streamline sports business operations. In sports management, determining an athlete's commercial value or pitch fee shouldn't rely on guesswork. This project proves how a manager can use structured logic to backup multi-lakh contract negotiations, balance brand expectations, and present clear, data-backed ROI probabilities to corporate brand directors
