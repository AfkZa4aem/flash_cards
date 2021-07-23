from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
WORDS = {}

# ---------------------------- PANDAS LOGIC ------------------------------- #
data = pandas.read_csv("./data/en_ru.csv")
to_learn = data.to_dict(orient="records")


# ---------------------------- LOGIC ------------------------------- #
def next_word():
    global WORDS, timer
    timer = window.after_cancel(timer)
    WORDS = choice(to_learn)
    eng = WORDS["English"]
    canvas.itemconfig(bg_card, image=front_card)
    canvas.itemconfig(lang_text, text="English", fill="black")
    canvas.itemconfig(word_text, text=eng, fill="black")
    timer = window.after(3000, translate)


def translate():
    rus = WORDS["Russian"]
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
yes_button = Button(image=yes_img, highlightthickness=0, command=next_word)
yes_button.grid(column=0, row=1)

no_img = PhotoImage(file="./images/wrong.png")
no_button = Button(image=no_img, highlightthickness=0, command=next_word)
no_button.grid(column=1, row=1)

next_word()


window.mainloop()
