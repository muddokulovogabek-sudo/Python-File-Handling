with open("Input/students.txt") as f:
    students = [x.strip() for x in f if x.strip()]

for s in students:
    print(s, "->", len(s))