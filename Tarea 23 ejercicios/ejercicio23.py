class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def contar_nodos_hoja(raiz):
    if raiz is None:
        return 0

    # Si el nodo no tiene hijos, es un nodo hoja
    if raiz.izquierdo is None and raiz.derecho is None:
        return 1

    # Suma los nodos hoja de los subarboles izquierdo y derecho
    return contar_nodos_hoja(raiz.izquierdo) + contar_nodos_hoja(raiz.derecho)

# Ejemplo de uso
if __name__ == "__main__":
    raiz = Nodo(1)
    raiz.izquierdo = Nodo(2)
    raiz.derecho = Nodo(3)
    raiz.izquierdo.izquierdo = Nodo(4)
    raiz.izquierdo.derecho = Nodo(5)
    raiz.derecho.izquierdo = Nodo(6)
    raiz.derecho.derecho = Nodo(7)

    print(contar_nodos_hoja(raiz))  
