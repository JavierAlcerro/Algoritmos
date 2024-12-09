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

    def combinar_listas(self, otra_lista):
        dummy = Nodo(0)
        actual = dummy
        l1 = self.cabeza
        l2 = otra_lista.cabeza

        while l1 and l2:
            if l1.valor < l2.valor:
                actual.siguiente = l1
                l1 = l1.siguiente
            else:
                actual.siguiente = l2
                l2 = l2.siguiente
            actual = actual.siguiente

        if l1:
            actual.siguiente = l1
        if l2:
            actual.siguiente = l2

        nueva_lista = ListaEnlazada()
        nueva_lista.cabeza = dummy.siguiente
        return nueva_lista

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

lista1 = ListaEnlazada()
lista1.agregar(1)
lista1.agregar(3)
lista1.agregar(5)

lista2 = ListaEnlazada()
lista2.agregar(2)
lista2.agregar(4)
lista2.agregar(6)

print("Lista 1:")
lista1.imprimir()
print("Lista 2:")
lista2.imprimir()

lista_combinada = lista1.combinar_listas(lista2)
print("Lista combinada:")
lista_combinada.imprimir()
