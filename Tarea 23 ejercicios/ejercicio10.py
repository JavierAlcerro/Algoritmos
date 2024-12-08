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

class HistorialNavegacion:
    def __init__(self):
        self.historial = Pila()
        self.pila_atras = Pila()

    def visitar(self, url):
        """Agrega una nueva URL al historial y limpia la pila de 'atras'."""
        self.historial.push(url)
        self.pila_atras = Pila()  
        print(f"Visitando: {url}")

    def ir_atras(self):
        """Va hacia atras en el historial si es posible."""
        if self.historial.esta_vacia():
            print("No hay historial para ir hacia atras.")
            return
        url_actual = self.historial.pop()
        self.pila_atras.push(url_actual)
        if self.historial.esta_vacia():
            print("No hay mas paginas en el historial.")
            return
        url_previa = self.historial.peek()
        print(f"Regresando a: {url_previa}")

    def mostrar_historial(self):
        """Muestra el historial actual."""
        if self.historial.esta_vacia():
            print("El historial esta vacio.")
        else:
            print("Historial de navegacion:")
            for url in reversed(self.historial.elementos):
                print(f"- {url}")

def menu():
    navegador = HistorialNavegacion()

    urls_disponibles = [
        "https://google.com",
        "https://youtube.com",
        "https://wikipedia.org",
        "https://facebook.com",
        "https://twitter.com"
    ]

    while True:
        print("\n=== Menu ===")
        print("1. Visitar una pagina predeterminada")
        print("2. Ir hacia atras")
        print("3. Mostrar historial")
        print("4. Salir")
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            print("Paginas disponibles para visitar:")
            for i, url in enumerate(urls_disponibles, start=1):
                print(f"{i}. {url}")
            try:
                eleccion = int(input("Elige una opcion para visitar (1-5): "))
                if 1 <= eleccion <= len(urls_disponibles):
                    navegador.visitar(urls_disponibles[eleccion - 1])
                else:
                    print("Opcion no valida. Intentalo de nuevo.")
            except ValueError:
                print("Por favor, ingresa un numero valido.")
        elif opcion == "2":
            navegador.ir_atras()
        elif opcion == "3":
            navegador.mostrar_historial()
        elif opcion == "4":
            print("Saliendo del navegador...")
            break
        else:
            print("Opcion no valida. Intentalo de nuevo.")

menu()
