import random


def guess_number(target):
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == target:
        print(f"Congratulations! You guessed the number {target}.")
    elif guess < target:
        print(f"{guess} is smaller than the target number. Try again.")
        guess_number(target)
    else:
        print(f"{guess} is bigger than the target number. Try again.")
        guess_number(target)


if __name__ == "__main__":
    computer_number = random.randint(1, 100)
    guess_number(computer_number)


