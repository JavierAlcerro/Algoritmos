# Array.py (todo en un solo archivo)

class Array:
    def __init__(self, elementos):
        self.elementos = elementos  # Inicializa la lista de elementos

    # Método para obtener el número máximo
    def getMaxNum(self):
        max_num = None  # Inicialmente no hay números

        for x in self.elementos:
            if isinstance(x, (int, float)):  # Verifica si es un número
                if max_num is None or x > max_num:
                    max_num = x  # Actualiza el número máximo
        return max_num

    # Método para eliminar duplicados
    def removeDupes(self):
        nueva_lista = []  # Nueva lista para almacenar elementos únicos
        for x in self.elementos:
            if x not in nueva_lista:  # Comprobar si el elemento no está en la nueva lista
                nueva_lista.append(x)  # Añadir elemento si es único
        self.elementos = nueva_lista  # Actualizar la lista original

# Código para probar la clase Array
def main():
    # Pruebas con diferentes tipos de matrices
    arrays = [
        Array([10, 3.5, 'texto', 7, 'texto', 10]),  # Duplicados en números y texto
        Array([None, 'hello', 'hello', {}, []]),      # Duplicados en texto
        Array([0, 0.0, -10, 20, -30, 5.5, 20]),       # Duplicados en números
        Array(['a', 'b', 'c', 'a', 'b']),             # Duplicados en letras
        Array([True, 50, 3.14, 'world', True]),       # Duplicados en booleanos
        Array([])                                      # Matriz vacía
    ]

    # Ejecutar getMaxNum en cada matriz y mostrar los resultados
    for i, arr in enumerate(arrays):
        print(f"Matriz {i + 1} antes de eliminar duplicados: {arr.elementos}")
        arr.removeDupes()  # Eliminar duplicados
        print(f"Matriz {i + 1} después de eliminar duplicados: {arr.elementos}")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
