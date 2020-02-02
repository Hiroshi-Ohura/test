"""
Comparison among factors

Overlap rates in the following tables are computed to compare timing of high/low
crowdedness level across countries of the same factor

Overlap rate:
the number of dates when both factors in each pair have the same crowdedness level /
the number of all dates

Comparison among regions and countries

Similarly, overlap rates in the following tables were computed to compare timing
of high/low crowdedness level across factors for a given universe
"""

import matplotlib.pyplot as plt
import pandas as pd
import itertools
import seaborn as sns

df = pd.read_csv("data/quote.csv")
df_ret = df[["date", "USD", "EUR", "GBP", "CAD"]].set_index("date").pct_change(1)
df_ret = df_ret.dropna()
num_all = len(df_ret)

df_ret["USD"] = df_ret["USD"].apply(
    lambda x: -1 if x < -0.005 else (1 if x > 0.005 else 0))
df_ret["EUR"] = df_ret["EUR"].apply(
    lambda x: -1 if x < -0.005 else (1 if x > 0.005 else 0))
df_ret["GBP"] = df_ret["GBP"].apply(
    lambda x: -1 if x < -0.005 else (1 if x > 0.005 else 0))
df_ret["CAD"] = df_ret["CAD"].apply(
    lambda x: -1 if x < -0.005 else (1 if x > 0.005 else 0))

country_list = ["USD", "EUR", "GBP", "CAD"]

df_overlap = pd.DataFrame(index=country_list, columns=country_list)

for v in itertools.combinations_with_replacement(country_list, 2):
    num_comb = sum(df_ret[v[0]] == df_ret[v[1]])
    overlap_rate = num_comb / num_all
    df_overlap[v[0]][v[1]] = overlap_rate

fig = plt.figure(figsize=(20, 10))
for i in range(0, 3):
    ax = fig.add_subplot(1, 3, i+1)
    sns.heatmap(df_overlap.astype(float), annot=True, cmap='Blues',
                vmin=0, vmax=1, cbar=False, square=True)

plt.title("Overlap Rate")
plt.tight_layout()
plt.show()

