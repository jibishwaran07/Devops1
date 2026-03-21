# Predefined marks of students (no user input)
marks = [78, 45, 90, 32, 67, 88, 23, 56, 99, 40]

n = len(marks)

# Calculations
highest = max(marks)
lowest = min(marks)
average = sum(marks) / n

passed = len([x for x in marks if x >= 40])
failed = len([x for x in marks if x < 40])

# Sorting
ascending = sorted(marks)
descending = sorted(marks, reverse=True)

# Output
print("===== Student Marks Analyzer =====")
print("Marks:", marks)
print("Highest mark:", highest)
print("Lowest mark:", lowest)
print("Average mark:", average)
print("Passed:", passed)
print("Failed:", failed)
print("Ascending order:", ascending)
print("Descending order:", descending)
