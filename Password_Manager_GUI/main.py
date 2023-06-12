from tkinter import *
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

logo = PhotoImage(file="Password_Manager_GUI\\logo.png")
canvas = Canvas(window, width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=2, column=2)

website = Label(text="Website:", )


window.mainloop()
