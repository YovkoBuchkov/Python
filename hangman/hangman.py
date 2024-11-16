import random
from hangman_arts import banner, hanged_man

print(banner)

with open('hangman_dictionary.txt', 'r') as file:
    word = file.read().splitlines()

random_word = random.choice(word)

guessed_letter = []

for _ in range(len(random_word)):
    guessed_letter += "_"

print(*guessed_letter)
lives = 0
game_over = False
while not game_over:
    user_guess_letter = input("Please enter letter: ").lower()
    if user_guess_letter in random_word and user_guess_letter not in guessed_letter:
        for i in range(len(random_word)):
            if random_word[i] == user_guess_letter:
                guessed_letter[i] = user_guess_letter
        print(*guessed_letter)
        if "_" not in guessed_letter:
            print("*************Congratulations! You won!*************")
            game_over = True
    else:
        lives += 1
        print(hanged_man[lives])
        print("*************Wrong guess!*************")
        print(*guessed_letter)
        if lives < 6:
            print(f"************* {6 - lives} lives left *************")
        if lives == 6:
            print(f"*************Game over!*************\nThe word was: {random_word}")
            game_over = True


