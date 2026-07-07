# clash-royale-analysis

**What does it take to win in Clash Royale?** 

Is it determined by elixir cost or rarity of a given card?
Or maybe, it is a 3rd, more sinister option (a credit card).

Nevertheless, I wanted to find out and there is only one way to satiate this thirst for knowledge: Data!

---

For this project, I will be using **Python**, **Pandas** for Data Manipulation / Analytics, and **Matplotlib** for Data Visualization. 
This data is publicly available on [Kaggle](https://www.kaggle.com/datasets/hrish4/clash-royale-cards-data)

---

## How to Run it Locally:
- Make sure you have python installed
- Install pandas (**pip install pandas**)
- Download the dataset from the Kaggle link above and put it in the same folder as analysis.py
- Then, run **py analysis.py** in your terminal from that folder

---

## Findings
- Cards with higher rarity also have slightly higher win rates
- Low Elixir Cards (1-4 Elixir) have a higher win rate than High Elixir Cards (5-9 Elixir)
- Rarity has the highest correlation in determining the best predictor of win rate
- Aerial cards average approximately 1% higher win rate than grounded cards, though this may be partially explained by aerial cards skewing toward higher rarities rather than the aerial attribute itself.

Developed by _Keifer Kolar_
