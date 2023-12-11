with open ('zem.txt', 'r', encoding='utf-8') as datne:
    teksts=datne.read()
print(f"Failā ir šāds teksts: {teksts}")
#izdruka simbolu skaitu     burti,cipari,tukšumi,interpunkcijas
skaits=len(teksts)
print(f"Simbolu skaits tekstā ir {skaits}")
#pirmie 10 simboli
print(f"Pirmie 10 simboli ir : {teksts[:10]}")
# pirmais unpēdējais simbols ... kā indeksē simboulus virknē ?
#indeks- katram simbolam sava vieta viknē
#ziema.. z-0, i-1, e-2, m-3, a-4
print(f"Pirmais un pēdējais simbols ir: {teksts[0]} {teksts[-1]}")



