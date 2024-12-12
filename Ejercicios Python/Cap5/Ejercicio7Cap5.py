class FibonacciIterator:
    def __init__(self, max_value=None):
        """
        Inicializa el iterador de Fibonacci. Si max_value es proporcionado,
        el iterador se detendrá cuando alcance ese valor.
        """
        self.max_value = max_value  # Límite superior opcional para la secuencia
        self.fib_sequence = [0, 1]  # La secuencia de Fibonacci comienza con [0, 1]
        self.index = 1  # Comenzamos en el índice 1 (el primer número calculado es 1)
    
    def next(self):
        """
        Mueve el iterador hacia adelante en la secuencia de Fibonacci y devuelve el siguiente número.
        """
        if self.index >= len(self.fib_sequence):  # Si estamos al final de la secuencia calculada
            # Calculamos el siguiente número de Fibonacci y lo agregamos a la secuencia
            next_value = self.fib_sequence[-1] + self.fib_sequence[-2]
            if self.max_value is not None and next_value > self.max_value:
                raise StopIteration("No hay más elementos en la secuencia de Fibonacci.")
            self.fib_sequence.append(next_value)
        
        # Devolvemos el número actual en la secuencia y avanzamos el índice
        value = self.fib_sequence[self.index]
        self.index += 1
        return value
    
    def anterior(self):
        """
        Mueve el iterador hacia atrás en la secuencia de Fibonacci y devuelve el número anterior.
        """
        if self.index == 1:
            raise StopIteration("No se puede retroceder más allá de F(0).")
        
        # Retrocedemos el índice y devolvemos el número en la secuencia
        self.index -= 1
        return self.fib_sequence[self.index]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return self.next()

    def __str__(self):
        """
        Representación en cadena de la secuencia hasta el valor actual.
        """
        return " -> ".join(map(str, self.fib_sequence[:self.index]))


# Ejemplo de uso
if __name__ == "__main__":
    print("Iterador de Fibonacci hacia adelante y hacia atrás")

    # Crear el iterador
    fib_iter = FibonacciIterator(max_value=100)

    # Avanzar y retroceder en la secuencia
    print("Siguiente (hacia adelante):")
    for _ in range(5):
        print(fib_iter.next(), end=" ")

    print("\nVolver hacia atrás:")
    for _ in range(3):
        print(fib_iter.anterior(), end=" ")

    print("\nAvanzar de nuevo:")
    print(fib_iter.next())  # Repetirá el número que estaba antes de retroceder
    print(fib_iter.next())  # Continuará hacia adelante
    
    print("\nEstado actual del iterador:", fib_iter)
