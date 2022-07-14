from tkinter import *

def button_clicked():
    miles = float(input.get())
    km_distance = miles*1.609344
    is_equal_label.config(text=km_distance)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)

is_equal_label = Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal_label.grid(column=0, row=1)

is_equal_label = Label(text="0", font=("Arial", 12, "bold"))
is_equal_label.grid(column=1, row=1)

#Entry
input = Entry(width=10)
input.grid(column=1, row=0)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()