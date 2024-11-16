from art import logo
import random


def game_on(num, random_num):
    attempts = num
    while True:
        guess = int(input('Make a guess:  '))
        if attempts == 0:
            print("You've run out of guesses. Refresh the page to run again.")
            break
        if guess < random_num:
            attempts -= 1
            print('Too low.')
            print(f"Guess again.\nYou have {attempts} attempts remaining to guess the number.")
            continue
        elif guess > random_num:
            attempts -= 1
            print('Too high.')
            print(f"Guess again.\nYou have {attempts} attempts remaining to guess the number.")
            continue
        else:
            print(f"You got it! The answer was {random_num}.")
            break


def get_random_():
    random_num = random.randrange(1, 101)
    line = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if line.lower() == "easy":
        print("You have 10 attempts remaining to guess the number.")
        game_on(10, random_num)
    elif line.lower() == "hard":
        print("You have 5 attempts remaining to guess the number.")
        game_on(5, random_num)
    else:
        print("Invalid input. Please choose 'easy' or 'hard'.")
        get_random_()


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
get_random_()