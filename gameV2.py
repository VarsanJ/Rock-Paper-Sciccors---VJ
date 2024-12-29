# Module Importation
import random

# Sets Up Counters For Each Scenario
RockWin, RockLoss, RockTie = (0,)*3
PaperWin, PaperLoss, PaperTie = (0,)*3
ScissorWin, ScissorLoss, ScissorTie = (0,)*3

# Determines the Number of Games to Run
while True:
    try:
        instances = int(input("How many games do you want to run?"))
        break
    except Exception:
        print("Please enter a valid number of inputs")

# Collects the User's Moves
for i in range(0, instances):
    try:
        move = int(input(f"""
Please state your move for Game {i}
1 --> Rock
2 --> Paper
3 --> Scissors
Any other input will be considered as a random input
"""))
        if (move != 1) and (move != 2) and (move != 3):
            move = random.randint(1, 3)
    except Exception:
        move = random.randint(1, 3)

# Runs The Moves
    response = random.randint(-1, 1)
    action = move + response
    if action > move:
        print(f"You have won game {i}")
        if move == 1:
            RockWin += 1
        elif move == 2:
            PaperWin += 1
        else:
            ScissorWin += 1
    elif action == move:
        print(f"You have tied game {i}")
        if move == 1:
            RockTie += 1
        elif move == 2:
            PaperTie += 1
        else:
            ScissorTie += 1
    else:
        print(f"You have lost game {i}")
        if move == 1:
            RockLoss += 1
        elif move == 2:
            PaperLoss += 1
        else:
            ScissorLoss += 1

# Final Stats
print("FINAL OUTCOMES BASED ON YOUR MOVES:")
print(f"Rock: {RockWin} wins, {RockTie} ties, {RockLoss} loss")
print(f"Paper: {PaperWin} wins, {PaperTie} ties, {PaperLoss} loss")
print(f"Scissors: {ScissorWin} wins, {ScissorTie} ties, {ScissorLoss} loss")
