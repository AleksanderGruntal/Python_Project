from random import *
from datetime import *
#9



#8 Poes
arve_nr=datetime.now() #date.today()
print(arve_nr)
tsekk="Arve: 12345/nToode Hind Kogus Summa/n"
summa=0
toode1="piim"
hind=randint(50,150)/100
v=input("Toode:"+toode1+"Hind"+str(hind)+"Kas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu?"))
    tsekk+=toode1+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"/n"
    summa+=mitu*hind
toode="Kommid"
hind=randint(600,1500)/100
if v=="kommid":
    mitu=int(input("Mitu?"))
    tsekk+=toode1+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"/n"
    summa+=mitu*hind
toode="leib"
hind=randint(90,300)/100
if v=="leib":
    mitu=int(input("Mitu?"))
    tsekk+=toode1+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"/n"
    summa+=mitu*hind

#7 Inimeselt pikkus ja sugu 
sugu=input("Kas sa oled mees või naine?").lower()
if sugu=="naine" or sugu=="n":
    l1=155
    l2=170
    l3=255
elif sugu=="mees" or sugu=="m":
    l1=160
    l2=180
    l3=255
else:
    l1=0
    print("Viga")
if l1!=0:
   try:
     pikkus=int(input("Sisesta oma pikkus"))
     if pikkus>29 and pikkus<l1:
        vastus="Lühike"
     elif pikkus>l1 and pikkus<l2:
        vastus="Keskmine"
     elif pikkus>l2 and pikkus<=l3:
        vastus="Pikk"
     else:
         vastus="tundmatu"
     print("Sinu pikkus on {0}".format(vastus))
   except:
    print("Vale andmete formaat!")
   
#6 Inimese pikkus
try:
     pikkus=int(input("Sisesta oma pikkus"))
     if pikkus>29 and pikkus<155:
        vastus="Lühike"
     elif pikkus>155 and pikkus<170:
        vastus="Keskmine"
     elif pikkus>170 and pikkus<=255:
        vastus="Pikk"
     else:
         vastus="tundmatu"
     print("Sinu pikkus on {0}".format(vastus))
except:
    print("Vale andmete formaat!")

