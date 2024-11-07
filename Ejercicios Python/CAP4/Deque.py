class Deque:
    def __init__(self, max_size):
        self.__max_size = max_size  # Tamaño máximo del deque
        self.__deque = [None] * max_size  # Inicializar la lista como vacía
        self.__front = 0  # Índice del frente
        self.__rear = 0  # Índice de la parte trasera
        self.__count = 0  # Contador de elementos en el deque

    def insertLeft(self, item):
        if self.isFull():
            raise IndexError("No se puede insertar: el deque está lleno.")
        self.__front = (self.__front - 1) % self.__max_size  # Mover el frente hacia la izquierda
        self.__deque[self.__front] = item  # Insertar el elemento en el frente
        self.__count += 1  # Incrementar el contador

    def insertRight(self, item):
        if self.isFull():
            raise IndexError("No se puede insertar: el deque está lleno.")
        self.__deque[self.__rear] = item  # Insertar el elemento en la parte trasera
        self.__rear = (self.__rear + 1) % self.__max_size  # Mover la parte trasera hacia la derecha
        self.__count += 1  # Incrementar el contador

    def removeLeft(self):
        if self.isEmpty():
            raise IndexError("No se puede eliminar: el deque está vacío.")
        item = self.__deque[self.__front]  # Obtener el elemento del frente
        self.__deque[self.__front] = None  # Limpiar la referencia
        self.__front = (self.__front + 1) % self.__max_size  # Mover el frente hacia la derecha
        self.__count -= 1  # Decrementar el contador
        return item  # Devolver el elemento eliminado

    def removeRight(self):
        if self.isEmpty():
            raise IndexError("No se puede eliminar: el deque está vacío.")
        self.__rear = (self.__rear - 1) % self.__max_size  # Mover la parte trasera hacia la izquierda
        item = self.__deque[self.__rear]  # Obtener el elemento de la parte trasera
        self.__deque[self.__rear] = None  # Limpiar la referencia
        self.__count -= 1  # Decrementar el contador
        return item  # Devolver el elemento eliminado

    def peekLeft(self):
        if self.isEmpty():
            raise IndexError("No se puede mirar: el deque está vacío.")
        return self.__deque[self.__front]  # Devolver el elemento en el frente

    def peekRight(self):
        if self.isEmpty():
            raise IndexError("No se puede mirar: el deque está vacío.")
        return self.__deque[(self.__rear - 1) % self.__max_size]  # Devolver el elemento en la parte trasera

    def isEmpty(self):
        return self.__count == 0  # Verificar si el deque está vacío

    def isFull(self):
        return self.__count == self.__max_size  # Verificar si el deque está lleno

    def __len__(self):
        return self.__count  # Devolver el número de elementos en el deque

    def __str__(self):
        # Convertir el deque a una cadena para su visualización
        return str([self.__deque[(self.__front + i) % self.__max_size] for i in range(self.__count)])
