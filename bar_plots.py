import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(font_scale=1.2)
sns.set_style('whitegrid')
sns.set_palette('Paired')

top_btm = pd.read_csv("data/top_btm.csv", index_col=0)
top_mkt = pd.read_csv("data/top_mkt.csv", index_col=0)
mkt_btm = pd.read_csv("data/mkt_btm.csv", index_col=0)

x = np.array(["Top - Bottom", "Top - Market", "Market - bottom"])
x_position = np.array([0, 1.6, 3.2])

fct = "beta"

y_hi = np.array([top_btm[fct + "_hi"].values[-1],
                 top_mkt[fct + "_hi"].values[-1],
                 mkt_btm[fct + "_hi"].values[-1]])
y_mid = np.array([top_btm[fct + "_mid"].values[-1],
                  top_mkt[fct + "_mid"].values[-1],
                  mkt_btm[fct + "_mid"].values[-1]])
y_lo = np.array([top_btm[fct + "_lo"].values[-1],
                 top_mkt[fct + "_lo"].values[-1],
                 mkt_btm[fct + "_lo"].values[-1]])

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1)
ax.bar(x_position, y_hi, width=0.4, label='High', color="red")
ax.bar(x_position + 0.4, y_mid, width=0.4, label='Mid', color="grey")
ax.bar(x_position + 0.8, y_lo, width=0.4, label='Low', color="blue")

ax.legend()
ax.set_title("Cometric")
ax.set_ylabel('Cumulative Return')
ax.set_xticks(x_position + 0.4)
ax.set_xticklabels(x)
plt.show()
