from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/french_words.csv')

to_learn = data.to_dict(orient='records')
current_card = {}

# ---------------------------- next card------------------------------- #
def already_known():

    to_learn.remove(current_card)

    data_tosave = pd.DataFrame.from_dict(to_learn)
    data_tosave.to_csv("data/words_to_learn.csv", index=False)

    next_card()

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(img_pic, image=front_image)
    flip_timer = window.after(3000, func=flip_card)
    canvas.update()

def flip_card():
    canvas.itemconfig(img_pic, image=back_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
front_image = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# Canvas, tło
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img_pic = canvas.create_image(400, 263, image=front_image)
canvas.grid(column=1, row=1, columnspan=2)

language_text = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))

# Button
right_button = Button(image=right_image, highlightthickness=0, command=already_known)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)

right_button.grid(column=2, row=2)
wrong_button.grid(column=1, row=2)

next_card()

window.mainloop()