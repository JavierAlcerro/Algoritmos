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

def ordenar_cola(cola):
    if cola.esta_vacia():
        return

    for i in range(cola.tamano):
        menor = cola.dequeue()

        for j in range(cola.tamano):
            actual = cola.dequeue()
            if actual < menor:
                cola.enqueue(menor)
                menor = actual
            else:
                cola.enqueue(actual)

        cola.enqueue(menor)

def ejemplo_ordenar_cola():
    cola = ColaCircular(10)

    numeros = [5, 1, 9, 3, 7, 2, 8, 4, 6, 0]
    print("Encolando numeros desordenados:", numeros)
    for numero in numeros:
        cola.enqueue(numero)

    print("\nOrdenando la cola...")
    ordenar_cola(cola)

    print("\nContenido de la cola ordenada:")
    while not cola.esta_vacia():
        print(cola.dequeue(), end=" ")
    print()

ejemplo_ordenar_cola()
