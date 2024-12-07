def encontrar_max_min(arreglo):
    if not arreglo:
        return None, None

    max_valor = arreglo[0]
    min_valor = arreglo[0]
    
    for num in arreglo:
        if num > max_valor:
            max_valor = num
        if num < min_valor:
            min_valor = num
    
    return max_valor, min_valor

numeros = [3, 1, 4, 1, 5, 9, -2, 6]
maximo, minimo = encontrar_max_min(numeros)
print(f"Máximo: {maximo}, Mínimo: {minimo}")
