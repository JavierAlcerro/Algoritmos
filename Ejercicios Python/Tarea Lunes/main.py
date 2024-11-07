from pila import Pila
from cola import Cola

def main():
    print("Elige una opción:")
    print("1. Ejecutar como Pila (LIFO)")
    print("2. Ejecutar como Cola (FIFO)")
    
    opcion = input("Introduce el número de la opción: ")

    if opcion == '1':
        estructura = Pila()
        estructura.generar_numeros()
        pares, impares, prom_pares, prom_impares = estructura.calcular_pares_impares()

        print(f"Numeros pares: {pares}")
        print(f"Numeros impares: {impares}")
        print(f"Promedio de numeros pares: {prom_pares}")
        print(f"Promedio de numeros impares: {prom_impares}")

        print("\nMostrando la pila (último en entrar, primero en salir):")
        estructura.mostrar_pila()

    elif opcion == '2':
        estructura = Cola()
        estructura.generar_numeros()
        pares, impares, prom_pares, prom_impares = estructura.calcular_pares_impares()

        print(f"Numeros pares: {pares}")
        print(f"Numeros impares: {impares}")
        print(f"Promedio de numeros pares: {prom_pares}")
        print(f"Promedio de numeros impares: {prom_impares}")

        print("\nMostrando la cola (primero en entrar, primero en salir):")
        estructura.mostrar_cola()

    else:
        print("Opción no valida.")

if __name__ == "__main__":
    main()
