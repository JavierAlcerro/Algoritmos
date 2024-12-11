class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def altura_arbol(nodo):
    if nodo is None:
        return -1  
    else:
        altura_izquierda = altura_arbol(nodo.izquierda)
        altura_derecha = altura_arbol(nodo.derecha)
        return 1 + max(altura_izquierda, altura_derecha)

raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)

print("La altura del árbol es:", altura_arbol(raiz))
