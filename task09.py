with open("Input/numbers.txt") as f:
    numbers = [int(x.strip()) for x in f if x.strip()]

for n in numbers:
    print(n, "->", len(str(abs(n))), "xonali")