#virke ir masivs
"""
a="Labdien"
for x in a:
    print(x)
"""
#virknes garums len()
# len funkcija- pasaka cik gara virkne
"""
a="idk"
print(len(a))
print("idk" in a)
"""
#virkņu sadalīšana
"""
a = "moday"
print(a[2:5]) #dabūj burtus no 2. pozicijas us 5.
print(a[:5]) #dabūj burtus sākuma pozicijas us 5.
print(a[2:]) #dabūj burtus no 2. līdz beigām
#var izmantot negativus indeksus
print(a[-5:-2])
"""
#izmanto for cikls un ...nu (apgriezti vārdi)
"""
vards=input("Ievadi vārdu: ")
apgriezts_vards="" 
for burts in vards[::-1]:
    apgriezts_vards=apgriezts_vards+burts
print("Apgrieztā versija is: " + apgriezts_vards)
"""
#reversed
"""
vards=input("Ievadi vārdu: ")
apgriezts_vards="" 
for burts in reversed(vards):
    apgriezts_vards=apgriezts_vards+burts
print("Apgrieztā versija is: " + apgriezts_vards)
"""
#complex uzd
"""
for skaitlis in range(1, 101):
    if skaitlis %3==0 and skaitlis %5==0:
        print("FizzBuzz")
    elif skaitlis %3==0:
        print("Fizz")
    elif skaitlis %5==0:
        print("Buzz")
    else:
        print("skaitlis")
"""
#easy uzd
"""
teksts=input("ieavadi tekstu: ")

burtuskaits=0
for burts in teksts:
    if burts.isalpha():
        burtuskaits+=1

vardi=teksts.split()

vardusarakts=len(vardi)

print(f"Burtu skaits ir {burtuskaits}")
print(f"Vārdu skaits ir {vardusarakts}")
"""