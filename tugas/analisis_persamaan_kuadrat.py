print("Analisis Persamaan Kuadrat")
a = float(input("Koefisien a: "))
b = float(input("Koefisien b: "))
c = float(input("Koefisien c: "))

if a == 0:
    print("Bukan persamaan kuadrat.")
else:
    d = b**2 - 4*a*c
    print(f"Diskriminan: {d:.2f}")
    if d > 0:
        x1 = (-b + d**0.5) / (2 * a)
        x2 = (-b - d**0.5) / (2 * a)
        print(f"Dua akar real: x1 = {x1:.2f}, x2 = {x2:.2f}")
    else:
        if d == 0:
            x = -b / (2 * a)
            print(f"Akar real kembar: x = {x:.2f}")
        else:
            print("Tidak ada akar real.")