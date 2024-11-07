import string

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def is_palindrome(input_string):
    # Crear una pila
    stack = Stack()

    # Preprocesar la cadena: eliminar espacios, puntuación y convertir a minúsculas
    filtered_string = ''.join(
        char.lower() for char in input_string 
        if char.isalpha()
    )

    # Llenar la pila con la cadena filtrada
    for char in filtered_string:
        stack.push(char)

    # Comparar la cadena original filtrada con la cadena invertida usando la pila
    reversed_string = ''
    while not stack.is_empty():
        reversed_string += stack.pop()

    return filtered_string == reversed_string

def main():
    input_string = "Un hombre, un plan, un canal, Panamá"
    if is_palindrome(input_string):
        print(f'"{input_string}" es un palíndromo.')
    else:
        print(f'"{input_string}" no es un palíndromo.')

if __name__ == "__main__":
    main()
