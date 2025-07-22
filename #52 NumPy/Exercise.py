import numpy as np
'''
1, Stock Prices: Extract Weekly Closing Values
Given a NumPy array of daily stock prices for a year (252 trading days), extract the closing price of every Friday (assume day 0 is a Monday).
'''
'''

sales = np.round(np.random.uniform(100,200,365))
print(sales)

print(sales[4::7])
'''

'''
2. Weather Station: Temperature Above Threshold
You have hourly temperature data for a month (30 days × 24 hours). Extract all values where temperature > 35°C.
'''
'''
# temp = np.round(np.random.uniform(0,50,(30,24)))

temp = np.array([
 [36, 16, 46, 18, 14, 48,  9, 34, 27, 44,  7, 45, 45, 10, 42,  1, 32, 40,
  41, 39, 43, 14, 27, 25],
 [33, 23, 32, 20, 49, 11, 30, 43, 14, 32, 31, 45, 12,  5, 32, 40, 45, 15,
  33, 41, 27, 25,  6, 45],
 [ 9, 42,  4, 42,  6, 18, 17, 21,  1,  1, 46, 23, 36,  4, 31, 22, 15, 13,
  38, 35, 28, 42, 43, 16],
 [21, 44, 35, 17, 34, 25, 30, 37,  4,  6, 43, 24,  5, 17, 46, 44, 27, 19,
  30, 23, 34,  2,  5, 43],
 [29, 20, 15, 12, 23,  4, 33, 32, 40, 22, 27, 46, 39, 27, 47, 46, 34, 37,
  13, 46, 14,  6, 33, 28],
 [32,  6, 31, 37, 14, 43, 21, 18,  6, 47,  5,  3, 24, 15, 21, 50, 35, 28,
  21, 36, 13, 30, 10, 26],
 [ 8, 22, 26, 22, 31, 29,  4,  7,  3, 26,  7,  8,  6, 26, 24, 48, 36, 32,
  13, 48, 16, 14,  3, 42],
 [21, 32, 45, 44, 45,  9,  3, 48, 32,  8, 32,  1, 39, 29, 36, 14,  3, 12,
  34,  3, 30,  3, 25, 26],
 [10, 34, 33, 50, 25, 49, 16, 29, 25, 31, 37, 29, 31, 20,  5,  5, 34, 30,
  14, 28, 48, 25, 44, 18],
 [48,  1, 19, 21, 35,  2, 47,  2,  8, 49, 13, 12, 18, 26,  4,  7, 26,  7,
   1,  7, 33, 44, 27, 22],
 [43, 10,  3, 38, 20, 25, 31, 41,  6, 38,  4, 29, 31, 15, 35, 49, 20, 10,
  26, 47, 24, 49, 36, 39],
 [23, 43, 34, 11, 10, 26, 50, 26, 30, 43, 37, 31, 24, 40, 48,  5,  6,  3,
  32, 41, 39,  9, 38, 16],
 [25,  7, 35, 42, 36, 27, 30, 38, 14, 45, 14,  6, 41, 32, 28, 33, 32, 31,
  36, 44, 37, 18, 48, 46],
 [34, 35, 36,  2, 16, 46, 19, 18, 48, 14, 10, 27,  3, 39, 17, 46, 49,  6,
  13, 10,  6, 31, 45, 35],
 [48, 42, 41,  4, 33,  3, 44,  4, 12, 32, 30, 37, 23, 19, 15, 36,  1, 31,
  45, 10, 50, 46, 15,  2],
 [ 4, 43,  7, 19,  3, 31, 10, 49, 33,  5, 50, 28, 37, 10, 39, 17, 47, 25,
  47, 45, 46, 35, 27, 44],
 [43, 44, 24, 18, 46,  5, 14, 45, 49, 39, 33, 24, 10, 34, 34, 37, 14, 25,
  39,  0, 11, 35, 14, 44],
 [11, 46, 23,  2, 36, 29,  2,  0, 42, 31, 20, 41, 37, 50,  3, 17, 14, 16,
  37, 50, 23, 47, 23, 43],
 [ 3, 17, 42, 25, 46,  3, 21, 13,  7, 19, 30, 13, 12, 50, 23,  4, 23,  4,
  32, 13, 42, 37, 24, 39],
 [ 1, 13,  4, 17, 44, 10,  1, 42, 34, 30, 47, 25, 21, 15, 45, 36, 32, 42,
  10, 39, 32, 10, 35, 19],
 [48, 24,  8, 46, 35, 22, 44,  9, 23, 43,  3,  1,  2, 42, 37,  1, 49, 12,
  34, 41, 22, 20, 17, 43],
 [ 8, 27, 35,  4, 50, 21, 23, 34, 26, 18, 32, 19, 17,  3, 38, 39, 47, 29,
  26, 45,  6, 50,  2,  3],
 [42, 23,  4, 44, 12, 36, 35, 38, 44, 43, 50, 13, 33,  2, 31, 26, 36, 11,
  46,  5, 39, 34, 43, 24],
 [38, 36, 49,  1, 46, 32, 18, 12, 14, 17, 45,  5,  2, 28, 18,  7, 14, 32,
   6, 39, 35, 15, 32,  9],
 [32, 44, 38, 21, 11, 14, 14, 11,  7, 35,  2, 17,  7,  5, 16,  5, 23,  6,
  25, 21, 29, 17, 30, 42],
 [14, 25, 11, 20, 47, 18, 11, 43, 12, 43, 47, 11, 41, 15, 39, 39, 23, 36,
  13, 47, 32, 14, 47, 13],
 [49, 12,  7,  6, 32,  6,  0, 25, 17,  5, 32, 20,  1, 28, 42, 48, 29, 22,
   5, 49,  9, 34,  9, 18],
 [ 5, 27,  9,  7, 34, 28, 18, 42,  6, 49, 45, 37,  2, 41, 24, 40, 27, 28,
  20, 12, 19, 14, 23, 22],
 [37, 35,  0, 35, 35, 16, 35,  1,  1, 36,  5, 31, 43, 31, 36, 24, 39, 45,
  44, 38, 25, 45, 20, 42],
 [43, 32, 45, 39, 31, 14, 11, 23, 30, 32, 44, 40, 15,  0, 13, 31, 47, 11,
  10, 25, 20, 49, 21, 22]])

print(temp)

high_tempt = temp[temp>35]
print(high_tempt)
'''


