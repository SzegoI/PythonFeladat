utasok = [72, 85, 64, 91, 58, 103, 77, 69, 88, 95, 60, 81]

liftmax = int(input("A lift teherbírása (kg): "))

osszeg = 0
for suly in utasok:
     osszeg = osszeg + suly

if osszeg <= liftmax:
      print(f"Az összes tömeg: {osszeg} kg. El lehet férni.")
else:
    print(f"Az összes tömeg: {osszeg} kg. Nem lehet elférni.")

elsoutas = -1
i = 0
while i < len(utasok) and elsoutas == -1:
    if utasok[i] > 100:
        elsoutas = i
    i = i + 1
if elsoutas != -1:
     print(f"Az első 100 kg súly feletti utas: {elsoutas+ 1}. ({utasok[elsoutas]} kg)")
else:
    print("4. feladat: Nincs 100 kg feletti utas.")

