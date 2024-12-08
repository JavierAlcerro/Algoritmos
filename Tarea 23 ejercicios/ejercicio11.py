class Cola:
    def __init__(self):
        self.elementos = []

    def enqueue(self, elemento):
        self.elementos.append(elemento)

    def dequeue(self):
        if self.esta_vacia():
            raise IndexError("No se puede hacer dequeue en una cola vacia.")
        return self.elementos.pop(0)

    def peek(self):
        if self.esta_vacia():
            raise IndexError("No se puede hacer peek en una cola vacia.")
        return self.elementos[0]

    def esta_vacia(self):
        return len(self.elementos) == 0

cola = Cola()
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
print("Peek:", cola.peek())  
print("Dequeue:", cola.dequeue())  
print("Dequeue:", cola.dequeue())  
print("Esta vacia:", cola.esta_vacia())  
cola.dequeue()
print("Esta vacia:", cola.esta_vacia())  