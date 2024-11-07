import random

# Generar lista de 10 números aleatorios entre 1 y 100
numeros = [random.randint(1, 100) for _ in range(10)]

# Sumar los números
suma_total = sum(numeros)

# Calcular el promedio (dividiendo la suma total entre 10)
promedio = suma_total / 10

# Calcular el porcentaje del promedio respecto a 100
porcentaje = (promedio / 100) * 100

# Imprimir resultados
print(f"Números generados: {numeros}")
print(f"Suma total de los números: {suma_total}")
print(f"Promedio de los números: {promedio:.2f}")
print(f"Porcentaje del promedio respecto a 100: {porcentaje:.2f}%")
