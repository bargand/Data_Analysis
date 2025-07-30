import pandas as pd

df = pd.read_csv("E:/Python New/vignaR.csv")

'''
#if the dataframe is very big then just print the data we will see the first 5 and last 5 data frame
print(df)

#use to_string() function for showing the entire data
print(df.to_string()) 
'''

print(pd.options.display.max_rows) #it will return 60 because if we print the data then if the data is bigger than 60 then printed data is first 5 and last 5 rows, and if the data is less or equal to 60 then the printed data is full.

#we can increase the data structure like this

pd.options.display.max_rows = 9999 # then the printed data is full

print(df)