#Rock, Paper, Scissors Game
import random 
instr = "Predict a value 'must be integer' between 1 and 3. If what you predict is what system predict, then you win!"
print("Instruction: " + instr)
#Rules
rule = "If you are new to this type of simple game, here is the rule: \n" + "Rock vs paper->Rock wins \n" + "Paper vs Scissor->Paper wins \n" + "Rock vs scissor->Scissor wins \n"
print(rule)
print("Below is the choice arrangement: \n" + "1. Paper; \n" + "2. Rock; \n" + "3. Scissor. \n")
#Let's start the game
choice = int(input("Your Turn: "))
#Validate the user's choice 
while choice > 3 or choice < 1:
    choice = int(input("Enter a valid integer!"))
    