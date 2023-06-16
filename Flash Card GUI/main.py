import ctypes
from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

ctypes.windll.shcore.SetProcessDpiAwareness(1)

# UI

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR,
              highlightthickness=0)


card_fg = PhotoImage(file="Flash Card GUI\images\card_front.png")
right = PhotoImage(file="Flash Card GUI\images\wright.png")
wrong = PhotoImage(file="Flash Card GUI\images\wrong.png")

canvas = Canvas(width=800, height=526)
canvas.create_image(400, 263, image=card_fg)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_button = Button(image=right, highlightthickness=0)
right_button.grid(row=1, column=1)

left_button = Button(image=wrong, highlightthickness=0)
left_button.grid(row=1, column=0)


window.mainloop()
