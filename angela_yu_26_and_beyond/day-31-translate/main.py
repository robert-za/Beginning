from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("./data/italian_words.csv")
to_learn = data.to_dict(orient="records")


def next_word():
    random_it = random.choice(to_learn)["Italian"]
    canvas.itemconfig(language, text="Italian")
    canvas.itemconfig(word, text=random_it)
    

window = Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.title("Flash Cards")

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
canvas.create_image(400,263,image=card_front)
canvas.grid(row=0,column=0,columnspan=2)

language = canvas.create_text(400,150,text="language",fill="black",font=("Ariel",40, "italic"))

word = canvas.create_text(400,263,text="word",fill="black",font=("Ariel",60,"bold"))

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image,highlightthickness=0,command=next_word)
wrong_button.grid(row=1,column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image,highlightthickness=0,command=next_word)
right_button.grid(row=1,column=1)

next_word()

window.mainloop()