class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar_duplicados(self):
        valores_vistos = set()
        actual = self.cabeza
        previo = None

        while actual:
            if actual.valor in valores_vistos:
                previo.siguiente = actual.siguiente
            else:
                valores_vistos.add(actual.valor)
                previo = actual
            actual = actual.siguiente

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(2)
lista.agregar(3)
lista.agregar(1)

print("Lista antes de eliminar duplicados:")
lista.imprimir()

lista.eliminar_duplicados()

print("Lista despues de eliminar duplicados:")
lista.imprimir()
