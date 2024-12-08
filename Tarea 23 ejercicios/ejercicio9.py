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

def calcular_expresion(lista):
    """Calcula el resultado de una expresion en notacion postfija usando una pila."""
    pila = Pila()

    for elemento in lista:
        if isinstance(elemento, (int, float)):  
            pila.push(elemento)
        elif elemento in "+-*/":  
            try:
                b = pila.pop()
                a = pila.pop()
            except IndexError:
                return "Error: expresion mal formada"

            if elemento == "+":
                pila.push(a + b)
            elif elemento == "-":
                pila.push(a - b)
            elif elemento == "*":
                pila.push(a * b)
            elif elemento == "/":
                if b == 0:
                    return "Error: division por cero"
                pila.push(a / b)
        else:
            return "Error: elemento desconocido en la expresion"

    if pila.esta_vacia() or len(pila.elementos) > 1:
        return "Error: expresion mal formada"

    return pila.pop()

expresiones = [
    [3, 4, '+'],         
    [5, 1, 2, '+', 4, '*', '+', 3, '-'],  
    [7, 3, '/'],          
    [4, 0, '/'],          
    [2, '+'],             
]

for expresion in expresiones:
    resultado = calcular_expresion(expresion)
    print(f"Expresion: {expresion} -> Resultado: {resultado}")
