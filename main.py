from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("jp.csv")
data_df = pd.DataFrame(data)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
learned = []

def new_word():
    global flip_timer, idx, learned
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_title, text="Japanese", fill="black")
    idx = random.randint(0, len(data_df))
    while idx in learned:
        idx = random.randint(0, len(data_df))
    canvas.itemconfig(card_word, text=f"\n{data_df.expression[idx]}\n{data_df.reading[idx]}", font=("Arial", 50, "bold"), fill="black")
    canvas.itemconfig(card_bg, image=front_img)
    flip_timer = window.after(4000, func=flip_card)
    return idx

def flip_card():
    global idx
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{data_df.meaning[idx]}", font=("Arial", 30, "bold"), fill="white")
    canvas.itemconfig(card_bg, image=back_img)

def is_known():
    global idx, learned
    learned.append(idx)

    new_word()

flip_timer = window.after(4000, func=flip_card)

canvas = Canvas(width=810, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="card_front.png")
back_img = PhotoImage(file="card_back.png")
card_bg = canvas.create_image(410, 270, image=front_img) #position of the center of the image
card_title = canvas.create_text(400, 150, text="Japanese", font=("Arial", 40, "italic"))
idx = random.randint(0,len(data_df))
card_word = canvas.create_text(400, 263, text=f"\n{data_df.expression[idx]}\n{data_df.reading[idx]}", font=("Arial", 30, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


my_image1 = PhotoImage(file="right.png")
right_button = Button(image=my_image1, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(column=1, row=1)

my_image2 = PhotoImage(file="wrong.png")
wrong_button = Button(image=my_image2, highlightthickness=0, bg=BACKGROUND_COLOR, command=new_word)
wrong_button.grid(column=0, row=1)




window.mainloop()