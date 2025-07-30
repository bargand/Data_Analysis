import pandas as pd

'''
data analysis is support only csv file ot in json file
'''

df = pd.read_csv("E:/Python New/vignaR.csv")

print(df.info())
'''
'''
#for extract first 5 row
print(df.head())

#for extract first 15 row
print(df.head(15))

#for extra last 5 row
print(df.tail())

#for extract last 17 row
print(df.tail(17))