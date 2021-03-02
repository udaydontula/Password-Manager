from tkinter import *
from tkinter import messagebox
import paswdgnt
import json


# ----------------------------- SEARCH PASSWORD ------------------------------------#

def find_password():
    pass


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generate():
    new_password = paswdgnt.password_generator()
    pass_box.insert(END, new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    user_password = pass_box.get()
    user = email_box.get()
    email = website_box.get()

    if len(user_password) == 0 or len(user) == 0 or len(email) == 0:
        messagebox.showerror(title="Empty Field", message="Please don't leave any field empty...!!")

    else:
        user_option = messagebox.askokcancel(title=email, message=f"These are the Details:\nEmail : {user}\n"
                                                                  f"Password : {user_password}\nIs it ok to save?")

        if user_option:

            with open("password_data.txt", "a") as file:
                file.write(f"   {email}     |    {user}      |       {user_password}    \n")
                pass_box.delete(first=0, last=END)
                website_box.delete(first=0, last=END)
                website_box.focus()

        else:
            pass_box.delete(first=0, last=END)
            website_box.delete(first=0, last=END)
            website_box.focus()


# ---------------------------- UI SETUP ------------------------------- #

# Window


window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

# Canvas

canvas = Canvas(width=200, height=200)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(105, 100, image=bg_image)
canvas.grid(row=1, column=2)

# Label

website = Label(text="Website:")
website.grid(row=2, column=1)

user_name = Label(text="Email/Username:")
user_name.grid(row=3, column=1)

password = Label(text="Password:")
password.grid(row=4, column=1)

# Entry

website_box = Entry(width=33)
website_box.grid(row=2, column=2)
website_box.focus()

email_box = Entry(width=50)
email_box.grid(row=3, column=2, columnspan=2)
email_box.insert(END, "46uday.d@gmail.com")

pass_box = Entry(width=33)
pass_box.grid(row=4, column=2)

# Buttons

password_generator = Button(width=13, height=1, text="Generate", command=password_generate)
password_generator.grid(row=4, column=3)

add = Button(width=45, height=1, text="Add", command=save_data)
add.grid(row=5, column=2, columnspan=2)

search = Button(width=13, height=1, text="Search", command=find_password)
search.grid(row=2, column=3)

window.mainloop()
