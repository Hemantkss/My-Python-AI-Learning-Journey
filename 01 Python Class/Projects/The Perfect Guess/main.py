# Import the random module to use random numbers
import random

# This line picks a random number between 1 and 100
secret_number = random.randint(1, 100)

# This keeps track of how many times the player has guessed
guess_count = 0

# Start a loop that goes on until the correct number is guessed
while True:
    # Ask the player to guess a number
    guess = int(input("Guess a number between 1 and 100: "))
    
    # Increase the number of guesses by 1
    guess_count += 1

    # Check if the guessed number is correct
    if guess == secret_number:
        print("🎉 Great job! You guessed the number in", guess_count, "tries!")
        break  # End the game
    # If the guessed number is too small
    elif guess < secret_number:
        print("Too low! Try a bigger number.")
    # If the guessed number is too big
    else:
        print("Too high! Try a smaller number.")
