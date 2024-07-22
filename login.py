import re
import tkinter
from tkinter import *
from tkinter import messagebox

import database
import gui


# Function to validate username
def validate_username(username):
    if 3 <= len(username) <= 20:
        return True
    return False


# Function to validate password
def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True


# Login Button click from login Frame
def login():
    username = usernameEntry.get()
    password = passwordEntry.get()

    if not validate_username(username):
        messagebox.showerror("Error", "Invalid username. It must be between 3 and 20 characters long.")
        return

    if not validate_password(password):
        messagebox.showerror("Error",
                             "Invalid password. It must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character.")
        return

    rows = database.view_owner(username)
    if not rows:
        print('Invalid user name or password')
        messagebox.showerror("Oops!", 'Invalid Username')
    else:
        if rows[0][1] == password:
            print(rows)
            loginWindow.destroy()
            gui.home(username)
        else:
            messagebox.showerror('Oops!', 'Invalid Password')
            forgotPassButton.grid(row=2, column=1, sticky=E)


# Signup button click from Login frame
def signUp():
    new_username.set('')
    new_password.set('')
    loginFrame.pack_forget()
    Header['text'] = 'Create Account'
    createAccFrame.pack()


def createAccount():
    username = n_usernameEntry.get()
    password = n_passwordEntry.get()

    if not validate_username(username):
        messagebox.showerror("Error", "Invalid username. It must be between 3 and 20 characters long.")
        return

    if not validate_password(password):
        messagebox.showerror("Error",
                             "Invalid password. It must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character.")
        return

    rows = database.view_owner(username)
    if rows:
        messagebox.showerror("Oops!", 'Username Already Exists')
    else:
        database.insert_owner(username, password)
        messagebox.showinfo('Registered', 'Successfully Signed Up')
        gotoLogin()


def gotoLogin():
    username.set('')
    password.set('')
    createAccFrame.pack_forget()
    Header['text'] = 'LOGIN'
    loginFrame.pack()


# Password reset functions
def passReset():
    new_username.set('')
    new_username.set('')
    loginFrame.pack_forget()
    Header['text'] = "Password Reset"
    passResetFrame.pack()


def gotoLogin_from_passreset():
    username.set('')
    password.set('')
    passResetFrame.pack_forget()
    Header['text'] = "LOGIN"
    loginFrame.pack()


def passResetSubmit():
    username = usernameEntry1.get()
    new_password_1 = passresetEntry1.get()
    new_password_2 = passresetEntry2.get()

    if not validate_username(username):
        messagebox.showerror("Error", "Invalid username. It must be between 3 and 20 characters long.")
        return

    if not validate_password(new_password_1) or not validate_password(new_password_2):
        messagebox.showerror("Error",
                             "Invalid password. It must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character.")
        return

    rows = database.view_owner(username)
    if not rows:
        messagebox.showerror("Oops!", 'Invalid Username')
    else:
        if new_password_1 != new_password_2:
            messagebox.showwarning('Error', 'Passwords do not match.')
        else:
            database.update_owner(username, new_password_1)
            messagebox.showinfo('Success', 'Password Changed')
            gotoLogin_from_passreset()


# Main window login
loginWindow = Tk()
img = PhotoImage(file="../src/images/loginbg.png")

loginWindow.configure(bg='black')
loginWindow.title("ROG Login (owner)")

# bk = Frame(loginWindow, bg="black")

canvas1 = Canvas(loginWindow, width=400, height=400)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(122, 20, image=img, anchor="nw")


def on_closing():
    if messagebox.askokcancel('Quit', 'Are you sure you want to quit?'):
        loginWindow.destroy()


loginWindow.protocol("WM_DELETE_WINDOW", on_closing)

Header = Label(loginWindow, text='LOGIN/SIGN UP', font=('', 35), pady=10, padx=30, bg='black', fg='white')
Header.pack()

username = StringVar()
password = StringVar()
new_username = StringVar()
new_password = StringVar()
new_password2 = StringVar()

