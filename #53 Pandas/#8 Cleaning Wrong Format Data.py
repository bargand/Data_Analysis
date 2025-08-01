import pandas as pd

df = pd.read_csv("E:/Python New/#53 Pandas/dummy.csv")

#using date_time format we can we can clean the data
df["Date"] = pd.to_datetime(df["Date"] , format='mixed')

print(df)

#we can specifically remove one cell from coloum and row

df.dropna(subset="Date", inplace=True) # this way we can specify which cell data have to be deleted
print(df)