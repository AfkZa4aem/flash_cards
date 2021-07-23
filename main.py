from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
word = {}

# ---------------------------- PANDAS LOGIC ------------------------------- #
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/en_ru.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ---------------------------- LOGIC ------------------------------- #
def next_word():
    global word, timer
    timer = window.after_cancel(timer)
    word = choice(to_learn)
    eng = word["English"]
    canvas.itemconfig(bg_card, image=front_card)
    canvas.itemconfig(lang_text, text="English", fill="black")
    canvas.itemconfig(word_text, text=eng, fill="black")
    timer = window.after(3000, translate)


def known():
    to_learn.remove(word)
    next_word()


def unknown():
    new_dict = pandas.DataFrame(to_learn)
    new_dict.to_csv("./data/words_to_learn.csv", index=False)
    next_word()


def translate():
    rus = word["Russian"]
    canvas.itemconfig(bg_card, image=back_card)
    canvas.itemconfig(lang_text, text="Russian", fill="white")
    canvas.itemconfig(word_text, text=rus, fill="white")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, translate)

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0)
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")
bg_card = canvas.create_image(400, 263, image=front_card)
canvas.config(bg=BACKGROUND_COLOR)
lang_text = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
yes_img = PhotoImage(file="./images/right.png")
yes_button = Button(image=yes_img, highlightthickness=0, command=known)
yes_button.grid(column=0, row=1)

no_img = PhotoImage(file="./images/wrong.png")
no_button = Button(image=no_img, highlightthickness=0, command=unknown)
no_button.grid(column=1, row=1)

next_word()


window.mainloop()
