from first import first, first_option_2
from fibbo import fibbo

def main():
    continue_menu = True

    while continue_menu:

        try:
            menu = int(input("1. Realizar el primer programa (primera versión)\n2. Realizar el primer programa (segunda versión) \n3. Realizar el segundo programa (fibonnacci)\n4. Salir\nOpción: "))

            if menu == 1:
                first()

            elif menu == 2:
                first_option_2()

            elif menu == 3:
                fibbo()

            elif menu == 4:
                continue_menu = False

            else:
                raise Exception("Número no valido")

        except Exception as e:
            print(e)
            continue

if __name__ == "__main__":
    main()
