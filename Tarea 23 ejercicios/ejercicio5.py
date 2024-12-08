def eliminar_duplicados(arreglo):
    return list(set(arreglo))

arreglo = [1, 2, 2, 3, 4, 4, 5]
arreglo_sin_duplicados = eliminar_duplicados(arreglo)

print(f"Arreglo original: {arreglo}")
print(f"Arreglo sin duplicados: {arreglo_sin_duplicados}")
