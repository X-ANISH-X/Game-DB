import tkinter
from tkinter import *
from tkinter import messagebox
import os
import re

import tkinterCommands
import database

cwd = os.path.dirname(os.path.realpath(__file__))
unique_ID_path = cwd + '/unique_id.py'


# Function to validate email
def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None


# Function to validate name
def validate_name(name):
    return 3 <= len(name) <= 50  # Example constraint


# Function to validate gamer tag
def validate_gamer_tag(gamer_tag):
    if 3 <= len(gamer_tag) <= 20:
        if re.search(r'[A-Z]', gamer_tag) and re.search(r'[a-z]', gamer_tag) and re.search(r'[0-9]', gamer_tag) and re.search(r'[\W_]', gamer_tag):
            return True
    return False


# Function to validate age
def validate_age(age):
    return age.isdigit() and 18 <= int(age) <= 120  # Updated constraint


# Database commands
def add_gamer_info(gamer_name, gamer_email, gamer_tag, age):
    """Inserting New Gamer data into gamer table"""
    unique_ID = 0
    # Getting Unique id
    with open(unique_ID_path) as unique_IDFile:
        unique_ID = unique_IDFile.read()
        print(unique_ID)
    unique_ID = int(unique_ID) + 1

    print(gamer_name, gamer_email)
    database.insert(int(unique_ID), gamer_name, gamer_email, gamer_tag, age)

    # Storing incremented unique id
    with open(unique_ID_path, "w") as unique_IDFile:
        unique_IDFile.write(str(unique_ID))
        unique_IDFile.close()


# Function to set placeholder text
def set_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.config(fg='grey')
    entry.bind("<FocusIn>", lambda event: clear_placeholder(event, entry, placeholder))
    entry.bind("<FocusOut>", lambda event: add_placeholder(event, entry, placeholder))


def clear_placeholder(event, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, "end")
        entry.config(fg="black")


def add_placeholder(event, entry, placeholder):
    if not entry.get():
        entry.insert(0, placeholder)
        entry.config(fg="grey")


# Main window
def window():
    """New Window for signing up the new user"""
    new_user = Toplevel()
    new_user.title("Sign up")

    cwd = os.path.dirname(os.path.realpath(__file__))

    demoCafe = cwd + '/images/welcome1.png'
    print(demoCafe)
    cafe = PhotoImage(file=demoCafe)
    label = Label(new_user, image=cafe)
    label.grid(row=0, column=0, columnspan=4)

    def get_info():
        name = gamer_name_entry.get()
        email = gamer_email_entry.get()
        gamer_tag = gamer_tag_entry.get()
        age = gamer_age_entry.get()

        if name == "Enter your name":
            name = ""
        if email == "Enter your email":
            email = ""
        if gamer_tag == "Enter your gamer tag":
            gamer_tag = ""
        if age == "Enter your age (18+)":
            age = ""

        if not validate_name(name):
            messagebox.showerror("Error", "Invalid name. Name must be between 3 and 50 characters long.")
            return
        if not validate_email(email):
            messagebox.showerror("Error", "Invalid email address. Please enter a valid email.")
            return
        if not validate_gamer_tag(gamer_tag):
            messagebox.showerror("Error", "Invalid gamer tag. Gamer tag must be between 3 and 20 characters long, and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
            return
        if not validate_age(age):
            messagebox.showerror("Error", "Invalid age. Age must be a number between 18 and 120.")
            return

        print(name, ' ', email, ' ', gamer_tag, ' ', age)  # Debug line
        add_gamer_info(name, email, gamer_tag, age)
        messagebox.showinfo("Success", "User information added successfully!")
        new_user.destroy()

    tkinterCommands.createLable(new_user, 'Name: ', row=1, col=0, sticky=E)
    gamer_name_entry = tkinterCommands.createEntry(new_user, row=1, col=1, width=100)
    set_placeholder(gamer_name_entry, "Enter your name")

    tkinterCommands.createLable(new_user, 'Email: ', row=2, col=0, sticky=E)
    gamer_email_entry = tkinterCommands.createEntry(new_user, row=2, col=1, width=100)
    set_placeholder(gamer_email_entry, "Enter your email")

    tkinterCommands.createLable(new_user, 'Gamer Tag: ', row=3, col=0, sticky=E)
    gamer_tag_entry = tkinterCommands.createEntry(new_user, row=3, col=1, width=100)
    set_placeholder(gamer_tag_entry, "Enter your gamer tag (must have a capital letter, digit and a symbol)")

    tkinterCommands.createLable(new_user, 'Age: ', row=4, col=0, sticky=E)
    gamer_age_entry = tkinterCommands.createEntry(new_user, row=4, col=1, width=100)
    set_placeholder(gamer_age_entry, "Enter your age (18+)")

    tkinterCommands.createButton(new_user, 'Submit', width=12, row=5, col=1, cmd=get_info)

    new_user.mainloop()


if __name__ == "__main__":
    window()