# Login Frame
loginFrame = Frame(loginWindow, padx=340, pady=60, bg='black')

usernameLabel = Label(loginFrame, text="Username: ", font=("arial", 25), bg='black', fg="white")
usernameLabel.grid(row=0, column=0)
usernameEntry = Entry(loginFrame, textvariable=username, bd=7, font=("arial", 24))
usernameEntry.grid(row=0, column=1)

passwordLabel = Label(loginFrame, text="Password: ", font=("arial", 25), bg='black', fg='white')
passwordLabel.grid(row=1, column=0)
passwordEntry = Entry(loginFrame, textvariable=password, show='*', bd=7, font=("arial", 24))
passwordEntry.grid(row=1, column=1)

signUpButton = Button(loginFrame, text='Sign Up', font=('', 20), padx=20, pady=7, fg='white', bg='gray', command=signUp)
signUpButton.grid(row=3, column=0, sticky=W)

loginButton = Button(loginFrame, text='Login', font=('', 20), padx=147, pady=7, bg='gray', command=login, fg="white")
loginButton.grid(row=3, column=1)

forgotPassButton = Button(loginFrame, text='Forgot password', font=('', 20), fg='white', bg='black', command=passReset)

loginFrame.pack()

# Create Account frame
createAccFrame = Frame(loginWindow, padx=100, pady=10, bg='black')

n_usernameLabel = Label(createAccFrame,font=("arial", 25), text="Username: ", bg='black', fg='white')
n_usernameLabel.grid(row=0, column=0)
n_usernameEntry = Entry(createAccFrame,font=("arial", 25), textvariable=new_username, bd=3)
n_usernameEntry.grid(row=0, column=1)

n_passwordLabel = Label(createAccFrame,font=("arial", 25), text="Password: ", bg='black', fg='white')
n_passwordLabel.grid(row=1, column=0)
n_passwordEntry = Entry(createAccFrame, textvariable=new_password,font=("arial", 25), show='*', bd=3)
n_passwordEntry.grid(row=1, column=1)

gotoLoginButton = Button(createAccFrame, text='Go to Login', font=('', 20), padx=20, pady=7, fg='white', bg='gray', command=gotoLogin)
gotoLoginButton.grid(row=2, column=0, sticky=W)

createAccButton = Button(createAccFrame, text='Create Account', font=('', 20), padx=147, pady=7, bg='gray',fg='white',
                         command=createAccount)
createAccButton.grid(row=2, column=1)

# Reset Password
passResetFrame = Frame(loginWindow, padx=100, pady=10, bg='black')

usernameLabel = Label(passResetFrame, text="Username: ", bg='black', fg='white')
usernameLabel.grid(row=0, column=0)
usernameEntry1 = Entry(passResetFrame, textvariable=new_username, bd=3)
usernameEntry1.grid(row=0, column=1)

passresetLabel1 = Label(passResetFrame, text="New Password: ", bg='black', fg='white')
passresetLabel1.grid(row=1, column=0)
passresetEntry1 = Entry(passResetFrame, textvariable=new_password, show='*', bd=3)
passresetEntry1.grid(row=1, column=1)

passresetLabel2 = Label(passResetFrame, text="Re-Enter Password: ", bg='black', fg='white')
passresetLabel2.grid(row=2, column=0)
passresetEntry2 = Entry(passResetFrame, textvariable=new_password2, show='*', bd=3)
passresetEntry2.grid(row=2, column=1)

gotoLoginButton = Button(passResetFrame, text='Go to Login', font=('', 10), padx=10, pady=10, fg='white', bg='black', command=gotoLogin_from_passreset)
gotoLoginButton.grid(row=3, column=0, sticky=W)

submitButton = Button(passResetFrame, text='Submit', font=('', 15), padx=5, pady=5, bg='black', fg='white' ,command=passResetSubmit)
submitButton.grid(row=3, column=1)

loginWindow.mainloop()
