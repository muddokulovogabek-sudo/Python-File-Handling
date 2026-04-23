with open("Input/numbers.txt") as f:
    numbers = [int(x.strip()) for x in f if x.strip()]

print(sum(numbers))