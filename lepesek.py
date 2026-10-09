lepesszam = [6500, 8200, 4300, 10100, 7600, 12000, 5400, 9800, 3900, 11200]

osszeg = 0

for lepes in lepesszam:
    osszeg = osszeg + lepes

atlag = osszeg /len(lepesszam)
print(f"Összesen {osszeg} lépés és lépések átlaga: {atlag}.")

maxlepes = [0]
maxnap = 0

for i in range(1, len(lepesszam)):
    if lepesszam[i] > maxlepes:
        maxlepes = lepessszam[i]
        maxnap = i + 1

print(f"A legtöbb lépés: {maxlepes}, a {maxnap}. napon volt.")

darabszam = 0
for lepes in lepesszam:
    if lepes >= 10000:
        darabszam = darabszam + 1
print(f"{darabszam} napon volt legalább 10000 lépés megtéve.")
