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

    def remove(self, valor):
        """Elimina un valor de la matriz si existe."""
        try:
            while True:  # Elimina todos los duplicados
                self.elementos.remove(valor)
                self.__nItems -= 1
        except ValueError:
            pass  # Si no hay más elementos para eliminar, se sale del bucle

    def display(self):
        """Muestra el contenido de la matriz."""
        print(self.elementos)


# Código para probar la clase OrderedRecordArray
def main():
    # Crear una matriz ordenada
    array = OrderedRecordArray(clave="numeros")

    # Insertar elementos, incluidos duplicados
    elementos_a_insertar = [5, 10, 5, 15, 10, 20, 5]
    for elem in elementos_a_insertar:
        array.insert(elem)

    print("Contenido de la matriz antes de eliminar duplicados:")
    array.display()

    # Intentar eliminar un valor que existe varias veces
    valor_a_eliminar = 5
    array.remove(valor_a_eliminar)
    print(f"Contenido de la matriz después de eliminar {valor_a_eliminar}:")
    array.display()

    # Intentar eliminar un valor que no existe
    valor_no_existente = 30
    array.remove(valor_no_existente)
    print(f"Contenido de la matriz después de intentar eliminar {valor_no_existente} (sin cambios):")
    array.display()

    # Eliminar otro valor
    valor_a_eliminar = 10
    array.remove(valor_a_eliminar)
    print(f"Contenido de la matriz después de eliminar {valor_a_eliminar}:")
    array.display()


# Ejecutar la función principal
if __name__ == "__main__":
    main()
