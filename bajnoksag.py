vegeredmenyek = input("Eredménysor: ")

gyozes = 0
dont = 0
veres = 0

for betu in vegeredmenyek:
    if betu == "G":
        gyozes = gyozes + 1
    elif betu == "D":
        dont = dont + 1
    elif betu == "V":
        veres = veres + 1

print(f"Győzelem: {gyozes}, döntetlen: {dont} és vereség: {veres}")

pontok = gyozes * 3 + dontet * 1

print(f"A csapat összesen {pontok} pontot szerzett.")

if veres == 0:
    print("Veretlen volt.")
else:
    print("Volt vereség.")