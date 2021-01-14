import numpy as np

temperatures = np.genfromtxt('temperature_data.csv', delimiter=',')

print(temperatures)
print("")
temperatures_fixed = temperatures + 3

print(temperatures_fixed)
print("")
monday_temperatures = temperatures_fixed[0,:]
print(monday_temperatures)
print("")

thursday_friday_morning = temperatures_fixed[3:5,1]
print(thursday_friday_morning)
print("")

temperature_extremes = temperatures_fixed[(temperatures_fixed < 50) | (temperatures_fixed > 60)]

print(temperature_extremes)