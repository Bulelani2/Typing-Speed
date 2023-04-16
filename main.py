from tkinter import *
import math
from paragraphs import para
import random

# ---------------------------- CONSTANTS ------------------------------- #

FONT_NAME = "Courier"
WORK_MIN = 1
reps = 0
timer = ""


def sent(words):
    txt.insert(END, words)


def rerun():
    global reps
    reps = 0
    sentences2 = random.choice(para)
    total_word = int(len(sentences2))
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    # title_label.config(text=f"Score:{retrieve_input(sent=sentences2, word=total_word)}", font=(FONT_NAME, 20))
    inputtxt.delete("1.0", END)
    txt.delete("1.0", END)
    sent(sentences2)


def retrieve_input(sent, word):
    inputv = inputtxt.get("1.0", "end-1c")
    user = len(inputv)
    if inputv in sent:
        total = round(user / word * 100)
        return f"{total}%"
    elif user == 0:
        return "No Text"
    else:
        return "Misspelled words"


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    sent(sentences)
    count_down(work_sec)
    title_label.config(text="Timer", font=(FONT_NAME, 50))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min == 0:
        if count_sec == "00":
            title_label.config(text=f"Score:{retrieve_input(sent=sentences, word=total_words)}", font=(FONT_NAME, 20))

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Typing Speed")
window.config(padx=100, pady=50, bg="light blue")
sentences = random.choice(para)

total_words = int(len(sentences))

title_label = Label(text="Timer", fg="black", bg="light blue", font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=100, height=30, bg="light blue", highlightthickness=0)
timer_text = canvas.create_text(50, 15, text="00:00", fill="black", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

txt = Text(window, height=5, width=30, bg="light green")
txt.grid(column=1, row=2, sticky=EW)
scrollbar = Scrollbar(window, orient='vertical', command=txt.yview)
scrollbar.grid(row=2, column=2, sticky=NS)

txt['yscrollcommand'] = scrollbar.set

inputtxt = Text(window, height=5, width=30, bg="light grey")
inputtxt.grid(column=1, row=3, columnspan=1, sticky=EW)
scrollbar2 = Scrollbar(window, orient='vertical', command=inputtxt.yview)
scrollbar2.grid(row=3, column=2, sticky=NS)
inputtxt['yscrollcommand'] = scrollbar.set

start_button = Button(height=2, width=6, bg="green", text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=4)

button = Button(height=2, width=6, text="Rerun", bg="red", command=rerun)
button.grid(column=2, row=4)

window.mainloop()
