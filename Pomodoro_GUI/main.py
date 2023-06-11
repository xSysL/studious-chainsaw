from tkinter import *
import ctypes
import math

ctypes.windll.shcore.SetProcessDpiAwareness(1)

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_SEC = int(.3*60)
SHORT_BREAK_SEC = int(.1*60)
LONG_BREAK_SEC = int(.2*60)
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text= "Timer")
    checkmark.config(text="")
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    
    global reps
    
    reps += 1
    

    if reps % 8 == 0:
        count_down(LONG_BREAK_SEC)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_SEC)
        label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_SEC)
        label.config(text="Work", fg="green")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔️"
        checkmark.config(text=marks)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)

label = Label(text="Timer", font=(FONT_NAME, 40, "bold"),
              background=YELLOW, fg="green")

checkmark = Label(fg="green", bg=YELLOW)
label.grid(column=2, row=1)
checkmark.grid(row=3, column=2)

start = Button(text="Start", command=start_timer)
reset = Button(text="Reset", command=reset_timer)

start.grid(row=3, column=1)
reset.grid(row=3, column=3)


tomato_img = PhotoImage(file="Pomodoro_GUI\\tomato.png")
canvas = Canvas(window, width=220, height=244, bg=YELLOW)
canvas.create_image(110, 90, image=tomato_img)
timer_text = canvas.create_text(110, 110, text="00:00", fill="white",
                                font=(FONT_NAME, 30, "bold"))

canvas.grid(row=2, column=2)


window.mainloop()
