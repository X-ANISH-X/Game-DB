import tkinter
from tkinter import *

def createLable(root, text, row, col, colspan=1, sticky=W, padx=0, pady=0):
    label = Label(root, text=text)
    label.grid(row=row, column=col, columnspan=colspan, sticky=sticky, padx=padx, pady=pady)
    return label

def createButton(root, name, width, row, col, cmd, sticky=E, padx=0, pady=0):
    button = Button(root, text=name, width=width, command=cmd)
    button.grid(row=row, column=col, sticky=sticky, padx=padx, pady=pady)
    return button

def createList(root, height, width, row, col, rowspan=1, columnspan=1, padx=0, pady=0):
    frame = Frame(root)
    frame.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, padx=padx, pady=pady, sticky=N+S+E+W)
    sb1 = Scrollbar(frame, orient=VERTICAL)
    sb1.pack(side=RIGHT, fill=Y)
    listbox = Listbox(frame, height=height, width=width, yscrollcommand=sb1.set)
    listbox.pack(side=LEFT, fill=BOTH, expand=True)
    sb1.config(command=listbox.yview)
    return listbox

def createEntry(root, row, col, width=17, padx=0, pady=0):
    entry = Entry(root, width=width)
    entry.grid(row=row, column=col, columnspan=2, padx=padx, pady=pady)
    return entry
