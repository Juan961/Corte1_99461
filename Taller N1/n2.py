def n2():
    # Inicio

    try:
        # Leer altura
        height = float(input("Enter your height (cm): "))

        # Si altura es igual o menor que cero
        if height <= 0: raise Exception("Height cannot be 0 or less")

        # Leer peso
        weight = float(input("Enter your height (kg): "))

        # Si peso es igual o menor que cero
        if weight <= 0: raise Exception("Weight cannot be 0 or less")

        # Calcular IMC
        imc = round( ( weight / ( ( height / 100 ) ** 2 ) ), 4)

        # Imprimir IMC
        print(f"Your IMC is: {imc}")

    except Exception as e:
        print(e)

    # Fin

if __name__ == "__main__":
    n2()
