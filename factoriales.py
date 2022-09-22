def factorial(n):
    """Calcula la factorial de n.

    n int > 0 
    returns n!
    """
    if n == 1:
        return 1

    return n * factorial(n - 1)

n = int(input('Escribe un entero: '))

print(factorial(n))