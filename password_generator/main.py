from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
from string import ascii_letters, digits, punctuation
import pyperclip
import json

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
    website = input_website.get().title()
    email = input_email.get()
    password = gen_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            input_website.delete(0, END)
            gen_password.delete(0, END)

# -------------------------- FIND PASSWORD ---------------------------- #

def search_password():
    website = input_website.get().title()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            pyperclip.copy(password)
            input_website.delete(0, END)
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


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

input_website = Entry(width=33)
input_website.grid(row=1, column=1)

input_email = Entry(width=52)
input_email.grid(row=2, column=1, columnspan=2)
input_email.insert(0, "input_your_email@mail.com")


gen_password = Entry(width=33)
gen_password.grid(row=3, column=1)

search_password_button = Button(text="Search", width=14, command=search_password)
search_password_button.grid(row=1, column=2)

gen_button = Button(text="Generate Password", command=generate_password)
gen_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()