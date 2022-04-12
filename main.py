'''
* A képernyőre írást igénylő részfeladatok eredményék megjelenítése előtt írja a képernyőre a feladat sorszámát (például: 3. feladat:)!
* Az egyes feladtokban a kiírásokat a minta szerint készítse el!
* Az ékezetmentes kiírás is elfogadott.
* A program megírásakor a fájlban lévő adatok helyes szerkezetét nem kell ellenőriznie, feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak megfelelnek
* Megoldását úgy készítse el, hogy az azonos szerkezetű, de tetszőleges bemeneti adatok mellet is helyes eredményt adjon

Hozz létre egy osztályt (class) létrehozása NEM KÖTELEZŐ DE több pontot lehet kapni osztály használata esetén, 
ami reprezentálja egy alkalmazott példányait (object) istance. Az osztály konstruktora (constructor) paraméterként kapja meg a beolvasott sort, 
és ebből határozza meg az adott attribútomokat (property). 

1. feladat:
A feladat megoldásához hozzon létre grafikus vagy konzolalkalmazást (projektet) "Lift" azonosítóval!

2. feladat:
Olvassa be a "lift.txt" állományban lévő adatokat és tárolja el el egy olyan adatszerkezetben , ami a további feladatok megoldására alkalmas! A fájlban legfeljebb 1000 sor lehet.

3. feladat:
Hatáozza meg és írja ki a minta szerint, hogy a vizsgált időszakban hány alkalommal használták a liftet!

4. feladat:
Írja ki a képernyőre a minta szerint, hogy a vizsgált időszak mettől meddig tartott!

5. feladat:
Határozza meg és írja ki a minta szerint, hogy melyik volt a legnagyobb sorszámú célszint az időszakban!

Minta:
3. feladat: Összes lifthasználat: 175
4. feladat: Időszak: 2018.03.06 - 2018.03.19
5. feladat: Célszint max: 5
'''

# Lehetséges megoldás

class Lift:
    def __init__(self, sor):
        datum, sorszam, indulo, erkezo = sor.strip().split(" ")
        self.datum = datum
        self.sorszam = sorszam
        self.indulo = indulo
        self.erkezo = erkezo

lista = []
with open("lift.txt") as f:
    for sor in f:
        lista.append(Lift(sor))
        
#3. feladat
print(f"3. feladat: Összes lifthasználat: {len(lista)}")

#4. feladat

'''
for sor in lista:
  ido1 = max(lista, key=lambda x:x.datum).datum
  ido2 = min(lista, key=lambda x:x.datum).datum
print(f"4. feladat: Időszak: {ido2[:-1]} - {ido1[:-1]}")

'''
# Vagy

legkisebb = lista[0].datum
legnagyobb = lista[0].datum
for sor in lista:
  if sor.datum < legkisebb:
    legkisebb = sor.datum
  if sor.datum > legnagyobb:
    legnagyobb = sor.datum
print(f"4. feladat: Időszak: {legkisebb[:-1]} - {legnagyobb[:-1]}")

  

#5. feladat

'''
for sor in lista:
  legnagyobb = max(lista, key=lambda x:x.erkezo).erkezo
print(f"5. feladat: Célszint max: {legnagyobb}")
'''

# Vagy

maximalis = lista[0].erkezo
for sor in lista:
  if sor.erkezo > maximalis:
    maximalis = sor.erkezo
print(f"5. feladat: Célszint max: {maximalis}")

