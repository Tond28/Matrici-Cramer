from tkinter import *
from tkinter import ttk, Canvas
from tkinter import filedialog
import os


def open_matrice2x2():
    os.system('"%s"' %"matrice2x2 tk.py")

def open_matrice3x3():
    os.system('"%s"' %"matrice 3x3.py")

def open_sistema2x2():
    os.system('"%s"' %"sistema2x2.py")

def open_sistema3x3():
    os.system('"%s"' %"sistema3x3.py")


root=Tk()

root.title("Matrici")
root.geometry("200x200")

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Matrici", menu=filemenu)
filemenu.add_command(label="Matrice 2x2", command=open_matrice2x2)
filemenu.add_command(label="Matrice 3x3", command=open_matrice3x3)

filemenu2 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Metodo di Cramer", menu=filemenu2)
filemenu2.add_command(label="Matrice2x2", command=open_sistema2x2)
filemenu2.add_command(label="Matrice3x3", command=open_sistema3x3)

root.config(menu=menubar)

Label(root, text="Program by", font=('verdana', 19)).place(height=34, x=5, y=20)
Label(root, text="Filippo Tondelli", font=('verdana', 19)).place(height=34, x=5, y=60)

root.mainloop()


