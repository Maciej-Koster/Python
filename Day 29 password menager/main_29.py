from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)

    password_print = password_entry.get()
    if len(password_print) == 0:
        password_entry.insert(0, string=password)
        pyperclip.copy(password)
    else:
        password_entry.delete(0, END)
        password_entry.insert(0, string=password)
        pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_entry():
    website_print = website_entry.get()
    email_print = email_entry.get()
    password_print = password_entry.get()
    text = f"{website_print} | {email_print} | {password_print}" + "\n"
    message = \
        f'''These are detail entered: \n Email: {email_print} \n Password: {password_print} \n Is it ok to save?
        '''

    if len(website_print) == 0 or len(password_print) == 0:
        messagebox.showinfo(title="Oops", message=" Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_print, message=message)
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(text)
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Menager")
window.config(padx=50, pady=50)

# Canvas

background = Canvas(width=200, heigh=200)
photo = PhotoImage(file="logo.png")
background.create_image(100, 100, image=photo)
background.grid(row=0, column=1)

# Label

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries

website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "myemail@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)


# Buttons

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=35, command=save_entry)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
