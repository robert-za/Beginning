from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"


try:
    data = pandas.read_csv("./data/words_to_learn.csv")
    print("opening words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/italian_words.csv")
    print("opening italian_words.csv")
finally:
    to_learn = data.to_dict(orient="records")
    current_card = {}


def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language, text="Italian", fill="black")
    canvas.itemconfig(word, text=current_card["Italian"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def supp_word():
    to_learn.remove(current_card)
    pandas.DataFrame(to_learn).to_csv("./data/words_to_learn.csv", index=False)
    next_word()


def flip_card():
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)
    

window = Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
window.title("Flash Cards")

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400,263,image=card_front)
canvas.grid(row=0,column=0,columnspan=2)

language = canvas.create_text(400,150,text="language",fill="black",font=("Ariel",40, "italic"))

word = canvas.create_text(400,263,text="word",fill="black",font=("Ariel",60,"bold"))

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image,highlightthickness=0,command=next_word)
wrong_button.grid(row=1,column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image,highlightthickness=0,command=supp_word)
right_button.grid(row=1,column=1)

next_word()

window.mainloop()