# Guess the number
# Feb. 26, 2020
# Nan Hu

####################################
# Basic Steps
####################################
# 1. Generate a number
# 2. Input my guess
# 3. Determine the guess is larger or smaller
# 4. Re-guess

####################################
# Detailed Steps
####################################
# 1. Generate a number
#	- import a module to randomly give a number
# 2. Input my guess
# 3. Determine the guess is larger or smaller
# 4. Re-guess
#	- A loop for continuing guessing until it is right

from random import randint

# Randomly generate a number between 1 to 100 for player to guess
rnd_num = randint(1,100)
player_guess = int(input("Please guess the number between 1 to 100:"))

# Determine the result if it is equal or not
while rnd_num != player_guess:
	if player_guess > rnd_num:
		print("Your guess is larger")
	else:
		print("Your guess is smaller")
	# re-guess the number
	player_guess = int(input("Please guess the number between 1 to 100:"))
print("You hit the number! Congrats!")
