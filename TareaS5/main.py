def odd_number():
    number = int(input("Ingrese el número para obtener los números impares menores a: "))

    if number <= 0: raise Exception("El número debe ser mayor o igual a 0")

    for i in range(1, number+1):
        if i % 2 != 0:
            print(i, end=", ")

    print("")

def factorial_2(num):
    if ( num == 1 ): return num
    return num * factorial_2(num-1)

print(factorial_2(10))

def factorial():
    number = int(input("Ingrese el número para calcular el factorial: "))

    res = 1

    for i in range(1, number+1):
        res *= i

    print(f"El resultado es {res}")

def number_is_prime():
    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    number = int(input("Ingrese el número para saber si es primo: "))

    if number <= 0: raise Exception("El número debe ser mayor o igual a 0")

    if number == 1:
        print("El número no es primo")
        return

    if number == 2:
        print("El número si es primo")
        return

    for i in range(2, number + 1):
        if is_prime(i):
            print(i, end=", ")

    print("")
    print(f"¿El número es primo? {is_prime(number)}")

def main():
    continue_menu = True

    while continue_menu:
        try:
            number = int(input("Que operación desea realizar\n1. Obtener los números impares menores a un número \n2. Calcular factorial de un número \n3. Calcular si un número es primo e imprimor los números primos menores a este \n4. Salir\nOpción: "))

            if number == 1:
                odd_number()

            elif number == 2:
                factorial()

            elif number == 3:
                number_is_prime()

            elif number == 4:
                print("Thanks have a good day")
                continue_menu = False

            else:
                raise Exception("Número no valido")

        except Exception as e:
            print(e)
            continue

if __name__ == "__main__":
    main()
