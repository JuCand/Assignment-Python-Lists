# Task 1: Given the list of temperatures, Extract the temperatures for the second week (7 days) of the month (index 7 to index 14).

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week_temps = temperatures[7:14]
print(second_week_temps)

# Task 2 Extract all the temperatures above 100. HINT: add the temperatures over 100 to a new list, or use list slicing to get the temperatures.

high_temperatures = [ int for int in temperatures if int >= 100]
print(high_temperatures)