from pass_letters import letters, numbers, symbols
import random
from tkinter import *
from tkinter import messagebox
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():

    password = []
    for i in range(0, 3):
        i = random.choice(letters)
        password.append(i)

    for i in range(0, 3):
        i = random.choice(symbols)
        password.append(i)

    for i in range(0, 3):
        i = random.choice(numbers)
        password.append(i)

    random.shuffle(password)

    output = "".join(password)
    password_entry.insert(0, output)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():

    if len(user_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(
            title="Oops", message="Please don't leave any boxes empty")

    else:

        is_ok = messagebox.askokcancel(
            title="Password Manager", message=f"Please confirm your choice: \n\nEmail/User: {user_entry.get()}\n\nPassword: {password_entry.get()}")

        if is_ok:

            with open("Password_Manager_GUI\\data.txt", 'a') as file:
                file.write(
                    f"{website_entry.get()} | {user_entry.get()} | {password_entry.get()}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

logo = PhotoImage(file="Password_Manager_GUI\\logo.png")
canvas = Canvas(window, width=200, height=200)
canvas.create_image(80, 100, image=logo)
canvas.grid(row=1, column=2)

website = Label(text="Website: ", font=("Courier", 15, "bold"))
website.grid(row=2, column=1)

user = Label(text="Email/Username: ", font=("Courier", 15, "bold"))
user.grid(row=3, column=1)

password = Label(text="Password: ", font=("Courier", 15, "bold"))
password.grid(row=4, column=1)

website_entry = Entry(font=('courier', 15), width=35)
website_entry.grid(row=2, column=2, columnspan=2)
website_entry.focus()

user_entry = Entry(font=('courier', 15), width=35)
user_entry.grid(row=3, column=2, columnspan=2)
user_entry.insert(0, "test@gmail.com")

password_entry = Entry(font=('courier', 15), width=22)
password_entry.grid(row=4, column=2)

password_button = Button(text="Generate Password",
                         font=("courier", 10, "bold"), command=password_generator)
password_button.grid(row=4, column=3)

add_button = Button(text="Add",
                         font=("courier", 10, "bold"), width=52, command=save_password)
add_button.grid(row=5, column=2, columnspan=2)


window.mainloop()
