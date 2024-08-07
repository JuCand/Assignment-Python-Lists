# Task 1: Sort the grades in descending order and print the sorted list.
# Task 2: Calculate the average grade and print it 

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print(grades)

grade_average = float(sum(grades) / len(grades))
print(grade_average)
