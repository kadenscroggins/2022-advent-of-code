with open('input.txt') as f:
    lines = f.readlines()

score = 0

for line in lines:
    if (line[2] == 'X'): # Rock
        score += 1
        if (line[0] == 'A'): # Rock, draw
            score += 3
        elif (line[0] == 'B'): # Paper, loss
            score += 0
        elif (line[0] == 'C'): # Scissors, win
            score += 6
    elif (line[2] == 'Y'): # Paper
        score += 2
        if (line[0] == 'A'): # Rock, win
            score += 6
        elif (line[0] == 'B'): # Paper, draw
            score += 3
        elif (line[0] == 'C'): # Scissors, loss
            score += 0
    elif (line[2] == 'Z'): # Scissors
        score += 3
        if (line[0] == 'A'): # Rock, loss
            score += 0
        elif (line[0] == 'B'): # Paper, win
            score += 6
        elif (line[0] == 'C'): # Scissors, draw
            score += 3

print('Score:', score)