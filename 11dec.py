"""
Tkinter, Pysimple

importē moduli
izveidot galveno logu
pievieno logrīkus
izsauc galveno notikumu logu
"""

from tkinter import*
import tkinter as tk 

#izveido galveno logu
logs=Tk()

logs.geometry("400x300+100+50")
logs.title("Molbert mājiņa")
#kā nomainīt ikonu ?
logs.iconbitmap('Home.ico')

#pievieno pogas..... nepieciešamos
#pack metode
"""
sarkana_poga=Button(logs, text="Sarkana", fg="red")
sarkana_poga.pack(side=LEFT)
zala_poga=Button(logs, text="Zaļa", fg="green")
zala_poga.pack(side=BOTTOM)
dzeltena_poga=Button(logs, text="Dzeltena", fg="yellow")
dzeltena_poga.pack(side=RIGHT)
zila_poga=Button(logs, text="Zila", fg="blue")
zila_poga.pack(side=TOP)
"""
#grid metode
"""
sarkana_poga=Button(logs, text="Violēts", fg="purple")
sarkana_poga.grid(row=0, column=0)

nosaukums1=Label(logs, text="Vārds").grid(row=1, column=2)
ievads1=Entry(logs).grid(row=1, column=3)
nosaukums2=Label(logs, text="Uzvārds").grid(row=2, column=2)
ievads2=Entry(logs).grid(row=2, column=3)
"""
#place metode
nosaukums1=Label(logs, text="Vārds").place(x=50, y=50)
ievads1=Entry(logs).place(x=85, y=50)

#sāksim izpildīt
logs.mainloop()
