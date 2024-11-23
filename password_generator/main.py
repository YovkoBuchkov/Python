from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
from string import ascii_letters, digits, punctuation
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
symbols = "#$%&()/*<=>?@[\]^_{|}~"

def generate_password():
    pass_letter = [choice(ascii_letters) for _ in range(randint(8, 10))]
    pass_num = [choice(digits) for _ in range(randint(2, 4))]
    pass_symbol = [choice(symbols) for _ in range(randint(2, 4))]

    new_password = pass_letter + pass_num + pass_symbol

    shuffle(new_password)
    password = "".join(new_password)
    gen_password.delete(0, 'end')
    gen_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = input_website.get()
    email = input_email.get()
    password = gen_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="All fields must be filled out.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Email: {email},\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                data_file.close()
                gen_password.delete(0, END)
                input_website.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password = Label(text="Password: ")
password.grid(row=3, column=0)

input_website = Entry(width=52)
input_website.grid(row=1, column=1, columnspan=2)

input_email = Entry(width=52)
input_email.grid(row=2, column=1, columnspan=2)
input_email.insert(0, "input_your_email@mail.com")


gen_password = Entry(width=33)
gen_password.grid(row=3, column=1)


gen_button = Button(text="Generate Password", command=generate_password)
gen_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()