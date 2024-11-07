class DequeFullException(Exception):
    #Excepción para indicar que el deque está lleno.
    pass

class DequeEmptyException(Exception):
    #Excepción para indicar que el deque está vacío.
    pass

class Deque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def insert_left(self, item):
        if self.is_full():
            raise DequeFullException("No se puede insertar: el deque está lleno.")
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1) % self.capacity
        self.items[self.front] = item

    def insert_right(self, item):
        if self.is_full():
            raise DequeFullException("No se puede insertar: el deque está lleno.")
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item

    def remove_left(self):
        if self.is_empty():
            raise DequeEmptyException("No se puede eliminar: el deque está vacío.")
        item = self.items[self.front]
        if self.front == self.rear:  # Solo hay un elemento
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return item

    def remove_right(self):
        if self.is_empty():
            raise DequeEmptyException("No se puede eliminar: el deque está vacío.")
        item = self.items[self.rear]
        if self.front == self.rear:  # Solo hay un elemento
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1) % self.capacity
        return item

    def peek_left(self):
        if self.is_empty():
            raise DequeEmptyException("No se puede mirar: el deque está vacío.")
        return self.items[self.front]

    def peek_right(self):
        if self.is_empty():
            raise DequeEmptyException("No se puede mirar: el deque está vacío.")
        return self.items[self.rear]

    def __str__(self):
        if self.is_empty():
            return "Deque vacío"
        elements = []
        i = self.front
        while True:
            elements.append(self.items[i])
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        return "Deque: " + " ".join(str(x) for x in elements)

class StackFullException(Exception):
    #Excepción para indicar que la pila está llena.
    pass

class StackEmptyException(Exception):
    #Excepción para indicar que la pila está vacía.
    pass

class Stack:
    def __init__(self, capacity):
        self.deque = Deque(capacity)

    def is_empty(self):
        return self.deque.is_empty()

    def is_full(self):
        return self.deque.is_full()

    def push(self, item):
        if self.is_full():
            raise StackFullException("No se puede insertar: la pila está llena.")
        self.deque.insert_right(item)

    def pop(self):
        if self.is_empty():
            raise StackEmptyException("No se puede extraer: la pila está vacía.")
        return self.deque.remove_right()

    def peek(self):
        if self.is_empty():
            raise StackEmptyException("No se puede mirar: la pila está vacía.")
        return self.deque.peek_right()

    def size(self):
        # No hay un método de tamaño en Deque, así que se calcula manualmente
        if self.deque.is_empty():
            return 0
        if self.deque.front <= self.deque.rear:
            return self.deque.rear - self.deque.front + 1
        return self.deque.capacity - (self.deque.front - self.deque.rear - 1)

    def __str__(self):
        return str(self.deque)

# Ejemplo de uso
if __name__ == "__main__":
    stack = Stack(5)

    # Insertar elementos
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Estado de la pila:", stack)

    # Verificar el elemento superior
    print("Elemento superior:", stack.peek())

    # Eliminar elementos
    print("Elemento extraído:", stack.pop())
    print("Estado de la pila:", stack)

    # Insertar más elementos
    stack.push(4)
    stack.push(5)
    print("Estado de la pila:", stack)

    # Mostrar el tamaño de la pila
    print("Tamaño de la pila:", stack.size())
