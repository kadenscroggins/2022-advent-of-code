with open('input.txt') as f:
    lines = f.readlines()

biggest = 0
calories = 0

for line in lines:
    if (line == "\n"):
        if calories > biggest:
            biggest = calories
        calories = 0
    else:
        calories += int(line)

print(biggest)