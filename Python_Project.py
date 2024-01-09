from random import *
from datetime import *
from math import *
#
print("Tere! Olen sinu uus sõber - Python!")
nimi = input("nimi")
nimi = print(", oi kui ilus nimi!")
nimi = print("! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")

if nimi.isalpha() and (nimi.lower()=="1" or nimi.lower()=="0"):
#
try:
    gender=input("Sugu: ")
    if gender.isalpha() and (gender.lower()=="naine" or gender.lower()=="mees"):
        if gender.lower()=="naine":
            print("Ei soobi")
        else:
            try:
                age=int(input("Vanus:"))
                if 16<=age<=18:
                    print("Oled meeskonnas!")
                else:
                    print("Vanus ei soobi")
            except :
                print("Vale vanus! Viga andmetüübiga")
    else:
        print("Sisesta tekst")
except :
    print("Viga andmetüübiga!")

#
a=10            #int
b=2.3           #float
c="programma"   #str
d="1.1"      #str
print(b.is_integer()) #float
print(c.isalpha()) #True
print(d.isalpha()) #false
print(d.isnumeric()) #false
print(d.isdigit()) 
print(c.isdecimal())


#
try:
    s1 = float(input("Введите длину первой стороны квадрата: "))
    s2 = float(input("Введите длину первой стороны квадрата: "))

    if s1 == s2:
        print("Это квадрат!")
    else:
        print("Это не квадрат.")
except :
    print("Где то ошибка посмотрите тип как вы укащали данные!")


#12

hind = float(input("Sisesta toote hind:"))
if hind <= 10: 
    soodustus = hind * 0.1
else:
    soodustus = hind * 0.2
okonnelik_hind = hind - soodustus
print("Lõplik hind on", okonnelik_hind, "€")


#13
try:
    gender=input("kas sa oled mees või naine?")
    if gender.lower()=="naine":
        print("kahjuks, otsime ainult mehi")
    else:
       age=int(input("Palun märige oma vanus"))
       if age>=16 and age <=18:
          print("Sa sobid meie meeskonda")
       else:
          print("kahjuks sa ei sobi meie meeskonda")
except :
    print("Kuskil on viga")



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

