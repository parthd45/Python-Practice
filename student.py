# Student Marks Management System

# Student details
name = "Parth"
roll_no = 45

# Subject marks
marks = [85, 78, 92, 67, 88]

# Calculate total marks
total = 0

for mark in marks:
    total = total + mark

# Calculate percentage
percentage = total / len(marks)

# Find highest and lowest marks
highest = max(marks)
lowest = min(marks)

# Display student details
print("===== STUDENT RESULT =====")

print("Student Name:", name)
print("Roll Number:", roll_no)

print("\nSubject Marks:", marks)
print("Total Marks:", total)
print("Percentage:", percentage)

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

# Check result
if percentage >= 75:
    print("Grade: Distinction")
elif percentage >= 60:
    print("Grade: First Class")
elif percentage >= 40:
    print("Grade: Pass")
else:
    print("Grade: Fail")

print("==========================")