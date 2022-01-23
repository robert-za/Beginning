from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


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

gen_pass_button = Button(text="Generate Password",padx=0, pady=2)
gen_pass_button.grid(row=3,column=2)

add_button = Button(text="Add",width=37, pady=2)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()