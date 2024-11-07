class Stack(object):
    def __init__(self, max):  # Constructor
        self.__stackList = [None] * max  # La pila almacenada como una lista
        self.__top = -1  # Sin elementos al inicio

    def push(self, item):  # Insertar elemento en la parte superior de la pila
        if self.isFull():  # Verificar si la pila está llena antes de hacer push
            raise IndexError("No se puede hacer push: la pila está llena.")
        self.__top += 1  # Avanzar el puntero
        self.__stackList[self.__top] = item  # Almacenar el elemento

    def pop(self):  # Eliminar el elemento superior de la pila
        if self.isEmpty():  # Verificar si la pila está vacía antes de hacer pop
            raise IndexError("No se puede hacer pop: la pila está vacía.")
        top = self.__stackList[self.__top]  # Elemento superior
        self.__stackList[self.__top] = None  # Eliminar referencia al elemento
        self.__top -= 1  # Disminuir el puntero
        return top  # Devolver el elemento superior

    def peek(self):  # Obtener el elemento superior sin eliminarlo
        if not self.isEmpty():  # Si la pila no está vacía
            return self.__stackList[self.__top]  # Devolver el elemento superior
        raise IndexError("No se puede hacer peek: la pila está vacía.")

    def isEmpty(self):  # Verificar si la pila está vacía
        return self.__top < 0

    def isFull(self):  # Verificar si la pila está llena
        return self.__top >= len(self.__stackList) - 1

    def __len__(self):  # Devolver el número de elementos en la pila
        return self.__top + 1

    def __str__(self):  # Convertir la pila a cadena
        ans = "["  # Comenzar con un corchete izquierdo
        for i in range(self.__top + 1):  # Recorrer los elementos actuales
            if len(ans) > 1:  # Excepto junto al corchete izquierdo,
                ans += ", "  # separar los elementos con comas
            ans += str(self.__stackList[i])  # Agregar el elemento en forma de cadena
        ans += "]"  # Cerrar con un corchete derecho
        return ans
