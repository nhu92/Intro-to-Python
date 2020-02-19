# Rock-Paper-Scissors Game
# Feb. 19, 2020
# Nan Hu

from random import randint

Choice_set = ["Rock", "Scissors","Paper"]
# Input player play
player_play = input("Your choice: 1 - Rock; 2 - Scissors; 3 - Paper.\n")
# Random generate computer play
com_play = str(randint(1,3))
print("Player's Choice is: " + Choice_set[int(player_play)-1])
print("Computer's Choice is: " + Choice_set[int(com_play)-1])

# Judgement based on the combination of player and computer's choice
judge = player_play + com_play

# If block for determining the result
if judge == "11" or judge == "22" or judge == "33":
	print("TIE!")
elif judge == "21" or judge == "32" or judge == "13":
	print("You Lose!")
else:
	print("You Win!")

