with open("Input/numbers.txt") as f:
    numbers = [int(x.strip()) for x in f if x.strip()]

count = 0
for n in numbers:
    if n % 5 == 0:
        print(n)
        count += 1

print("Count:", count)