# OrderedRecordArray.py

class OrderedRecordArray:
    def __init__(self, clave, tamaño_inicial=5, incremento=5):
        self.clave = clave  # La clave que se utilizará para ordenar
        self.elementos = []  # Inicializa la lista de elementos
        self.__nItems = 0  # Inicializa el contador de elementos
        self.tamaño_maximo = tamaño_inicial  # Almacena el tamaño máximo
        self.incremento = incremento  # Incremento fijo para el crecimiento

    def insert(self, valor):
        """Inserta un valor en la matriz manteniendo el orden."""
        if self.__nItems >= self.tamaño_maximo:
            self.expand()  # Expande la lista si es necesario
        self.elementos.append(valor)
        self.__nItems += 1
        self.elementos.sort()  # Mantiene la lista ordenada

    def expand(self):
        """Expande la capacidad de la lista."""
        # Crear una nueva lista con mayor capacidad
        nueva_capacidad = self.tamaño_maximo + self.incremento
        nueva_lista = [None] * nueva_capacidad
        # Copiar elementos existentes a la nueva lista
        for i in range(self.__nItems):
            nueva_lista[i] = self.elementos[i]
        self.elementos = nueva_lista
        self.tamaño_maximo = nueva_capacidad  # Actualiza el tamaño máximo

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

    def current_capacity(self):
        """Devuelve la capacidad actual de la lista."""
        return self.tamaño_maximo


# Código para probar la clase OrderedRecordArray
def main():
    # Crear una matriz ordenada con capacidad inicial
    array = OrderedRecordArray(clave="numeros", tamaño_inicial=5, incremento=5)

    # Insertar elementos para forzar la expansión de la matriz
    elementos_a_insertar = [10, 20, 5, 15, 25, 30, 35, 40, 45, 50]
    print(f"Capacidad inicial: {array.current_capacity()}")
    
    for elem in elementos_a_insertar:
        array.insert(elem)
        print(f"Insertando {elem}, capacidad actual: {array.current_capacity()}")

    print("Contenido de la matriz después de las inserciones:")
    array.display()


# Ejecutar la función principal
if __name__ == "__main__":
    main()
