import pandas as pd

df = pd.read_csv("E:/Python New/vignaR.csv")

'''
#Calculate mean

cal_mean = round(df["Duration"].mean())
cal_mean2 = round(df["Calories"].mean())

print(cal_mean)
print(cal_mean2)
'''
'''
#calculate median

cal_median = round(df["Calories"].median())
print(cal_median)
'''

#calculate mode

cal_mode = df["Duration"].mode()[0]
print(cal_mode)