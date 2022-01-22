from tkinter import *
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=200)
window.config(padx=20, pady=20)

# def button_click():
#     #input.get() taken from entry object
#     my_label.config(text = input.get())


# #Label
# my_label = Label(text = "I am a label", font=("Arial", 24))
# # my_label["text"] = "New Text"
# my_label.config(text = "Newer Text", padx=30, pady=30)
# # my_label.pack()
# # my_label.place(x=100, y=200)
# my_label.grid(column=0,row=0)

# #Button
# button = Button(text = "OK", command = button_click)
# # button.pack()
# button.grid(column=1,row=1)

# #Button
# button_useless = Button(text = "Cancel")
# # button.pack()
# button_useless.grid(column=2,row=0)

def miles_to_km():
    km = round(float(miles_input.get()) * 1.609)
    km_results_label.config(text=f"{km}")

#Entry
miles_input = Entry(width=10)
miles_input.grid(column=1,row=0)

miles_unit_label = Label(text="Miles")
miles_unit_label.config(padx=15,pady=15)
miles_unit_label.grid(column=2,row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.config(padx=15,pady=15)
is_equal_label.grid(column=0,row=1)

km_results_label = Label(text="0")
km_results_label.config(padx=15,pady=15)
km_results_label.grid(column=1,row=1)

km_unit_label = Label(text="Km")
km_unit_label.config(padx=15,pady=15)
km_unit_label.grid(column=2,row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.config(padx=15,pady=15)
calculate_button.grid(column=1,row=2)






window.mainloop()