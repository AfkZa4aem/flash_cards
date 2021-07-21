from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- PANDAS LOGIC ------------------------------- #
data = pandas.read_csv("./data/en_ru.csv")
words_dict = data.to_dict(orient="records")
random_dict = choice(words_dict)
eng_word = random_dict["English"]
# rus_word = random_dict["Russian"]


# ---------------------------- LOGIC ------------------------------- #
def new_word():
    random_pair = choice(words_dict)
    eng = random_pair["English"]
    # rus_word = random_dict["Russian"]
    canvas.itemconfig(word_text, text=eng)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0)
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")
canvas.create_image(400, 263, image=front_card)
canvas.config(bg=BACKGROUND_COLOR)
lang_text = canvas.create_text(400, 150, text="English", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text=eng_word, font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Buttons
yes_img = PhotoImage(file="./images/right.png")
yes_button = Button(image=yes_img, highlightthickness=0, command=new_word)
yes_button.grid(column=0, row=1)

no_img = PhotoImage(file="./images/wrong.png")
no_button = Button(image=no_img, highlightthickness=0, command=new_word)
no_button.grid(column=1, row=1)


window.mainloop()
