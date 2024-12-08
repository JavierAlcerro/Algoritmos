class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        raise IndexError("No se puede hacer pop en una pila vacia")

    def peek(self):
        if not self.esta_vacia():
            return self.elementos[-1]
        raise IndexError("No se puede hacer peek en una pila vacia")

    def esta_vacia(self):
        return len(self.elementos) == 0

def verificar_balanceo(cadena):
    """Verifica si una cadena de parentesis está balanceada."""
    pila = Pila()
    pares = {')': '(', '}': '{', ']': '['}  

    for char in cadena:
        if char in '({[':  
            pila.push(char)
        elif char in ')}]':  
            if pila.esta_vacia() or pila.pop() != pares[char]:
                return False

    return pila.esta_vacia()

cadenas = [
    "()",          
    "({[]})",      
    "({[})",       
    "(()",         
    "",            
    "{[()]}",      
    "{[()]]}"      
]

for cadena in cadenas:
    resultado = "Balanceada" if verificar_balanceo(cadena) else "No balanceada"
    print(f"Cadena: {cadena} -> {resultado}")
