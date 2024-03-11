#import random
import random

#welcome instructions
print(f"Welcome user to Rock-Paper-Scissors!. The goal of the game is to beat your opponent's choice!")
print("Rock beats scissors, paper beats rock and scissors beats paper. If the same choice is picked, it is a tie.")
print("WIN +1, LOSE -1, TIE 0")
print("Good luck!")

#user name
strName = input("What is your username/name?  ")
strBotName = input("What is the name of the bot?  ")

#game variables
isLoop = True #set loop
isChoice = True #set choice
intPointUser = 0 #set user points
intPointBot = 0 #set bot points

#game loop
while isLoop:
	strChoice = print(f"""{strName}, what is your choice?
	ROCK - R
	PAPER - P
	Scissors - S
	Exit - any other character""")
	
	strChoice = input("") #user input

	#convert user choices
	if strChoice == "S":
		isChoice = True 
		strUserChoice = "SCISSORS"
	elif strChoice == "R":
		isChoice = True 
		strUserChoice = "ROCK"
	elif strChoice == "P":
		isChoice = True 
		strUserChoice = "PAPER"
	else:
		isLoop = False
		isChoice = False
		strUserChoice = ""
	if isChoice:
		strBotChoice = random.randint(1,3)

		#convert bot choice to string
		if strBotChoice == 1:
			strBotChoice = "ROCK"
		elif strBotChoice == 2:
			strBotChoice = "PAPER"
		elif strBotChoice == 3:
			strBotChoice = "SCISSORS"

		#display output of choices
		print(f"{strName} chose {strUserChoice} and {strBotName} chose {strBotChoice}") 

		#comparing choices using conditional statements
		if strBotChoice == strUserChoice:
			print("The game is a tie.") #tie case
		else:
			#individual cases
			if strUserChoice == "ROCK": #rock
				if strBotChoice == "PAPER":
					print("YOU LOSE")
					intPointUser -= 1
					intPointBot += 1
				else:
					print("YOU WIN")
					intPointUser += 1
					intPointBot -= 1
					
			if strUserChoice == "PAPER": #paper
				if strBotChoice == "SCISSORS":
					print("YOU LOSE")
					intPointUser -= 1
					intPointBot += 1
				else:
					print("YOU WIN")
					intPointUser += 1
					intPointBot -= 1
					
			if strUserChoice == "SCISSORS": #scissors
				if strBotChoice == "ROCK":
					print("YOU LOSE")
					intPointUser -= 1
					intPointBot += 1
				else:
					print("YOU WIN")
					intPointUser += 1
					intPointBot -= 1

#terminate
print(f"{strName}, your point total was {intPointUser} and {strBotName} had {intPointBot} points.")
if intPointUser > intPointBot:
	print(f"{strName} WON!")
elif intPointBot > intPointUser:
	print(f"{strBotName} WON!")
else:
	print("TIE GAME")
print("Thank you for playing!")
