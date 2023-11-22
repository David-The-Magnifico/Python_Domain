import random

coin = random.randint(0, 1)

guess = int(input("Guess the coin flip! Enter 0 for heads or 1 for tails: "))

if guess == coin:
    print("Congratulations! Your guess is correct.")
else:
    print("Sorry, your guess is incorrect. Try again next time.")
