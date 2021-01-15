import codecademylib
import numpy as np

data = np.genfromtxt('cereal.csv', delimiter=",")

print(data)
print("................................................")
average_calories = np.mean(data)

print(average_calories)
print("................................................")

calorie_stats_sorted = np.sort(data)

print(calorie_stats_sorted)
print("................................................")

median_calories = np.median(data)

print(median_calories)
print("................................................")

nth_percentile = np.percentile(data, 60)

print(nth_percentile)
print("................................................")

more_calories = np.mean(data > 60)

print(more_calories)
print("................................................")

calorie_std = np.std(data)

print(calorie_std)

print("")
