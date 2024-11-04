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

# Ejemplo de uso
if __name__ == "__main__":
    deque = Deque(5)

    # Insertar elementos
    deque.insert_right(1)
    deque.insert_right(2)
    deque.insert_left(0)
    print(deque)

    # Verificar los elementos
    print("Frente:", deque.peek_left())
    print("Final:", deque.peek_right())

    # Eliminar elementos
    deque.remove_left()
    print(deque)
    deque.remove_right()
    print(deque)

    # Insertar más elementos
    deque.insert_right(3)
    deque.insert_left(-1)
    print(deque)

    # Mostrar el estado final del deque
    print("Estado final del deque:", deque)
