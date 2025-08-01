import numpy as np
from scipy import stats

data_set = [34,67,90,12,45,76,98,34,23,67,34,34]

cal_mean = np.mean(data_set)
print(cal_mean)

cal_median = np.median(data_set)
print(cal_median)

#we only can calculate mode value to import stats in scipy
cal_mode = stats.mode(data_set)
print(cal_mode)