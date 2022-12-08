def priority(item):
    if (ord(item) < 91):
        return (ord(item) - 38) # Unicode offset to make A-Z 27-52
    else:
        return (ord(item) - 96) # Unicode offset to make a-z 1-26

with open('input.txt') as F:
    LINES = F.readlines()

for LINE in LINES:
    LEFT = LINE[0: int(len(LINE) / 2)]
    RIGHT = LINE[int(len(LINE) / 2): int(len(LINE))]
    print(LEFT, RIGHT)