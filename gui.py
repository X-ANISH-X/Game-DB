import tkinter
from tkinter import *
from tkinter import messagebox
import os

import tkinterCommands
import userInfo
import signup
import database

def home(username):
    def get_selected_row(event):
        index = gamer_list.curselection()[0]
        global selected_tuple
        selected_tuple = gamer_list.get(index)

    def view_command():
        gamer_list.delete(0, END)
        for row in database.view('gamer'):
            id_name = (row[0], row[1])
            gamer_list.insert(END, id_name)

    def add_gamer_command():
        signup.window()
        view_command()

    def remove_gamer_command():
        try:
            ID = selected_tuple[0]
            if messagebox.askokcancel('Delete User', 'Are you sure you want to remove %s permanently?' % selected_tuple[1]):
                database.delete(ID)
            view_command()
        except:
            print('Select a tuple')
            messagebox.showinfo("Warning", "Select a Gamer.")

    def view_gamer_command():
        try:
            ID = selected_tuple[0]
            print(ID)
            userInfo.window(selected_tuple)
        except:
            print('Select a tuple')
            messagebox.showinfo("Warning", "Select a Gamer.")

    # Main home window GUI
    root = Tk()
    root.title("%s's Gaming Cafe Data" % username)

    cwd = os.path.dirname(os.path.realpath(__file__))
    # print(cwd)

    def on_closing():
        if messagebox.askokcancel('Quit', 'Are you sure you want to quit?'):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    # ROG Cafe image----
    imagePath = cwd + '/images/onepiece.png'
    image = PhotoImage(file=imagePath)
    # Resize the image
    image = image.subsample(1, 1)  # Change these values to adjust the size
    imageLabel = Label(root, image=image)
    imageLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    # tkinterCommands.createLable(root, 'Nishant Gaming Cafe', row=1, col=1)  # insert image and make it bold

    tkinterCommands.createButton(root, 'Refresh', width=17, row=1, col=2, cmd=view_command, sticky='e')
    tkinterCommands.createButton(root, 'Add Gamer', width=17, row=2, col=2, cmd=add_gamer_command)
    tkinterCommands.createButton(root, 'Remove Gamer', width=17, row=3, col=2, cmd=remove_gamer_command)
    tkinterCommands.createButton(root, 'View Gamer', width=17, row=4, col=2, cmd=view_gamer_command)

    gamer_list = tkinterCommands.createList(root, height=20, width=60, row=1, col=0, rowspan=4, columnspan=2)
    gamer_list.bind('<<ListboxSelect>>', get_selected_row)

    # Adjust column weights
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)

    view_command()  # display the Gamers on home screen

    root.mainloop()
