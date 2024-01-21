# guess the correct number between 1-100

import random

low = 1
high = 100
guesses = 0
number = random.randint(low, high)

print("----Guess the Correct Number----")
print()
while True:
    guess = int(input(f"Enter a number between {low} - {high}: "))

    if low <= guess <= high:
        guesses += 1
        if guess < number:
            print(f"{guess} is too low.")
        elif guess > number:
            print(f"Guess is too high.")
        else:
            print(f"{guess} is correct!")
            break
    else:
        print("Please enter a number within the valid range.")

print(f"This round took you {guesses} guesses.")
