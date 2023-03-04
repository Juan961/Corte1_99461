def factorial(n):
    res = 1

    for i in range(1, n+1):
        res *= i

    return res

def combinaciones_lineales(n, m):
    return (factorial(n)) / ( ( factorial(m) ) * ( factorial( n - m ) ) )
