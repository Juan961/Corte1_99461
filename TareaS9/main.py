import time
import random
import math
from functools import wraps

is_pair = lambda number: number % 2 == 0

def random_function():
    digits = 0
    required = "pair"
    
    while digits < 10:
        number = random.randint(100, 120)

        if number == 110 or number == 115 or number == 119:
            continue

        if required == "pair" and is_pair(number):
            digits += 1
            required = "notPair"
            print(number)
        
        elif required == "notPair" and not is_pair(number):
            digits += 1
            required = "pair"
            print(number)

def calculate():
    operation = int(input("Ingrese la función\n1. Sen\n2. Cos\n3. Tan\n4. Exp\n5. Logaritmo natural\nOpción: "))
    number = float(input("Ingrese el número para calcular: "))

    if operation == 1:
        print( math.sin(number) )
    elif operation == 2:
        print( math.cos(number) )
    elif operation == 3:
        print( math.tan(number) )
    elif operation == 4:
        print( math.exp(number) )
    elif operation == 5:
        print( math.log(number) )

def time_analize(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

@time_analize
def watch_first():
    cadena = "Hola mundo"
    for i in cadena:
        print(i)


@time_analize
def watch_second():
    cadena = "Hola mundo"
    texto = ""

    for i in cadena:
        texto += i + "\n"

    print(texto)

# random_function()
# calculate()
watch_first()
watch_second()
