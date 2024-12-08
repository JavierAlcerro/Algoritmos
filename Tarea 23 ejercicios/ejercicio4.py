def numero_en_arreglo(arreglo, numero):

    for elemento in arreglo:
        if elemento == numero:
            return True
    return False
    
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numero_a_buscar = 9

if numero_en_arreglo(numeros, numero_a_buscar):
    print(f"El numero {numero_a_buscar} esta presente en el arreglo")
else:
    print(f"El numero {numero_a_buscar} no esta presente en el arreglo")
