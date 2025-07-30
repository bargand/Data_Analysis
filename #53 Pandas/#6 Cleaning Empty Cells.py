import pandas as pd

df = pd.read_csv("E:/Python New/vignaR.csv")
'''
empty_data = df.dropna()

#Note: By default, the dropna() method returns a new DataFrame, and will not change the original.


print(empty_data.to_string())

'''
#using dropna(inplace=True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.

empty_data = df.dropna(inplace= True)

print(df.to_string())