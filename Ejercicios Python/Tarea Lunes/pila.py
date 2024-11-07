import random

class Pila:
    def __init__(self):
        self.pila = []

    def apilar(self, numero):
        self.pila.append(numero)

    def desapilar(self):
        if self.pila:
            return self.pila.pop()
        else:
            return None

    def generar_numeros(self):
        for _ in range(100):
            self.apilar(random.randint(1, 100))

    def calcular_pares_impares(self):
        pares = [num for num in self.pila if num % 2 == 0]
        impares = [num for num in self.pila if num % 2 != 0]

        promedio_pares = sum(pares) / len(pares) if pares else 0
        promedio_impares = sum(impares) / len(impares) if impares else 0

        return len(pares), len(impares), promedio_pares, promedio_impares

    def mostrar_pila(self):
        while self.pila:
            print(self.desapilar())
