import tkinter as tk
from tkinter import messagebox

def paradi_sveik():
    vards=ievades_luki.get()
    krasa=ievades_luki2.get()
    messagebox.showinfo("**Sveiciens**", f"Labdien, {vards} ! Mēs tevi izsekoju un zinam kad tev patīk {krasa} krāsa.")

#galvenais logs
logs=tk.Tk()
logs.title("Es sveiks !!")
logs.iconbitmap('runa.ico')
#lukums vārdu ievadei
ievades_luki=tk.Entry(logs, width=30)
ievades_luki.pack(pady=10)
laukums1=tk.Label(logs, text="↑ Vārds ? ↑")
laukums1.pack(padx=5)
laukums=tk.Label(logs, text="↓ Krāsa ? ↓")
laukums.pack(padx=5)
ievades_luki2=tk.Entry(logs, width=30)
ievades_luki2.pack(pady=10)


#poga
sveicien_poga=tk.Button(logs, text="Sveiciens",command=paradi_sveik)
sveicien_poga.pack(pady=10)
#palaižam tkinker logu#
logs.mainloop()