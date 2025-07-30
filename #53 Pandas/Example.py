import pandas as pd
import numpy as np

df = pd.read_csv("E:/Python New/vignaR.csv")

a = df.to_string()

print(np.array(a[1]))