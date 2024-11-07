import random

class Cola:
    def __init__(self):
        self.cola = []

    def encolar(self, numero):
        self.cola.append(numero)

    def desencolar(self):
        if self.cola:
            return self.cola.pop(0)
        else:
            return None

    def generar_numeros(self):
        for _ in range(100):
            self.encolar(random.randint(1, 100))

    def calcular_pares_impares(self):
        pares = [num for num in self.cola if num % 2 == 0]
        impares = [num for num in self.cola if num % 2 != 0]

        promedio_pares = sum(pares) / len(pares) if pares else 0
        promedio_impares = sum(impares) / len(impares) if impares else 0

        return len(pares), len(impares), promedio_pares, promedio_impares

    def mostrar_cola(self):
        while self.cola:
            print(self.desencolar())
