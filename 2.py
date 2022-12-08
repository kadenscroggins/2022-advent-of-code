with open('input.txt') as f:
    lines = f.readlines()

ROCK = 1
PAPER = 2
SCISSORS = 3

LOSE = 0
DRAW = 3
WIN = 6

'''
Part 1
'''
score = 0

for line in lines:
    if (line[2] == 'X'): # Rock
        score += ROCK
        if (line[0] == 'A'): # Rock, draw
            score += DRAW
        elif (line[0] == 'B'): # Paper, loss
            score += LOSE
        elif (line[0] == 'C'): # Scissors, win
            score += WIN
    elif (line[2] == 'Y'): # Paper
        score += PAPER
        if (line[0] == 'A'): # Rock, win
            score += WIN
        elif (line[0] == 'B'): # Paper, draw
            score += DRAW
        elif (line[0] == 'C'): # Scissors, loss
            score += LOSE
    elif (line[2] == 'Z'): # Scissors
        score += SCISSORS
        if (line[0] == 'A'): # Rock, loss
            score += LOSE
        elif (line[0] == 'B'): # Paper, win
            score += WIN
        elif (line[0] == 'C'): # Scissors, draw
            score += DRAW

print('Part 1 score:', score)

'''
Part 2
'''
score = 0

for line in lines:
    if (line[0] == 'A'): # Rock
        if (line[2] == 'X'): # Lose, Scissors
            score += LOSE + SCISSORS
        elif (line[2] == 'Y'): # Draw, Rock
            score += DRAW + ROCK
        elif (line[2] == 'Z'): # Win, Paper
            score += WIN + PAPER
    elif (line[0] == 'B'): # Paper
        if (line[2] == 'X'): # Lose, Rock
            score += LOSE + ROCK
        elif (line[2] == 'Y'): # Draw, Paper
            score += DRAW + PAPER
        elif (line[2] == 'Z'): # Win, Scissors
            score += WIN + SCISSORS
    elif (line[0] == 'C'): # Scissors
        if (line[2] == 'X'): # Lose, Paper
            score += LOSE + PAPER
        elif (line[2] == 'Y'): # Draw, Scissors
            score += DRAW + SCISSORS
        elif (line[2] == 'Z'): # Win, Rock
            score += WIN + ROCK

print('Part 2 score:', score)