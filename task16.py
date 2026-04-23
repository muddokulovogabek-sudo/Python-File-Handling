with open("Input/students.txt") as f:
    students = [x.strip() for x in f if x.strip()]

for s in students:
    if len(s) > 5:
        print(s)