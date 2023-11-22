import random

# Generate a random three-digit number
three_digit_number = random.randint(0, 999)

# Ask the user to guess a three-digit number
guess = int(input("Please enter your three-digit number: "))

# Check if the guess matches the generated number
if guess == three_digit_number:
    print("Congratulations! You won the Lottery.")
else:
    print("Sorry, you lose. Please try again later.")
