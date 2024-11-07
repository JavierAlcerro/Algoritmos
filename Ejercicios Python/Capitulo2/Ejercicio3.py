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


# Código para probar la clase Array
def main():
    # Pruebas con diferentes tipos de matrices
    arrays = [
        Array([10, 3.5, 'texto', 7]),          # Mezcla de números y texto
        Array([None, 'hello', {}, []]),        # Sin números
        Array([0, 0.0, -10, 20, -30, 5.5]),    # Con ceros, negativos y flotantes
        Array(['a', 'b', 'c']),                # Solo cadenas
        Array([True, 50, 3.14, 'world']),      # Booleanos, números y cadenas
        Array([])                               # Matriz vacía
    ]

    # Ejecutar getMaxNum en cada matriz y mostrar los resultados
    for i, arr in enumerate(arrays):
        print(f"Matriz {i+1}: {arr.elementos}")
        print(f"  Número máximo: {arr.getMaxNum()}")

    # Crear una lista ordenada a partir de la matriz de números
    for i, arr in enumerate(arrays):
        if any(isinstance(x, (int, float)) for x in arr.elementos):  # Solo si hay números
            ordenados = ordenar_matriz(arr)
            print(f"Matriz {i+1} ordenada: {ordenados}")

def ordenar_matriz(array):
    """Ordena los números de la matriz utilizando deleteMaxNum."""
    numeros_ordenados = []
    while True:
        max_num = array.getMaxNum()
        if max_num is None:
            break  # Sale si no hay más números
        numeros_ordenados.append(max_num)
        
        # Crear una nueva matriz sin el número máximo
        array.elementos.remove(max_num)  # Elimina el número máximo
    return numeros_ordenados

# Ejecutar la función principal
if __name__ == "__main__":
    main()
