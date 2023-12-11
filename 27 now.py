"""
open()
kādas datnes ? teksta - .txt, .csv ...... JSON
.txt
"""
"""
def lasit_datni():
    #pajauta ievadit datnes nosaukumu
    datnes_nosaukums=input("Ieavadi datnes nosaukumu : ")
    #atveram failu un lasam tās saturu
    try:
        with open(datnes_nosaukums, 'r', encoding='utf-8') as fails:
            saturs=fails.read()
            print(f"Datnes saturs ir : {saturs}")

    except FileNotFoundError:
        print("Norādīto failu nevar atrast !")
if __name__=="__main__":
    lasit_datni()
"""
"""
read()- atgriež visu informāciju
readline()- atgriež vienu rindu
"""
"""
fails=open('bot.txt', 'r', encoding='utf-8')
#pārluko visu failu pa rindiņām
for iv in fails:
    print(iv)

    fails.close()
    """