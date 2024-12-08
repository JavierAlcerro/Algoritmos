class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        """Agrega un elemento al tope de la pila."""
        self.elementos.append(elemento)

    def pop(self):
        """Elimina y devuelve el elemento del tope de la pila. Lanza una excepción si esta vacia."""
        if not self.esta_vacia():
            return self.elementos.pop()
        raise IndexError("No se puede hacer pop en una pila vacia")

    def peek(self):
        """Devuelve el elemento del tope de la pila sin eliminarlo. Lanza una excepcion si esta vacia."""
        if not self.esta_vacia():
            return self.elementos[-1]
        raise IndexError("No se puede hacer peek en una pila vacia")

    def esta_vacia(self):
        """Devuelve True si la pila esta vacia, de lo contrario False."""
        return len(self.elementos) == 0

    def tamano(self):
        """Devuelve el numero de elementos en la pila."""
        return len(self.elementos)

pila = Pila()

pila.push(10)
pila.push(20)
pila.push(30)

print(f"Elemento en el tope: {pila.peek()}")  

print(f"Elemento eliminado: {pila.pop()}")  

print(f"Elemento en el tope: {pila.peek()}")  

print(f"La pila esta vacia: {pila.esta_vacia()}")  

pila.pop()
pila.pop()

try:
    pila.pop()
except IndexError as e:
    print(f"Error: {e}")  
