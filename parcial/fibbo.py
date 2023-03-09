def fibbo():
    number = int(input("Ingrese el número de veces que desee ver la serie fibbonacci: "))

    a = 0
    b = 1

    print(f"{a}, {b}", end=", ")

    for _ in range(2, number):
        temp = a

        a = b
        b = temp + b

        print(b, end=", ")

    print("")
