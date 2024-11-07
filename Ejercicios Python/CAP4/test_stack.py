from SimpleStack import Stack

def test_stack():
    max_size = 3
    stack = Stack(max_size)

    print("Probando inserción en la pila (Push)")
    for i in range(max_size):
        print(f"Haciendo push de {i+1}")
        stack.push(i + 1)
        print(stack)

    try:
        print("Intentando hacer push en una pila llena")
        stack.push(4)  # Esto debería lanzar una excepción
    except IndexError as e:
        print("Excepción capturada:", e)

    print("\nProbando eliminación de la pila (Pop)")
    for i in range(max_size):
        print("Haciendo pop:", stack.pop())
        print(stack)

    try:
        print("Intentando hacer pop de una pila vacía")
        stack.pop()  # Esto debería lanzar una excepción
    except IndexError as e:
        print("Excepción capturada:", e)

test_stack()
