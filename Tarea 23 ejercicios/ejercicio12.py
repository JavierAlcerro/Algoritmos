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

def atencion_cliente():
    cola = Cola()

    print("Clientes llegando al banco...")
    for numero_cliente in range(1, 10):
        print(f"Cliente {numero_cliente} llega y se agrega a la cola.")
        cola.enqueue(f"Cliente {numero_cliente}")

    print("\nAtendiendo a los clientes...")
    while not cola.esta_vacia():
        cliente_atendido = cola.dequeue()
        print(f"Atendiendo a {cliente_atendido}.")

atencion_cliente()
