# #C:\Users\YovoB\AppData\Local\Programs\Python\Python39-32\Scripts\pyinstaller.exe  --onefile cow_bull_window.py
# import random
#
# digits = list(range(10))
# random.shuffle(digits)
# secret_number = digits[:4]
# secret_number = ''.join(map(str, secret_number))
# print(secret_number)
#
# while True:
#     check_number = input()
#     if check_number == secret_number:
#         print(f"You guessed my number")
#         break
#     bull = 0
#     cow = 0
#     for digit in secret_number:
#         for i in check_number:
#             if digit == i:
#                 bull += 1
#     print(f"You guess {cow} Cows and {bull} Bull!")
#
# else:
#     print(f"You guess my number")

import random

# Генериране на случайно четирицифрено число без повтарящи се цифри
digits = list(range(10))
random.shuffle(digits)
secret_number = digits[:4]
secret_number = ''.join(map(str, secret_number))

print("Генерирано число (за тестване):", secret_number)  # Можете да премахнете този ред в реална игра
guess = ""
while guess != "ko":
    guess = input("Въведете четирицифрено число: ")

    if len(guess) != 4 or not guess.isdigit():
        print("Моля, въведете валидно четирицифрено число.")
        continue

    exact_matches = 0
    partial_matches = 0
    checked_indices = set()

    for i, g_digit in enumerate(guess):
        if g_digit == secret_number[i]:
            exact_matches += 1
            checked_indices.add(i)
        elif g_digit in secret_number and g_digit != secret_number[i]:
            for j, s_digit in enumerate(secret_number):
                if g_digit == s_digit and j not in checked_indices:
                    partial_matches += 1
                    checked_indices.add(j)
                    break

    if exact_matches > 0:
        print(f"Ти имаш {exact_matches} бика.")
    if partial_matches > 0:
        print(f"Ти имаш {partial_matches} крави.")

    if guess == secret_number:
        print("Поздравления! Познахте числото.")
        break

else:
    print(secret_number)


