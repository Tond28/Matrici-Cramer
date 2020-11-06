from tkinter import *
from tkinter import ttk


def matrice_3x3(*args):
    try:
        matrice_1=float(mat_1.get())
        matrice_2=float(mat_2.get())
        matrice_3=float(mat_3.get())
        matrice_4=float(mat_4.get())
        matrice_5=float(mat_5.get())
        matrice_6=float(mat_6.get())
        matrice_7=float(mat_7.get())
        matrice_8=float(mat_8.get())
        matrice_9=float(mat_9.get())

        risultato.set(((matrice_1*matrice_5*matrice_9)+(matrice_2*matrice_6*matrice_7)+(matrice_3*matrice_4*matrice_8))-((matrice_3*matrice_5*matrice_7)+(matrice_1*matrice_6*matrice_8)+(matrice_2*matrice_4*matrice_9)))

    except ValueError:
        pass

def reset(*args):                                                                           
    clear = ""
    mat_1.set(clear)
    mat_2.set(clear)
    mat_3.set(clear)
    mat_4.set(clear)
    mat_5.set(clear)
    mat_6.set(clear)
    mat_7.set(clear)
    mat_8.set(clear)
    mat_9.set(clear)
    risultato.set(clear)




root=Tk()
root.title("Matrice 3x3")
root.geometry("300x450")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)


mat_1=StringVar()
mat_2=StringVar()
mat_3=StringVar()
mat_4=StringVar()
mat_5=StringVar()
mat_6=StringVar()
mat_7=StringVar()
mat_8=StringVar()
mat_9=StringVar()
risultato=StringVar()

mat1_entry=Entry(root, width=2, textvariable=mat_1, font=('verdana', 50))
mat1_entry.place(height=100, x=0, y=50)

mat2_entry=Entry(root, width=2, textvariable=mat_2, font=('verdana', 50))
mat2_entry.place(height=100, x=90, y=50)

mat3_entry=Entry(root, width=2, textvariable=mat_3, font=('verdana', 50))
mat3_entry.place(height=100, x=180, y=50)

mat4_entry=Entry(root, width=2, textvariable=mat_4, font=('verdana', 50))
mat4_entry.place(height=100, x=0, y=150)

mat5_entry=Entry(root, width=2, textvariable=mat_5, font=('verdana', 50))
mat5_entry.place(height=100, x=90, y=150)

mat6_entry=Entry(root, width=2, textvariable=mat_6, font=('verdana', 50))
mat6_entry.place(height=100, x=180, y=150)

mat7_entry=Entry(root, width=2, textvariable=mat_7, font=('verdana', 50))
mat7_entry.place(height=100, x=0, y=250)

mat8_entry=Entry(root, width=2, textvariable=mat_8, font=('verdana', 50))
mat8_entry.place(height=100, x=90, y=250)

mat9_entry=Entry(root, width=2, textvariable=mat_9, font=('verdana', 50))
mat9_entry.place(height=100, x=180, y=250)

Label(root, text="MATRICE 3x3", font=('verdana', 20)).pack(anchor=N)


Label(root, text="RISULTATO:", font=('verdana', 15)).place(height=20, x=0, y=370)
Label(root, textvariable=risultato, font=('verdana', 15)).place(height=20, x=130, y=370)
Button(root, text="CALCOLA", command=matrice_3x3, font=('verdana', 15)).place(height=25, x=0, y=400)

Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=200, y=400)

root.bind('<Return>', matrice_3x3)
root.bind('<Return>', reset)

root.mainloop()