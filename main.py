from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():

    # Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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

    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo("WARNING", f"Please don't leave any of the fields empty")
        window.deiconify()
    else:
        question = messagebox.askokcancel("Message",
                                          f"These are the details entered: \nWebsite: {website}\n"
                                          f"Email: {email}\n"
                                          f"Password: {password}\n"
                                          f"Do you want to proceed?")
        if question is True:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                web_entry.delete(0, END)
                password_entry.delete(0, END)
                messagebox.showinfo("Message", "Saved with success")
        else:
            window.deiconify()
            web_entry.delete(0, END)
            password_entry.delete(0, END)





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
web_entry = Entry(width=54)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()
email_entry = Entry(width=54)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "playmolegion@gmail.com")
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

# Buttons
gen_pass = Button(text="Generate Password", width=15, command=password_generator)
gen_pass.grid(row=3, column=2)

add = Button(text="Add", width=46, command=save_data)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()