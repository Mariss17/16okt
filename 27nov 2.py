"""fails=open('sad.txt', "a", encoding='utf-8')
fails.write("Šodien sniegs ārā")
fails.close()

ff=open('sad.txt', 'r', encoding='utf-8') 
print(ff.read())"""
#izveido jaunu tukšu failu
"""kk=open("pirmdiena", 'w')"""

#dzēšana
"""
import os
if os.path.exists('big sad.txt'):
    os.remove(big sad.txt)
else:
    print("fails nepastāv")
"""


"""
vards=input("ievadi savu vārdu: ")
try:
    with open(ls, 'w') as ff:
    ff.write(vards)
    print(f"Vārds {vards} ir ierakstits {ls}")

except IOError:
print(f"Kļūda, navar ierakstit failā {ls}")
"""