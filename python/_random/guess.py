import random

print("Welcome to the CMSC 12 Guessing Game!")
print("Guess a number from 1 to 100")

target = random.randint(0,100)

num_of_guesses = 5
guessed_correctly = False

while num_of_guesses > 0:
	print("\nGuesses left:", num_of_guesses)
	guess = int(input("Enter guess: "))

	# give hint
	if guess > target:
		print("Guess lower!")
	elif guess < target:
		print("Guess higher!")
	else:
		guessed_correctly = True
		break

	num_of_guesses -= 1

if guessed_correctly:
	print("Correct! The number is", target) 
else:
	print("Sorry, the number is", target)