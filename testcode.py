from tkinter import *
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="I am a Label")
my_label.pack()


def button_clicked():

    new_text = input.get()

    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.pack()

input = Entry()
input.pack()
print(input.get())

window.mainloop()
