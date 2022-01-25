from tkinter import *
from tkinter import messagebox
import random
import pyperclip #sudo apt install xclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_nums = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_nums

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    if username_entry.get() == "" or website_entry.get() == "" or password_entry.get() == "":
        messagebox.showinfo(title="Empy fields!", message="Please do not leave any fields empty!")
    else:

        is_correct = messagebox.askokcancel(title=website_entry.get(), message=f"Your input: \nEmail: {username_entry.get()}"
                                                                    f"\nPassword: {password_entry.get()} \nIs it OK?")

        if is_correct:
            with open("data.txt", "a") as data:
                data.write(f"{website_entry.get()} | {username_entry.get()} | {password_entry.get()}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50,pady=50)
window.title("Password Manager")

canvas = Canvas(width=200,height=200,highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image = lock_img)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:",pady=10)
website_label.grid(row=1, column=0)

username_label = Label(text="Username:",pady=10)
username_label.grid(row=2, column=0)

password_label = Label(text="Password:",pady=10)
password_label.grid(row=3, column=0)

website_entry = Entry(width=40)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

username_entry = Entry(width=40)
username_entry.grid(row=2,column=1,columnspan=2)
username_entry.insert(0,"somename@somemailbox.com")

password_entry = Entry(width=24)
password_entry.grid(row=3,column=1)

gen_pass_button = Button(text="Generate Password",padx=0, pady=2, command=generate)
gen_pass_button.grid(row=3,column=2)

add_button = Button(text="Add",width=37, pady=2, command = save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()