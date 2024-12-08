class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        raise IndexError("No se puede hacer pop en una pila vacia")

    def esta_vacia(self):
        return len(self.elementos) == 0

def invertir_cadena(cadena):
    """Invierte una cadena de texto utilizando una pila."""
    pila = Pila()

    for char in cadena:
        pila.push(char)

    cadena_invertida = ''
    while not pila.esta_vacia():
        cadena_invertida += pila.pop()

    return cadena_invertida

texto = "Si voy a pasar Algoritmos"
texto_invertido = invertir_cadena(texto)

print(f"Texto original: {texto}")
print(f"Texto invertido: {texto_invertido}")
