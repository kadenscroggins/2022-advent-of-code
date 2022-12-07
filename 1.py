with open('input.txt') as f:
    lines = f.readlines()

elves = []
calories = 0

for line in lines:
    if (line == "\n"):
        elves.append(calories)
        calories = 0
    else:
        calories += int(line)

elves.sort()
print('Part 1:', elves[-1])
print('Part 2:', elves[-1] + elves[-2] + elves[-3])