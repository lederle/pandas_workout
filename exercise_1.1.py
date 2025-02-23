import numpy as np
import pandas as pd

rng = np.random.default_rng()
data = rng.integers(low=70, high=100, size=10, endpoint=True)
index = pd.date_range(start="2025-09-01", periods=10, freq="MS").month_name()
s = pd.Series(data=data, index=index)
print("data:")
print(s)
print()
print("mean: ", s.mean())
print("size of first half: ", s[:"January"].size)
mean1 = s[:"January"].mean()
print("mean of first half: ", mean1)
print("size of second half: ", s["February":].size)
mean2 = s["February":].mean()
print("mean of second half: ", mean2)
if mean1 > mean2:
    print("first half was better than second")
else:
    print("second half was better than first")
