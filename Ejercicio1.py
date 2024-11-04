class StackFullException(Exception):
    #Excepción para indicar que la pila está llena.
    pass

class StackEmptyException(Exception):
    #Excepción para indicar que la pila está vacía.
    pass

class Stack:
    def __init__(self, size):
        self.size = size
        self.items = []

    def is_full(self):
        return len(self.items) == self.size

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.is_full():
            raise StackFullException("No se puede insertar: la pila está llena.")
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise StackEmptyException("No se puede extraer: la pila está vacía.")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise StackEmptyException("No se puede mirar: la pila está vacía.")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def test_stack():
    # Crear una pila de tamaño 3
    stack = Stack(3)

    # Pruebas de inserción
    print("Insertando elementos en la pila...")
    try:
        stack.push(1)
        stack.push(2)
        stack.push(3)
        print("Estado de la pila:", stack)
        
        # Intentar insertar un cuarto elemento
        print("Intentando insertar un cuarto elemento...")
        stack.push(4)
    except StackFullException as e:
        print(e)

    # Pruebas de extracción
    print("\nExtrayendo elementos de la pila...")
    try:
        print("Elemento extraído:", stack.pop())
        print("Estado de la pila:", stack)
        print("Elemento extraído:", stack.pop())
        print("Elemento extraído:", stack.pop())
        print("Estado de la pila:", stack)
        
        # Intentar extraer de una pila vacía
        print("Intentando extraer de una pila vacía...")
        stack.pop()
    except StackEmptyException as e:
        print(e)

if __name__ == "__main__":
    test_stack()
