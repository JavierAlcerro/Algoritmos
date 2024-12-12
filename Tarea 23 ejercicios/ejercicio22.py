class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def recorrido_por_niveles(raiz):
    if raiz is None:
        return []

    cola = []
    resultado = []

    cola.append(raiz)

    while cola:
        nodo_actual = cola.pop(0)
        resultado.append(nodo_actual.valor)

        if nodo_actual.izquierdo:
            cola.append(nodo_actual.izquierdo)
        if nodo_actual.derecho:
            cola.append(nodo_actual.derecho)

    return resultado

if __name__ == "__main__":
    raiz = Nodo(1)
    raiz.izquierdo = Nodo(2)
    raiz.derecho = Nodo(3)
    raiz.izquierdo.izquierdo = Nodo(4)
    raiz.izquierdo.derecho = Nodo(5)
    raiz.derecho.izquierdo = Nodo(6)
    raiz.derecho.derecho = Nodo(7)

    print(recorrido_por_niveles(raiz))  
