import random

# Генериране на случайно четирицифрено число без повтарящи се цифри
digits = list(range(10))
random.shuffle(digits)
secret_number = digits[:4]
secret_number = ''.join(map(str, secret_number))

#print("Генерирано число (за тестване):", secret_number)  # Можете да премахнете този ред в реална игра
guess = ""
while guess != "ko":
    guess = input("Въведете четирицифрено число: ")

    if len(guess) != 4 or not guess.isdigit():
        print("Моля, въведете валидно четирицифрено число.")
        continue

    exact_matches = 0
    partial_matches = 0
    checked_indices = set()

    for i in range(4):
        if guess[i] == secret_number[i]:
            exact_matches += 1
            checked_indices.add(i)
        elif guess[i] in secret_number and guess[i] != secret_number[i]:
            for j in range(4):
                if guess[i] == secret_number[j] and j not in checked_indices:
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
