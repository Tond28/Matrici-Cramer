from tkinter import *
from tkinter import ttk

def matrice_3x3(*args):
    try:
        matrice_1=float(mat_1.get())
        matrice_2=float(mat_2.get())
        matrice_3=float(mat_3.get())
        matrice_4=float(mat_4.get())


        risultato.set((matrice_1*matrice_4)-(matrice_2*matrice_3))

    except ValueError:
        pass

def reset(*args):                                                                           
    clear = ""
    mat_1.set(clear)
    mat_2.set(clear)
    mat_3.set(clear)
    mat_4.set(clear)
    risultato.set(clear)

root=Tk()
root.title("Matrice 2x2")
root.geometry("250x350")



mat_1=StringVar()
mat_2=StringVar()
mat_3=StringVar()
mat_4=StringVar()
risultato=StringVar()

mat1_entry=Entry(root, width=2, textvariable=mat_1, font=('verdana', 50))
mat1_entry.place(height=100, x=0, y=50)

mat2_entry=Entry(root, width=2, textvariable=mat_2, font=('verdana', 50))
mat2_entry.place(height=100, x=90, y=50)

mat3_entry=Entry(root, width=2, textvariable=mat_3, font=('verdana', 50))
mat3_entry.place(height=100, x=0, y=150)

mat4_entry=Entry(root, width=2, textvariable=mat_4, font=('verdana', 50))
mat4_entry.place(height=100, x=90, y=150)

Label(root, text="MATRICE 2x2", font=('verdana', 20)).pack(anchor=N)


Label(root, text="RISULTATO:", font=('verdana', 15)).place(height=20, x=0, y=270)
Label(root, textvariable=risultato, font=('verdana', 15)).place(height=20, x=130, y=270)
Button(root, text="CALCOLA", command=matrice_3x3, font=('verdana', 15)).place(height=25, x=0, y=300)

Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=150, y=300)

root.bind('<Return>', matrice_3x3)
root.bind('<Return>', reset)

root.mainloop()