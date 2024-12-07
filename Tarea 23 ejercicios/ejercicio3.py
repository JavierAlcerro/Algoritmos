def invertir_arreglo(arreglo):

    for i in range(len(arreglo) - 1, -1, -1):
        print(arreglo[i])

numeros = [1, 2, 3, 4, 5]
invertir_arreglo(numeros)