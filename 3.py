def priority(item):
    if (ord(item) < 91):
        return (ord(item) - 38) # Unicode offset to make A-Z 27-52
    else:
        return (ord(item) - 96) # Unicode offset to make a-z 1-26

with open('input.txt') as F:
    LINES = F.readlines()

'''
Part 1
'''

letters = []

for LINE in LINES:
    LEFT = LINE[0: int(len(LINE) / 2)]
    RIGHT = LINE[int(len(LINE) / 2): int(len(LINE))]
    for LETTER in LEFT:
        if LETTER in RIGHT:
            letters.append(LETTER)
            break

priority_sum = 0

for LETTER in letters:
    # print("Letter:", LETTER, priority(LETTER))
    priority_sum += priority(LETTER)

print("Part 1:", priority_sum)

'''
Part 2
'''

priority_sum = 0

for i in range(0, len(LINES), 3):
    for LETTER in LINES[i]:
        if ((LETTER in LINES[i+1]) and (LETTER in LINES[i+2])):
            priority_sum += priority(LETTER)
            break
print("Part 2:", priority_sum)