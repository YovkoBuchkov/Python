import random
from tkinter import *
from tkinter import simpledialog, messagebox

def generate_secret_number():
    digits = list(range(10))
    random.shuffle(digits)
    secret_number = digits[:4]
    return ''.join(map(str, secret_number))

def play_game():
    secret_number = generate_secret_number()
    # print("Генерирано число (за тестване):", secret_number)  # Можете да премахнете този ред в реална игра
    guess = ""
    while guess != "ko":
        guess = simpledialog.askstring("Въведете четирицифрено число", "Въведете четирицифрено число:")

        if guess is None:  # Ако потребителят затвори диалога
            return

        if len(guess) != 4 or not guess.isdigit():
            messagebox.showerror("Грешка", "Моля, въведете валидно четирицифрено число.")
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
            messagebox.showinfo("Резултат", f"Ти имаш {exact_matches} бика.")
        if partial_matches > 0:
            messagebox.showinfo("Резултат", f"Ти имаш {partial_matches} крави.")

        if guess == secret_number:
            messagebox.showinfo("Поздравления", "Познахте числото.")
            break

    messagebox.showinfo("Тайното число", f"Тайното число беше: {secret_number}")

root = Tk()
root.withdraw()  # Скриване на главния прозорец
play_game()
root.mainloop()
