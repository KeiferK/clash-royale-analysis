# Clash Royale Analysis of 2025 Data Set (https://www.kaggle.com/datasets/hrish4/clash-royale-cards-data)
# By: Keifer Kolar


# Charts and Visualizations COMING SOON! -> import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("clash_royale_cards.csv")

plt.style.use('dark_background')

# Test
#print(df.head())

#================= General Knowledge =================

# General Knowledge #1: Which 5 cards have the highest win rate?

best = df.nlargest(5, "Win Rate")[["Card", "Win Rate", "rarity", "elixirCost"]]
print("\nTop 5 Cards with the highest win rate:\n", best.to_string())


# General Knowledge #2: Which 5 cards have the lowest win rate?

worst = df.nsmallest(5, "Win Rate")[["Card", "Win Rate", "rarity", "elixirCost"]]
print("\nBottom 5 Cards with the lowest win rate:\n", worst.to_string())


#================= Questions =================

# Question #1: Do higher rarity cards have higher win rates?

print("\nQuestion #1: Do higher rarity cards have higher win rates?\n")

rarity_winrate = df.groupby("rarity")["Win Rate"].mean().sort_values(ascending=False)
print(rarity_winrate)


# Q1 Graph

q1graph_colors = ['gold', 'cyan', 'purple', 'orange', 'blue']

plt.bar(rarity_winrate.index, rarity_winrate.values, color=q1graph_colors)

plt.title("Win Rate by Rarity")
plt.xlabel("Rarity")
plt.ylabel("Win Rate")
plt.ylim(50, 57)
plt.show()


# Question #2: Do higher elixir cards have better win rates?

print("\nQuestion #2: Do higher elixir cards have better win rates?\n")

low_elixir_win_rate = df[df["elixirCost"] <= 4]["Win Rate"].mean()
high_elixir_win_rate = df[df["elixirCost"] >= 5]["Win Rate"].mean()

print("Low Elixir (1-4 Elixir): ", low_elixir_win_rate)
print("High Elixir (5-9 Elixir): ", high_elixir_win_rate)

# Q2 Graph
q2graph_colors = ['Pink', 'Purple']

plt.bar(["Low Elixir (0-4)", "High Elixir (5-9)"], [low_elixir_win_rate, high_elixir_win_rate], color=q2graph_colors)

plt.title("Win Rate by High and Low Elixir Cost Cards")
plt.xlabel("Elixir Cost")
plt.ylabel("Win Rate")
plt.ylim(50, 55)
plt.show()


# Question #3: What is the best predictor of win rate?

print("\nQuestion #3: What is the best predictor of win rate?\n")

correlation = df[["elixirCost", "Usage", "Win Rate"]].corr()
print(correlation)

# Extra work needed to analyze rarity and whether it affects win rate
rarity_order = {"common": 1, "rare": 2, "epic": 3, "legendary": 4, "champion": 5}
df["rarity_numeric"] = df["rarity"].map(rarity_order)

correlation = df[["elixirCost", "Usage", "rarity_numeric", "Win Rate"]].corr()
predictors = correlation["Win Rate"].drop("Win Rate").sort_values(ascending=False)
print("\nWin Rate Correlations (sorted):\n", predictors.to_string())

# Q3 Graph
q3graph_colors = ['red', 'blue', 'green']

plt.bar(predictors.index, predictors.values, color=q3graph_colors)

plt.title("What is the Best Predictor of Win Rate?")
plt.xlabel("Predictors")
plt.ylabel("Win Rate")
plt.ylim(-0.1, 0.3)
plt.axhline(y=0, color='white', linewidth=1)
plt.show()