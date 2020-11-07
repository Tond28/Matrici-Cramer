from tkinter import *
from tkinter import ttk


def matrice_2x2(*args):
    matrice_1=float(mat_1.get())
    matrice_2=float(mat_2.get())
    matrice_3=float(mat_3.get())
    matrice_4=float(mat_4.get())

    incognita1=(inc_1.get())
    incognita2=(inc_2.get())

    numero1=float(num_1.get())
    numero2=float(num_2.get())

    if matrice_1/matrice_3!=matrice_2/matrice_4:
        controllo=1
    elif matrice_1/matrice_3==matrice_2/matrice_4:
        if matrice_1/matrice_3!=numero1/numero2:
            controllo=3
        elif matrice_1/matrice_3==numero1/numero2:
            controllo=2
    if controllo==1:
        incognita_out_1.set(incognita1)
        incognita_out_2.set(incognita2)

        risultato=((matrice_1*matrice_4)-(matrice_2*matrice_3))

        risultato1.set(((numero1*matrice_4)-(matrice_2*numero2))/risultato)
        risultato2.set(((matrice_1*numero2)-(numero1*matrice_3))/risultato)
    elif controllo==2:
        incognita_out_1.set("Indeterminato")
    elif controllo==3:
        incognita_out_1.set("Impossibile")

def reset(*args):                                                                           
    clear = ""
    mat_1.set(clear)
    mat_2.set(clear)
    mat_3.set(clear)
    mat_4.set(clear)
    risultato=0
    controllo=0
    inc_1.set(clear)
    inc_2.set(clear)
    incognita_out_1.set(clear)
    incognita_out_2.set(clear)
    risultato1.set(clear)
    risultato2.set(clear)
    num_1.set(clear)
    num_2.set(clear)





root=Tk()
root.title("Matrice 2x2")
root.geometry("500x500")
mainframe = ttk.Frame(root)
mainframe.place(height=0, x=0, y=0)


mat_1=StringVar()
mat_2=StringVar()
mat_3=StringVar()
mat_4=StringVar()
inc_1=StringVar()
inc_2=StringVar()
incognita_out_1=StringVar()
incognita_out_2=StringVar()
num_1=StringVar()
num_2=StringVar()
risultato1=StringVar()
risultato2=StringVar()


mat1_entry=Entry(root, width=2, textvariable=mat_1, font=('verdana', 50))
mat1_entry.place(height=100, x=0, y=50)

mat2_entry=Entry(root, width=2, textvariable=mat_2, font=('verdana', 50))
mat2_entry.place(height=100, x=90, y=50)

mat3_entry=Entry(root, width=2, textvariable=mat_3, font=('verdana', 50))
mat3_entry.place(height=100, x=0, y=150)

mat4_entry=Entry(root, width=2, textvariable=mat_4, font=('verdana', 50))
mat4_entry.place(height=100, x=90, y=150)

inc1_entry=Entry(root, width=2, textvariable=inc_1, font=('verdana', 50))
inc1_entry.place(height=100, x=200, y=50)

inc2_entry=Entry(root, width=2, textvariable=inc_2, font=('verdana', 50))
inc2_entry.place(height=100, x=200, y=150)

num1_entry=Entry(root, width=2, textvariable=num_1, font=('verdana', 50))
num1_entry.place(height=100, x=312, y=50)

num2_entry=Entry(root, width=2, textvariable=num_2, font=('verdana', 50))
num2_entry.place(height=100, x=312, y=150)

Label(root, text="MATRICE 2x2", font=('verdana', 20)).pack(anchor=N)


Label(root, text="RISULTATO:", font=('verdana', 15)).place(height=20, x=0, y=370)
Label(root, text="X", font=('verdana', 15)).place(height=20, x=180, y=140)
Label(root, text="=", font=('verdana', 15)).place(height=20, x=290, y=139)
Label(root, textvariable=risultato1, font=('verdana', 15)).place(height=30, x=150, y=370)
Label(root, textvariable=risultato2, font=('verdana', 15)).place(height=30, x=150, y=400)
Label(root, textvariable=incognita_out_1, font=('verdana', 15)).place(height=30, x=130, y=370)
Label(root, textvariable=incognita_out_2, font=('verdana', 15)).place(height=30, x=130, y=400)


Button(root, text="CALCOLA", command=matrice_2x2, font=('verdana', 15)).place(height=25, x=0, y=400)

Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=0, y=425)

root.bind('<Return>', matrice_2x2)
root.bind('<Return>', reset)

root.mainloop()

print("ciao")