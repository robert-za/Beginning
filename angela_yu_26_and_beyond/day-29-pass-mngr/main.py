from tkinter import *
from tkinter import messagebox
import random
import pyperclip #sudo apt install xclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    password_entry.delete(0, END)
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_nums = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_nums

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def open_writemode_dump(data):
    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

def save():

    new_data = {
        website_entry.get(): {
            "email": username_entry.get(),
            "password": password_entry.get(),
        }
    }
    if username_entry.get() == "" or website_entry.get() == "" or password_entry.get() == "":
        messagebox.showinfo(title="Empy fields!", message="Please do not leave any fields empty!")
    else:
        # is_correct = messagebox.askokcancel(title=website_entry.get(), message=f"Your input: \nEmail: {username_entry.get()}"
        #                                                             f"\nPassword: {password_entry.get()} \nIs it OK?")
        # if is_correct:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            open_writemode_dump(new_data)
        else:
            data.update(new_data)
            open_writemode_dump(data)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def search_password():
    if website_entry.get() != "":
        website = website_entry.get()
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Errrrrror", message="No Data File Found.")
        else:
            if website in data:
                searched_username = data[website]["email"]
                searched_password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Username: {searched_username}\nPassword: {searched_password}")
            else:
                messagebox.showinfo(title="Errrrror", message=f"Website {website} non-existant")
    else:
        pass

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

website_entry = Entry(width=24)
website_entry.grid(row=1,column=1,columnspan=1)
website_entry.focus()

search_button = Button(text="Search", padx=35, pady=2, bg="pink", command=search_password)
search_button.grid(row=1,column=2)

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