import random
from tkinter import *

def generate_secret_number():
    digits = list(range(10))
    random.shuffle(digits)
    secret_number = digits[:4]
    return ''.join(map(str, secret_number))

def check_guess(event=None):
    global secret_number
    guess = entry.get()
    if len(guess) != 4 or not guess.isdigit():
        results.insert(END, "Моля, въведете валидно четирицифрено число.\n")
        return

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

    result_text = ""
    if exact_matches > 0:
        result_text += f"{guess} - Ти имаш {exact_matches} бика.\n"
    if partial_matches > 0:
        result_text += f"{guess} - Ти имаш {partial_matches} крави.\n"
    if guess == secret_number:
        result_text += "Поздравления! Познахте числото.\n"
        secret_number = generate_secret_number()
        result_text += "Новото число е генерирано.\n"

    results.insert(END, result_text + "\n")
    entry.delete(0, END)

root = Tk()
root.title("Игра с числа")

secret_number = generate_secret_number()

entry = Entry(root, font=('sans', 20))
entry.pack(pady=20)
entry.bind("<Return>", check_guess)  # Свързване на клавиша Enter с функцията check_guess

check_button = Button(root, text="Провери", command=check_guess, font=('sans', 20))
check_button.pack(pady=10)

results = Text(root, font=('sans', 20), background='black', foreground='green', height=10, width=50)
results.pack(pady=20)

root.mainloop()
