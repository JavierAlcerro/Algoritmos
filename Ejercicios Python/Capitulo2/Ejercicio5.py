# OrderedRecordArray.py

class OrderedRecordArray:
    def __init__(self, clave):
        self.clave = clave  # La clave que se utilizará para ordenar
        self.elementos = []  # Inicializa la lista de elementos
        self.__nItems = 0  # Inicializa el contador de elementos

    def insert(self, valor):
        """Inserta un valor en la matriz manteniendo el orden."""
        self.elementos.append(valor)
        self.__nItems += 1
        self.elementos.sort()  # Mantiene la lista ordenada

    def merge(self, arr):
        """Fusiona otra matriz ordenada en esta."""
        if self.clave != arr.clave:
            raise ValueError("Las claves de ambos arrays deben ser idénticas.")

        # Crear una nueva lista suficientemente grande
        merged_list = [None] * (self.__nItems + arr.__nItems)
        i, j, k = 0, 0, 0  # Índices para self, arr y merged_list

        # Fusionar las dos listas
        while i < self.__nItems and j < arr.__nItems:
            if self.elementos[i] <= arr.elementos[j]:
                merged_list[k] = self.elementos[i]
                i += 1
            else:
                merged_list[k] = arr.elementos[j]
                j += 1
            k += 1

        # Copiar los elementos restantes de self
        while i < self.__nItems:
            merged_list[k] = self.elementos[i]
            i += 1
            k += 1

        # Copiar los elementos restantes de arr
        while j < arr.__nItems:
            merged_list[k] = arr.elementos[j]
            j += 1
            k += 1

        # Actualizar la lista de elementos y el número de elementos
        self.elementos = merged_list[:k]  # Truncar a la nueva longitud
        self.__nItems = k  # Actualizar el número de elementos

    def display(self):
        """Muestra el contenido de la matriz."""
        print(self.elementos)


# Código para probar la clase OrderedRecordArray
def main():
    # Crear dos matrices ordenadas
    array1 = OrderedRecordArray(clave="numeros")
    array2 = OrderedRecordArray(clave="numeros")

    # Insertar elementos aleatorios en las matrices
    import random
    for _ in range(5):
        array1.insert(random.randint(1, 20))
        array2.insert(random.randint(10, 30))

    print("Contenido de la matriz 1 antes de la fusión:")
    array1.display()
    print("Contenido de la matriz 2 antes de la fusión:")
    array2.display()

    # Fusionar la segunda matriz en la primera
    array1.merge(array2)

    print("Contenido de la matriz 1 después de la fusión:")
    array1.display()


# Ejecutar la función principal
if __name__ == "__main__":
    main()
