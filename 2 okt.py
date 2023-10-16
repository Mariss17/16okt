# Cikla konstrukcijas
#1. for ciklu 
"""
# lai īterētu caur sarakstiem
saraksts=[1,2,3,4,5]
for elements in saraksts:
    print(elements)
"""
#2. cikls for, apstrādājot veselu skaitļu intervālu
# funkcija range
"""
a=int(input())
s=0
for i in range(1,a+1):
    s+=i
print(s)

for i in range(10,5,-2):
    print(i)
"""
#3. cikls for, apstrādājot elementu kopu.
"""
burti=["aka","paka","laka"]
for i in burti:
    print("Sveiki, " + i + "!")
"""
#4. cikls ar preikšnosacijumu while
#5. 
#6. cikla pārtraukšana un turpināšana
"""
saraksts=[1,2,3,4,5]
for elements in saraksts:
    if elements==3:
        continue #pārtrauc šo iterāciju un turpinam ar nākamo
    if elements==5:
        break #iziet no cikla ja elements ir 5
    print(elements)
"""
#7. enumerate cikls, funkcija kas ļauj iegūt gan indeksu gan vērtību
"""
sarakts=['a','b','c']
for index, vertiba in enumerate(sarakts):
    print(f"indeks ir: {index}, vērtība {vertiba}")
"""
#uzdevuma - 
#izdrukāt visus pāra skaitļus no 10 - 100, gala punktus ieaskaitot
#1. risinājums
"""
for skaitlis in range(10,101):
    if skaitlis %2==0:
        print(skaitlis)
"""
#2. risinājums
"""
for skitlis in range(10,101,2):
    print(skitlis)
"""
# for cickls ar /sarakstu aptrādi/
"""
sarakts=[10,20,30,40,50,60]
rezultats=[] #tukš saraksts
for skaitlis in sarakts:
    rezultats.append(skaitlis*2)
print(rezultats)
"""
#while cickls ar lietotāja ievadi
""""\
ivade=''#simbolu virkne ir tukša
while ivade != "iziet":
    ivade=input("ievadiet 'iziet', lai pārtrauktu! ")
"""
# for cickls ar vairākiem sarakstiem /ZIP funkcija

vardi=["Anna", "Bots", "Negudrelis"]
vecumi=[19, 2, 12]
for vardi, vecums in zip(vardi,vecumi):
    print(f"{vardi} ir {vecums} gadus vecs/a")







