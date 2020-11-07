from tkinter import *
from tkinter import ttk


def matrice_3x3(*args):
    matrice_1=float(mat_1.get())
    matrice_2=float(mat_2.get())
    matrice_3=float(mat_3.get())
    matrice_4=float(mat_4.get())
    matrice_5=float(mat_5.get())
    matrice_6=float(mat_6.get())
    matrice_7=float(mat_7.get())
    matrice_8=float(mat_8.get())
    matrice_9=float(mat_9.get())

    incognita1=(inc_1.get())
    incognita2=(inc_2.get())
    incognita3=(inc_3.get())

    numero1=float(num_1.get())
    numero2=float(num_2.get())
    numero3=float(num_3.get())

    incognita_out_1.set(incognita1)
    incognita_out_2.set(incognita2)
    incognita_out_3.set(incognita3)

    risultato=(((matrice_1*matrice_5*matrice_9)+(matrice_2*matrice_6*matrice_7)+(matrice_3*matrice_4*matrice_8))-((matrice_3*matrice_5*matrice_7)+(matrice_1*matrice_6*matrice_8)+(matrice_2*matrice_4*matrice_9)))
    d1=(((numero1*matrice_5*matrice_9)+(matrice_2*matrice_6*numero3)+(matrice_3*numero2*matrice_8))-((matrice_3*matrice_5*numero3)+(numero1*matrice_6*matrice_8)+(matrice_2*numero2*matrice_9)))
    d2=(((matrice_1*numero2*matrice_9)+(numero1*matrice_6*matrice_7)+(matrice_3*matrice_4*numero3))-((matrice_3*numero2*matrice_7)+(matrice_1*matrice_6*numero3)+(numero1*matrice_4*matrice_9)))
    d3=(((matrice_1*matrice_5*numero3)+(matrice_2*numero2*matrice_7)+(numero1*matrice_4*matrice_8))-((numero1*matrice_5*matrice_7)+(matrice_1*numero2*matrice_8)+(matrice_2*matrice_4*numero3)))

    risultato1.set(d1/risultato)
    risultato2.set(d2/risultato)
    risultato3.set(d3/risultato)

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
    risultato=0
    d1=0
    d2=0
    d3=0
    inc_1.set(clear)
    inc_2.set(clear)
    inc_3.set(clear)
    incognita_out_1.set(clear)
    incognita_out_2.set(clear)
    incognita_out_3.set(clear)
    risultato1.set(clear)
    risultato2.set(clear)
    risultato3.set(clear)
    num_1.set(clear)
    num_2.set(clear)
    num_3.set(clear)





root=Tk()
root.title("Sistema 3x3")
root.geometry("500x500")


mat_1=StringVar()
mat_2=StringVar()
mat_3=StringVar()
mat_4=StringVar()
mat_5=StringVar()
mat_6=StringVar()
mat_7=StringVar()
mat_8=StringVar()
mat_9=StringVar()
inc_1=StringVar()
inc_2=StringVar()
inc_3=StringVar()
incognita_out_1=StringVar()
incognita_out_2=StringVar()
incognita_out_3=StringVar()
num_1=StringVar()
num_2=StringVar()
num_3=StringVar()
risultato1=StringVar()
risultato2=StringVar()
risultato3=StringVar()


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

inc1_entry=Entry(root, width=2, textvariable=inc_1, font=('verdana', 50))
inc1_entry.place(height=100, x=290, y=50)

inc2_entry=Entry(root, width=2, textvariable=inc_2, font=('verdana', 50))
inc2_entry.place(height=100, x=290, y=150)

inc3_entry=Entry(root, width=2, textvariable=inc_3, font=('verdana', 50))
inc3_entry.place(height=100, x=290, y=250)

num1_entry=Entry(root, width=2, textvariable=num_1, font=('verdana', 50))
num1_entry.place(height=100, x=402, y=50)

num2_entry=Entry(root, width=2, textvariable=num_2, font=('verdana', 50))
num2_entry.place(height=100, x=402, y=150)

num3_entry=Entry(root, width=2, textvariable=num_3, font=('verdana', 50))
num3_entry.place(height=100, x=402, y=250)

Label(root, text="SISTEMA 3x3", font=('verdana', 20)).pack(anchor=N)


Label(root, text="RISULTATO:", font=('verdana', 15)).place(height=20, x=0, y=370)
Label(root, text="X", font=('verdana', 15)).place(height=20, x=270, y=190)
Label(root, text="=", font=('verdana', 15)).place(height=20, x=380, y=187)
Label(root, textvariable=risultato1, font=('verdana', 15)).place(height=30, x=150, y=370)
Label(root, textvariable=risultato2, font=('verdana', 15)).place(height=30, x=150, y=410)
Label(root, textvariable=risultato3, font=('verdana', 15)).place(height=30, x=150, y=450)
Label(root, textvariable=incognita_out_1, font=('verdana', 15)).place(height=30, x=130, y=370)
Label(root, textvariable=incognita_out_2, font=('verdana', 15)).place(height=30, x=130, y=410)
Label(root, textvariable=incognita_out_3, font=('verdana', 15)).place(height=30, x=130, y=450)


Button(root, text="CALCOLA", command=matrice_3x3, font=('verdana', 15)).place(height=25, x=0, y=400)

Button(root, text="RESET", command=reset, font=('verdana', 15)).place(height=25, x=0, y=425)

root.bind('<Return>', matrice_3x3)
root.bind('<Return>', reset)

root.mainloop()