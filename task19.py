import csv

with open("Input/grades.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0], ":", row[1])