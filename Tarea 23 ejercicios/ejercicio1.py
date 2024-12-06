def suma_arreglo(numeros):
    suma=0
    for numeros in numeros:
        suma += numeros
    return suma
arreglo = [ 1, 2, 3, 4, 5]
resultado = suma_arreglo(arreglo)
print (f"El resultado es {resultado}")