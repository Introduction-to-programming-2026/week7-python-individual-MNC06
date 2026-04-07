# Project 2 — Number Guessing Game
# Author: your name here

import random

print("Choose difficulty: (1) Easy 1-10  (2) Medium 1-50  (3) Hard 1-100")
choice = input("Choice: ")

if choice == "1":
    max_number = 10
elif choice == "2":
    max_number = 50
elif choice == "3":
    max_number = 100
else:
    max_number = 10

secret = random.randint(1, max_number)

guesses = 0
guess = int(input(f"Guess a number between 1 and {max_number}: "))

while guess != secret:
    guesses += 1

    if guess < secret:
        guess = int(input("Too low! Try again: "))
    else:
        guess = int(input("Too high! Try again: "))

guesses += 1

print(f"Correct! You got it in {guesses} guesses.")
