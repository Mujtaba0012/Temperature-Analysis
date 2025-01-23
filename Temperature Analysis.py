import numpy as np

temperatures = np.array([

   [30, 32, 34, 28, 33, 31, 30, 29, 24, 35, 31, 30], # New York
   [25, 27, 26, 21, 23, 24, 28, 26, 30, 31, 27, 25], # Paris
   [35, 37, 29, 34, 33, 31, 32, 37, 28, 26, 30, 31] # Berlin

   ])

first_three_days = temperatures[:, :3]
print("\nAverage temputure for first three days:", first_three_days)

average_temp = np.mean(temperatures, axis=1)
print("\nAverage temperature for each city:", average_temp)

hottest_temp = np.max(temperatures)
coldest_temp = np.min(temperatures)

print("\nHottest temperature:", hottest_temp)
print("\nColdest temperature:", coldest_temp)
