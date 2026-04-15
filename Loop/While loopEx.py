# block of statements repeatedly
# infinate number of times
no_of_students = int(input("Enter the number of students: "))
i = 1
student_names = {}
while i <= no_of_students:
    name = input("Enter the name of students: ")
    print("The name of student {} is {}".format(i, name))
    i +=1
    student_names[1] = name
print(student_names)

while True:
    print("This is an infinate loop, Press Ctrl + C to stop it.")





