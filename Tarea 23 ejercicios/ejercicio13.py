class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cola = [None] * capacidad
        self.frente = 0
        self.fin = -1
        self.tamano = 0

    def enqueue(self, elemento):
        if self.esta_llena():
            raise OverflowError("No se puede agregar a una cola llena.")
        self.fin = (self.fin + 1) % self.capacidad
        self.cola[self.fin] = elemento
        self.tamano += 1

    def dequeue(self):
        if self.esta_vacia():
            raise IndexError("No se puede hacer dequeue en una cola vacia.")
        elemento = self.cola[self.frente]
        self.cola[self.frente] = None
        self.frente = (self.frente + 1) % self.capacidad
        self.tamano -= 1
        return elemento

    def peek(self):
        if self.esta_vacia():
            raise IndexError("No se puede hacer peek en una cola vacia.")
        return self.cola[self.frente]

    def esta_vacia(self):
        return self.tamano == 0

    def esta_llena(self):
        return self.tamano == self.capacidad

def ejemplo_cola_circular():
    cola = ColaCircular(5)

    print("Agregando elementos a la cola circular...")
    for i in range(5):
        print(f"Encolando: {i}")
        cola.enqueue(i)

    try:
        cola.enqueue(5)
    except OverflowError as e:
        print(e)

    print("\nEliminando elementos de la cola circular...")
    while not cola.esta_vacia():
        print(f"Desencolando: {cola.dequeue()}")

    try:
        cola.dequeue()
    except IndexError as e:
        print(e)

ejemplo_cola_circular()
