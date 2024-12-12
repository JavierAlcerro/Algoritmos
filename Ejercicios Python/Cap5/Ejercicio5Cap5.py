class Node:
    def __init__(self, data=None):
        self.data = data  # Almacena el dato del nodo
        self.next = None  # Apunta al siguiente nodo en la lista

class CircularLinkedList:
    def __init__(self):
        self._last = None  # La referencia al último nodo, que puede apuntar a cualquier nodo de la lista
        self.size = 0  # Número de nodos en la lista
    
    def isEmpty(self):
        return self._last is None
    
    def insertFirst(self, data):
        new_node = Node(data)
        if self.isEmpty():
            new_node.next = new_node  # El nodo apunta a sí mismo, ya que es la única entrada
            self._last = new_node  # Si la lista está vacía, el nuevo nodo es el único y último
        else:
            new_node.next = self._last.next  # El nuevo nodo apunta al antiguo primer nodo
            self._last.next = new_node  # El último nodo apunta al nuevo nodo
        self.size += 1
    
    def insertLast(self, data):
        new_node = Node(data)
        if self.isEmpty():
            new_node.next = new_node  # El nodo apunta a sí mismo, es el único nodo
            self._last = new_node
        else:
            new_node.next = self._last.next  # El nuevo nodo apunta al primer nodo
            self._last.next = new_node  # El último nodo apunta al nuevo nodo
            self._last = new_node  # El nuevo nodo se convierte en el último
        self.size += 1
    
    def deleteFirst(self):
        if self.isEmpty():
            raise IndexError("deleteFirst from empty list")
        if self._last.next == self._last:  # Solo hay un nodo
            self._last = None
        else:
            self._last.next = self._last.next.next  # El segundo nodo se convierte en el primero
        self.size -= 1
    
    def peekFirst(self):
        if self.isEmpty():
            raise IndexError("peekFirst from empty list")
        return self._last.next.data
    
    def __str__(self):
        if self.isEmpty():
            return "[]"
        elements = []
        current = self._last.next
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self._last.next:  # Hemos dado una vuelta completa
                break
        return " -> ".join(elements)


# Clase Stack (Pila) basada en la lista circular
class Stack:
    def __init__(self):
        self.circular_list = CircularLinkedList()
    
    def isEmpty(self):
        return self.circular_list.isEmpty()
    
    def push(self, data):
        self.circular_list.insertFirst(data)
    
    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        data = self.circular_list.peekFirst()  # Guardamos el dato a retornar
        self.circular_list.deleteFirst()  # Eliminamos el primer nodo
        return data
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("peek from empty stack")
        return self.circular_list.peekFirst()
    
    def __str__(self):
        return str(self.circular_list)


# Clase Queue (Cola) basada en la lista circular
class Queue:
    def __init__(self):
        self.circular_list = CircularLinkedList()
    
    def isEmpty(self):
        return self.circular_list.isEmpty()
    
    def insert(self, data):
        self.circular_list.insertLast(data)
    
    def remove(self):
        if self.isEmpty():
            raise IndexError("remove from empty queue")
        data = self.circular_list.peekFirst()  # Guardamos el dato a retornar
        self.circular_list.deleteFirst()  # Eliminamos el primer nodo
        return data
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("peek from empty queue")
        return self.circular_list.peekFirst()
    
    def __str__(self):
        return str(self.circular_list)


# Ejemplo de uso
if __name__ == "__main__":
    # Prueba de la pila
    print("Probando la pila (Stack):")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Pila actual:", stack)  # 30 -> 20 -> 10
    print("Peek (último elemento):", stack.peek())  # 30
    print("Pop (eliminando):", stack.pop())  # 30
    print("Pila después de pop:", stack)  # 20 -> 10

    # Prueba de la cola
    print("\nProbando la cola (Queue):")
    queue = Queue()
    queue.insert(10)
    queue.insert(20)
    queue.insert(30)
    print("Cola actual:", queue)  # 10 -> 20 -> 30
    print("Peek (primer elemento):", queue.peek())  # 10
    print("Remove (eliminando):", queue.remove())  # 10
    print("Cola después de remove:", queue)  # 20 -> 30
