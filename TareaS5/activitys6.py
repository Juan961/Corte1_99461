def factorial(num):
    if ( num == 1 ): return num
    return num * factorial(num-1)

def combinaciones_lineales(n, m):
    return (factorial(n)) / ( ( factorial(m) ) * ( factorial( n - m ) ) )

print(combinaciones_lineales(7, 5))

saludar = lambda nombre: f"Hola {nombre}"

print(saludar("Juan"))
