def first():
    # Check if the number is a valid input first
    number = str(int(input("Ingrese un número de entre 2 y 8 dígitos: ")))

    if len( number ) < 2: raise Exception("El número tiene menos de 2 dígitos")
    if len( number ) > 8: raise Exception("El número tiene más de 8 dígitos")

    numbers_equals_to_five = 0
    numbers_differents_to_five = 0

    for i in number:
        if int(i) == 5:
            print("salto")
            numbers_equals_to_five += 1
        else:
            print(i)
            numbers_differents_to_five += 1

    print(f"Dígitos diferentes a 5: { numbers_differents_to_five }")
    print(f"Dígitos iguales a 5: { numbers_equals_to_five }")
    print(f"Número de dígitos: { len( number ) }")

def first_option_2():
    number = int(input("Ingrese un número de entre 2 y 8 dígitos: "))

    if len( str(number) ) < 2: raise Exception("El número tiene más de 2 dígitos")
    if len( str(number) ) > 8: raise Exception("El número tiene más de 8 dígitos")

    numbers_equals_to_five = 0
    numbers_differents_to_five = 0
    digits = 0

    while number > 0:
        digits += 1

        temp = number % 10

        number = number // 10

        if temp == 5:
            print("salto")
            numbers_equals_to_five += 1
        else:
            print(temp)
            numbers_differents_to_five += 1

    print(f"Dígitos diferentes a 5: { numbers_differents_to_five }")
    print(f"Dígitos iguales a 5: { numbers_equals_to_five }")
    print(f"Número de dígitos: { digits }")
