import random
# Генериране на случайно четирицифрено число без повтарящи се цифри
digits = list(range(10))
random.shuffle(digits)
secret_number = digits[:4]
secret_number = ''.join(map(str, secret_number))

#print("Генерирано число (за тестване):", secret_number)  # Можете да премахнете този ред в реална игра
bull = 0
cow = 0
while True:
    guess = input("Въведете четирицифрено число: ")

    if len(guess) != 4 or not guess.isdigit():
        print("Моля, въведете валидно четирицифрено число.")
        continue

    for i in range(4):
        if guess[i] == secret_number[i]:
            bull += 1
        elif guess[i] in secret_number:
            cow += 1
    print(f"Имаш {bull} бикове, и {cow} Крави")
    if guess == secret_number:
        print("Поздравления! Познахте числото.")
        break