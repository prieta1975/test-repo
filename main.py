from tkinter import *
from tkinter import filedialog

fileName = "C:"

def doNothing():
    print("Nada")

def openFile():
    f = filedialog.askopenfile(parent=root)
    print(f.name)


# Window creation
root = Tk()

# Creates menu bar & config menu bar in window object
menuBar = Menu(master=root)
root.config(menu=menuBar)

# Creates File menu option & adds options for File menu option
fileMenu = Menu(master=menuBar)
menuBar.add_cascade(label="Fichero", menu=fileMenu)
fileMenu.add_command(label="New Project...", command=openFile)

# creates sub menu "SubMenu" for File menu option "Submenu" & creates options for sub menu
subMenu = Menu(master=fileMenu)
fileMenu.add_cascade(label="Submenu", menu=subMenu)
subMenu.add_command(label="Opc Subm")

#Creates File menu additional options
fileMenu.add_command(label="New...", command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=doNothing)

# Creates Edit menu option
editMenu = Menu(master=menuBar)
menuBar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Copy", command=doNothing)

# Creates Label to write output
w = Label(root, text="Hello World  ")
w.pack()


# Keeps window open
root.geometry("200x200")
root.mainloop()

