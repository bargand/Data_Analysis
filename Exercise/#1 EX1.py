import numpy as np
import pandas as pd

df = pd.read_csv("E:/Python New/Exercise/Titanic-Dataset.csv")

print(df.to_string())

print(df["Age"].to_string())