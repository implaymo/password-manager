from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    # Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = web_entry.get().title().rstrip(" ")
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo("WARNING", f"Please don't leave any of the fields empty")
    else:
        try:
            with open("data.json", "r") as file:
                # Read data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Update old data with new_Data
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)


def search():
    # Get entries
    website = web_entry.get().title().rstrip(" ")
    password = password_entry.get()
    try:
        if len(website) > 0 and len(password) == 0:
            with open("data.json", "r") as file:
                # Read file into data
                data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo("WARNING", f"File not found. Search another website.")
    else:
        if website in data:
            # Gets website dict info from the entry by user
            user_info = data.get(website)
            messagebox.showinfo(f"{website}",
                                f"Email: {user_info['email']}\nPassword: {user_info['password']}")
        else:
            messagebox.showinfo("WARNING", f"No details for {website} exists.")











# ---------------------------- UI SETUP ------------------------------- #

# Setup window
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

# Create Canvas and Image
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Labels
website = Label(text="Website:")
website.grid(row=1, column=0)
email_user = Label(text="Email/Username:")
email_user.grid(row=2, column=0)
password = Label(text="Password:")
password.grid(row=3, column=0)

# Entries
web_entry = Entry(width=34)
web_entry.grid(row=1, column=1)
web_entry.focus()
email_entry = Entry(width=54)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "playmolegion@gmail.com")
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

# Buttons
gen_pass = Button(text="Generate Password", width=15, command=password_generator)
gen_pass.grid(row=3, column=2)

search = Button(text="Search", width=15, command=search)
search.grid(row=1, column=2)

add = Button(text="Add", width=46, command=save_data)
add.grid(row=4, column=1, columnspan=2)


window.mainloop()
