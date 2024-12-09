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

def reorganizar_cola(cola):
    pares = []
    impares = []

    while not cola.esta_vacia():
        numero = cola.dequeue()
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    for numero in pares + impares:
        cola.enqueue(numero)

def ejemplo_reorganizar_cola():
    cola = ColaCircular(10)

    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Encolando numeros:", numeros)
    for numero in numeros:
        cola.enqueue(numero)

    print("\nReorganizando la cola...")
    reorganizar_cola(cola)

    print("\nContenido de la cola reorganizada:")
    while not cola.esta_vacia():
        print(cola.dequeue(), end=" ")
    print()

ejemplo_reorganizar_cola()
