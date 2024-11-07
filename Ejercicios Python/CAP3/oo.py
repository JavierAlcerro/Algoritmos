def median(self):
    if self.__nItems == 0:
        raise Exception("El arreglo está vacío")  # Manejo de caso vacío

    # Ordenamos el arreglo
    self.bubbleSort()  # Puedes usar cualquier método de ordenamiento que prefieras

    # Encontramos el índice medio
    mid = self.__nItems // 2

    # Si el número de elementos es impar, devolvemos el elemento central
    if self.__nItems % 2 == 1:
        return self.__a[mid]
    # Si es par, devolvemos el promedio de los dos elementos centrales
    else:
        return (self.__a[mid - 1] + self.__a[mid]) / 2
