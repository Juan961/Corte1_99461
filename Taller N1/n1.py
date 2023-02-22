def n1():
    # Inicio

    try:
        # Leer
        n1 = float(input("Enter the first number: "))

        if n1 <= 0: raise Exception("The first number cannot be 0 or less")

        # Leer
        n2 = float(input("Enter the second number: "))

        if n2 <= 0: raise Exception("The second number cannot be 0 or less")

        # Operar n1 % n2
        remainder = n1 % n2

        # Operar n1 / n2
        quotient = n1 / n2

        # Imprimir residuo
        print(f"The remainder of {n1} % {n2} is: {remainder}")

        # Imprimir cociente
        print(f"The quotient of {n1} / {n2} is: {quotient}s")

    except Exception as e:
        print(e)

    # Fin

if __name__ == "__main__":
    n1()
