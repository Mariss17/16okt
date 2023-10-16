# dalības operatori
# in | not in
"""
burts="t"

if burts not in "Java": 
  print("Burts T nav vārdā iekļauts.")
else:
  print("Burts T ir vārdā iekļauts.")
"""
# UN, VAi izmantošana IF
# and | or
"""
x=200
y=1000

if ((x<y) or (y%11 ==0)) :
    print("viens nosacijums izpildās")
else:
    print("texts if wrong")
"""
# preikšraksts pass
"""
x=100
y=4

if x<y:
    pass #te reaksīšu vēlāk
print("labrīt")
"""

# Lambda funkcija
"""
x=lambda a: a+10
print(x(-3))

ai= lambda t,u: t*u
print(ai(5,6))

ui=lambda k,i,s : k+i+s #darbība
print(ui (16, 6, -2 )) # arguments (())

h=lambda k: k**5 if k%5==0 else k**7
print(h(2))
"""
# vai dalās gan ar 5, gan ar 7
"""
skaitlis=int(input("ievadi skaitli: "))
if(skaitlis%5 == 0) and (skaitlis%7 == 0):
 print("dalās gan ar 5, gan ar 7")
else:
 print("nedalās")
"""
# def - atslēgvārds
"""
def funkcijas_nosaukums():
 print("bum burum")

print("labrīt")
vasara=funkcijas_nosaukums()
print(vasara)
"""
#uzdevums nr.1
"""
def izvele_skaitlim(skaitlis): # parametrs ir mainīgais kurš strādā unkcijas ietvaros
 darbiba={
      "a": lambda x: x**2,
      "b": lambda x: x**3,
      "c": lambda x: x*2,
    }
 if skaitlis>10:
    rezultats=darbiba["a"](skaitlis)
elif skaitlis<-10:
    rezultats=darbiba["b"](skaitlis)
else:
    rezultats=darbiba["c"](skaitlis)
return rezultats

rez=izvele_skaitlim(11)
print(rez)
"""
#uzd nr.2
"""
saraksts=[1,2,3,4,5,6,7,8,9,10] #masīvs

filtrets_saraksts=list(filter(lambda x: x%2==0, saraksts))

print("pāra skaitļi sarakstā:", filtrets_saraksts)
"""
#uzd nr.3
"""
sarakts=[1,2,3,4,5] #masīvs

#map - katram vienumam masīvā
dublets_saraksts=list(map(lambda x: x*2, sarakts))
print("Dublēts sarakts:", dublets_saraksts)
"""
#uzd nr.4
"""
#ternāro operatoru lietojums

skaitlis=7
rez="Pozitīvs" if skaitlis>0 else "Negatīvs vai nulle"
print(rez)

x=10
y=20
lielaka=x if x>y else y
print(lielaka)
"""
#uzd nr.5
"""
lirtotājs ievada 2 skaitļus, jaizveido programa kas šos skaitļus salīdzina
izveidojot funkciju ar 2 parametriem
"""
"""

def noteikt_skaitlus(skaitlis1, skaitlis2):
    if skaitlis1>0 and skaitlis2>0:
        return "abi skaitļi ir pozitīvi"
    elif skaitlis1<0 and skaitlis2<0:
        return "abi skaitļi ir negatīvi"
    elif skaitlis1==0 or skaitlis2==0:
        return "vizmas viens skaitlis ir nulle"
    else: 
        return "skaitļi ir ar dažādām zīmēm.."

sk1=int(input("ievadi pirmo skaitli: "))
sk2=int(input("ievadi otro skaitli: "))
rezultats=noteikt_skaitlus(sk1, sk2)
print(rezultats)
"""
#uzd nr.6
"""
def validet_vardu(vards) :
    if len(vards)<3:
        return "vārds ir pārāk īss"
    elif lean(vards)>20:
        return "vārds pārāk garš"
    elif not vards.isalpha():
        return "vārds drikst saturēt tikai burtus"
    else:
        return "vards der"
    
ievade=input("ievadi savu vārdu: ")
rezultas=validet_vardu(ievade)
print(rez)
"""



