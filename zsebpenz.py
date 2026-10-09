koltekezes = [1200 , 800, 1500, 700, 900, 1100, 400]

egyenleg = 5000
elmaradt = 0 
elso_elmaradt = 0 

for i in range(len(koltekezes)):
    if koltekezes[i] <= egyenleg:
        egyenleg = egyenleg - koltekezes[i]

    else:
        elmaradt = elmaradt + 1           
        if elso_elmaradt == 0:
            elso_elmaradt = i + 1         
    napi_egyenlegek.append(str(egyenleg))

print("2. feladat: " + " ".join(napi_egyenlegek))

if elmaradt > 0:
    print(f"{elmaradt} napon maradt el a vásárlás, először az {elso_elmaradt} napon.")
else:
    print("Sikerült minden nap vásárolni.")

if egyenleg >= 500:
    print("Maradt tartalék.")
else:
    print("Nem maradt tartalék.")