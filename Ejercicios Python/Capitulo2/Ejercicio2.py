# array_test.py

class Array:
    def __init__(self, elementos):
        self.elementos = elementos  # Inicializar la lista de elementos

    # Método para eliminar y devolver el número máximo
    def eliminarMaxNum(self):
        max_num = None
        max_index = -1

        # Buscar el número máximo y su índice
        for i, x in enumerate(self.elementos):
            if isinstance(x, (int, float)):
                if max_num is None or x > max_num:
                    max_num = x
                    max_index = i

        # Si se encontró un número máximo, lo eliminamos y lo devolvemos
        if max_index != -1:
            del self.elementos[max_index]  # Eliminar el número máximo
            return max_num
        return None  # Si no hay números, devuelve None

# Código de prueba
if __name__ == "__main__":
    # Pruebas con diferentes tipos de matrices
    arrays = [
        Array([10, 3.5, 'texto', 7]),          # Mezcla de números y texto
        Array([None, 'hello', {}, []]),        # Sin números
        Array([0, 0.0, -10, 20, -30, 5.5]),    # Con ceros, negativos y flotantes
        Array(['a', 'b', 'c']),                # Solo cadenas
        Array([True, 50, 3.14, 'world']),      # Booleanos, números y cadenas
        Array([])                               # Matriz vacía
    ]

    # Ejecutar eliminarMaxNum en cada matriz y mostrar los resultados
    for i, arr in enumerate(arrays):
        print(f"Matriz {i + 1}: {arr.elementos}")
        max_num = arr.eliminarMaxNum()  # Llamar al nuevo método
        print(f"  Número máximo eliminado: {max_num}")
        print(f"  Matriz después de eliminar el máximo: {arr.elementos}")
