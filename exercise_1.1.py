import numpy as np
import pandas as pd

rng = np.random.default_rng()
data = rng.integers(low=70, high=100, size=10, endpoint=True)
index = pd.date_range(start="2025-09-01", periods=10, freq="MS").month_name()
s = pd.Series(data=data, index=index)
print("data:")
print(s)
print()
print(f"mean: {s.mean()}")
print(f"size of first half: {s.loc[:"January"].size}")
mean1 = s.loc[:"January"].mean()
print(f"mean of first half: {mean1}")
print(f"size of second half: {s.loc["February":].size}")
mean2 = s.loc["February":].mean()
print(f"mean of second half: {mean2}")
if mean1 > mean2:
    print("first half was better than second")
else:
    print("second half was better than first")

# beyond
print(f"month with highest score: {s.idxmax()}")
