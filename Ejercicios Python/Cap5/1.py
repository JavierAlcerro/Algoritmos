def factorial(n):
    if n < 0:
        return
    resultado = 1
    for i in range (1, n+1):
        resultado *=i
    return resultado

print(factorial(5))