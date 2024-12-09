class ListaEnlazada:
    class Nodo:
        def __init__(self, dato):
            self.dato = dato
            self.siguiente = None

    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = self.Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None

        while actual and actual.dato != dato:
            anterior = actual
            actual = actual.siguiente

        if not actual:
            raise ValueError("El dato no se encuentra en la lista.")

        if not anterior:
            self.cabeza = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente

    def buscar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    def invertir(self):
        anterior = None
        actual = self.cabeza

        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente

        self.cabeza = anterior

def ejemplo_lista_enlazada():
    lista = ListaEnlazada()

    print("Agregando elementos: 1, 2, 3")
    lista.agregar(1)
    lista.agregar(2)
    lista.agregar(3)
    lista.mostrar()

    print("\nBuscando elementos:")
    print("¿2 esta en la lista?", lista.buscar(2))
    print("¿5 esta en la lista?", lista.buscar(5))

    print("\nEliminando el elemento 2")
    lista.eliminar(2)
    lista.mostrar()

    try:
        lista.eliminar(5)
    except ValueError as e:
        print(e)

    print("\nInvirtiendo la lista")
    lista.invertir()
    lista.mostrar()

ejemplo_lista_enlazada()
