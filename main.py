from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    question = messagebox.askyesno("Message", "Do you want to proceed?")
    if question is False:
        exit()

    with open("data.txt", "a") as file:
        file.write(f"{website} | {email} | {password}\n")
        web_entry.delete(0, END)
        password_entry.delete(0, END)
        messagebox.showinfo("Message", "Saved with success")





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
gen_pass = Button(text="Generate Password", width=15)
gen_pass.grid(row=3, column=2)

add = Button(text="Add", width=46, command=save_data)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()