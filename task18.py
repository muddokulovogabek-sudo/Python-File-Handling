with open("Input/students.txt") as f:
    students = [x.strip() for x in f if x.strip()]

name = input("Ism kiriting: ")

if name in students:
    print("FOUND")
else:
    print("NOT FOUND")