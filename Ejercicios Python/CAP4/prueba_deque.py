from Deque import Deque

def test_deque():
    deque = Deque(5)  # Crear un deque de tamaño máximo 5

    print("Insertando elementos...")
    deque.insertRight(1)
    deque.insertRight(2)
    deque.insertLeft(0)
    print(deque)  # Debería mostrar [0, 1, 2]

    print("Elemento al frente:", deque.peekLeft())  # Debería mostrar 0
    print("Elemento al final:", deque.peekRight())  # Debería mostrar 2

    print("Eliminando elementos...")
    print("Elemento eliminado:", deque.removeLeft())  # Debería mostrar 0
    print(deque)  # Debería mostrar [1, 2]

    print("Elemento eliminado:", deque.removeRight())  # Debería mostrar 2
    print(deque)  # Debería mostrar [1]

    deque.insertRight(3)
    deque.insertRight(4)
    deque.insertRight(5)
    print(deque)  # Debería mostrar [1, 3, 4, 5]

    try:
        deque.insertRight(6)  # Debería lanzar una excepción
    except IndexError as e:
        print("Excepción capturada:", e)

test_deque()
