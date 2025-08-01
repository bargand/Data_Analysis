import pandas as pd

df = pd.read_csv("E:/Python New/#53 Pandas/dummy.csv")

print(df.duplicated()) # check if there is duplicate or not

#we weill seen that in 12 number row one duplication found,  now we drop the duplicate row

df.drop_duplicates(inplace=True)
print(df.to_string())