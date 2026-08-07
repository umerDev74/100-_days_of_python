# List of student names
students = ["Ali", "Umer", "Ahmed", "Bilal", "Hamza"]

# List of marks of each student
marks = [78, 45, 89, 32, 67]

# Variables to store total marks, passed students and failed students
total_marks = 0
passed = 0
failed = 0

# Print the heading
print("===== Student Result =====")

# Loop through all students
for i in range(len(students)):

    # Get the student name using index
    name = students[i]

    # Get the marks using the same index
    mark = marks[i]

    # Add the student's marks to total marks
    total_marks += mark

    # Check if the student has passed
    if mark >= 50:
        status = "Pass"
        passed += 1
    else:
        # If marks are less than 50, student has failed
        status = "Fail"
        failed += 1

    # Print student's name
    print(f"Name   : {name}")

    # Print student's marks
    print(f"Marks  : {mark}")

    # Print student's result status
    print(f"Status : {status}")

    # Print a separator after each student
    print("--------------------")


# Calculate the average marks
average = total_marks / len(marks)


# Print the summary heading
print("\n===== Summary =====")

# Print total number of students
print(f"Total Students : {len(students)}")

# Print number of passed students
print(f"Passed         : {passed}")

# Print number of failed students
print(f"Failed         : {failed}")

# Print total marks of all students
print(f"Total Marks    : {total_marks}")

# Print average marks
print(f"Average Marks  : {average:.2f}")