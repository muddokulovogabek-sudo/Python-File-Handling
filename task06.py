with open("Input/numbers.txt") as f:
    numbers = [int(x.strip()) for x in f if x.strip()]

for n in numbers:
    if n % 2 != 0:
        print(n)