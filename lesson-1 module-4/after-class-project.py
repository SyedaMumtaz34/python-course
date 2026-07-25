# Empty list
empty_list = []
print(empty_list)

# Student marks
marks = [85, 72, 90, 66, 78]
print("Student Marks:", marks)

# Repeat list
sample_marks = [10, 20, 30] * 2
print("Repeated List:", sample_marks)

# Length
print("Number of marks:", len(marks))

# Indexing
print("First Mark:", marks[0])
print("Last Mark:", marks[-1])

# Slicing
print("First Three Marks:", marks[0:3])
print("Reversed Marks:", marks[::-1])

# Check marks with same first and last digit
count = 0
same_marks = []

for mark in [88, 72, 99, 65, 77]:
    text = str(mark)
    if text[0] == text[-1]:
        same_marks.append(mark)
        count += 1

print("Matching Marks:", same_marks)
print("Total Matching:", count)

# Total and Average
total = 0
for mark in marks:
    total = total + mark

average = total / len(marks)

print("Total Marks:", total)
print("Average Marks:", average)

# Smallest and Largest
marks.sort()

print("Smallest Mark:", marks[0])
print("Largest Mark:", marks[-1])

# Final Summary
print("\n----- Student Marks Summary -----")
print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Lowest:", marks[0])
print("Highest:", marks[-1])