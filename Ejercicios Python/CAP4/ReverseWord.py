# Un programa para determinar si una cadena es un palíndromo
from SimpleStack import Stack  # Importar la clase Stack desde simple_stack.py
import string

def is_palindrome(text):
    # Crear una pila para almacenar las letras
    stack = Stack(len(text))
    
    # Filtrar solo las letras y convertir a minúsculas
    filtered_text = ''.join([char.lower() for char in text if char.isalpha()])
    
    # Insertar las letras en la pila
    for letter in filtered_text:
        stack.push(letter)
    
    # Reconstruir el texto al revés usando la pila
    reversed_text = ''
    while not stack.isEmpty():
        reversed_text += stack.pop()
    
    # Comparar el texto filtrado con su versión invertida
    return filtered_text == reversed_text

# Probar el programa con la frase dada
text = "A man, a plan, a canal, Panama."
if is_palindrome(text):
    print(f'"{text}" es un palíndromo.')
else:
    print(f'"{text}" no es un palíndromo.')
