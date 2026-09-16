a = float(input("Sisi a: "))
b = float(input("Sisi b: "))
c = float(input("Sisi c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Segitiga sama sisi")
    else:
        if a == b or a == c or b == c:
            print("Segitiga sama kaki")
        else:
            print("Segitiga sembarang")
else:
    print("Ketiga sisi tidak membentuk segitiga")
    