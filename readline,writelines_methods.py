                 # READLINE METHOD ------------

# f=open('readline.txt','r')
# line1=f.readline()
# line2=f.readline()
# line3=f.readline()

# print(line1)
# print(line2)
# print(line3)

# f.close()


                 # WRITELINE METHOD .............

# file = open('student.txt', 'w')

# students = ["umer\n", "ali\n", "zohaib\n"]

# file.writelines(students)

# file.close


                  # READLINE + WHILE LOOP -----------

# file = open("readline.txt", 'r')

# while True:
#     line = file.readline()

#     if line == "":
#         break

#     print(line.strip())

# file.close()


                   # WRITELINES = FORLOOP ..............

# file = open("data.txt", "w")

# students = ['Umer', 'Ali', 'Bilal', 'Ahmad', 'Rohail']

# lines = []

# for student in students:
#     lines.append(student + "\n")

# file.writelines(lines)

# file.close()


                    # STUDENTS MARKS SHHET PROGRAM ______________

file = open("student_result.txt", "r")

while True:
    line = file.readline()

    if line == "":
        break

    data = line.strip().split(",")

    student = data[0]
    subject = data[1]
    marks = data[2]

    print("Student:", student)
    print("Subject:", subject)
    print("Marks:", marks)
    print("-------------------")

file.close()