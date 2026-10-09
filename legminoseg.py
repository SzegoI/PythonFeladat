meresertekek = [42, 55, -1, 61, 48, -1, 70, 66]

darabszam = 0
osszeg = 0
for meres in meresertekek :
    if meres != -1:
        darabszam = darabszam + 1
        osszeg = osszeg + meres
atlag = osszeg / darabszam             
print(f"Érvényes mérések száma: {darabszam}és átlaga: {atlag}")


szoveg = []
for ora in range(len(meresertekek) // 2):
    ora_osszeg = 0
    for i in (2 * ora, 2 * ora + 1):
        if meresertekek[i ] != -1:    
            ora_osszeg = ora_osszeg + meresertekek[i]
    szoveg.append(f"{8 + ora} órától {ora_osszeg}")
print("" + ", ".join(szoveg))


legnagyobb = meresertekek[0]
legnagyobb_index = 0
for i in range(1, len(meresek)):
    if meresertekek[i] > legnagyobb:      
        legnagyobb_index = i

percek = legnagyobb_index * 30
ora = 8 + percek // 60
perc = percek % 60
print(f"A legnagyobb érték: {legnagyobb}és időpontja: {ora}:{perc:02d}")