'''
3. Brain Scan: Crop Center Patch from MRI Slice
You have a 2D NumPy array representing a grayscale MRI image (256×256). Extract a 64×64 patch from the center.
'''
'''
mri = np.round(np.random.uniform(0,256,(256,256)))
print(mri)

pat = mri[96:160, 96:160]

print(pat)
'''
#or
'''
arr = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])

print(arr[1:3,1:3]) # prothom er 1:3 hocche main array gulo theke extracct korbe r 2nd 1:3 hocche individual extract korbe je array gulo first 1:3 er moddhe porbe.

'''
'''
4. Customer Data: Filter Customers in Age Range
You have a 2D array where column 0 = Age, column 1 = Income. Get all rows where age is between 25 and 40.
'''
'''
user_data = np.round(np.random.randint([18, 30000], [70, 120000], size=(1000, 2)))
print(user_data)

extract_row = user_data[(user_data[:,0] >= 25) & (user_data[:, 0] <= 40)]

print(extract_row)
'''

'''
data = np.random.rand(7, 96)  # shape: (days, 15-min intervals)

# 6 PM = 18*4 = 72, 10 PM = 22*4 = 88
evening_peak = data[:, 72:88]
print(evening_peak)
'''

'''
Problem 1: Filtering Outliers in Sales Data
You have a NumPy array sales_data containing daily sales (some values are outliers).
Task:

Replace all sales values above 3 standard deviations from the mean with the median value.

Use boolean indexing to filter and replace.
'''
'''
arr = np.array([1200, 1500, 900, 3000, 1800, 50000, 2000, 1600])

mean_val = np.mean(arr)
median_val = np.median(arr)
std_val = np.std(arr)

arr[arr > mean_val + 3*std_val] = median_val
print(arr)
'''

'''
Problem 2: Extracting Quarterly Revenue
You have a 2D array revenue where each row represents a month, and columns represent regions.
Task:

Slice the array to get Q1 (Jan-Mar) revenue for Region 2 (2nd column).
'''
'''
rev = np.array(
    [
    [120, 150, 200],  # Jan
    [130, 160, 210],  # Feb
    [140, 170, 220],  # Mar
    [150, 180, 230],  # Apr
]
)

print(rev[:3, 1])
#or
print(rev[:3, 1:2])
'''
'''
Problem 3: Masking Negative Values in Temperature Data
You have a temperature dataset with some erroneous negative values.
Task:

Use boolean indexing to replace all negative values with np.nan.
'''
'''
temp = np.array([25.5, -999, 22.1, 23.4, -999, 24.0])

temp[temp < 0] = np.nan
print(temp)
'''

'''
Problem 4: Extracting Weekday Data from Time Series
You have an array daily_sales where weekends (Sat & Sun) have -1 as a placeholder.
Task:

Extract only weekday sales (exclude -1).
'''
'''
sl_rev = np.array([100, 120, -1, -1, 110, 105, 90])

weekday_data = sl_rev[sl_rev != -1]
print(weekday_data)
'''

'''
Problem 5: Slicing Time-Based Data
You have a 2D array sensor_data where the 1st column is timestamp and the 2nd is value.
Task:

Extract all rows where timestamp is between 100 and 200.
'''
'''
sensor_data = np.array([
    [50, 12.5],
    [100, 15.0],
    [150, 17.5],
    [200, 20.0],
    [250, 22.5]
])

extract_data = sensor_data[(sensor_data[:,0] >= 100) & (sensor_data[:,0] <= 200)]

print(extract_data)

'''
'''
Problem 6: Flipping a Correlation Matrix
You have a correlation matrix corr_matrix, but the rows/columns are misaligned.
Task:

Reverse the order of rows only (last row becomes first).
'''
corr_matrix = np.array([
    [1.0, 0.5, 0.3],
    [0.5, 1.0, 0.7],
    [0.3, 0.7, 1.0]
])

# Your solution here (reverse rows)
flipped_corr = corr_matrix[::-1, :]
print(flipped_corr)