import pandas as pd

df = pd.read_csv("E:/Python New/#53 Pandas/dummy.csv")

print(df.to_string())# to print this data we will show that in 7 row duration coloum there will a wrong entries, to handle this wrong entries we can do this

#if dataset is small
df.loc[7, "Duration"] = 45 #in the third bracket we will give two argument one is row number and another is which coloum (row number and coloum name)
print(df.to_string())

#if the dataset is big then

for i in df.index:
    if df.loc[i , "Duration"] > 120:
        df.loc[i, "Duration"] = 99
print(df.to_string())


#for removing the rows

for i in df.index:
    if df.loc[i, "Duration"] < 7:
        df.drop(i, inplace=True)
print(df.to_string())