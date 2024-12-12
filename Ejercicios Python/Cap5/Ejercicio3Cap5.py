class Node:
    def __init__(self, data=None):
        self.data = data  # Almacena el dato del nodo
        self.prev = None  # Apunta al nodo anterior
        self.next = None  # Apunta al nodo siguiente

class Deque:
    def __init__(self):
        self.head = None  # El primer nodo (izquierda)
        self.tail = None  # El último nodo (derecha)
        self.size = 0  # Contador de elementos en la deque
    
    # Verifica si la deque está vacía
    def isEmpty(self):
        return self.size == 0
    
    # Inserta un elemento en el extremo izquierdo (inicio)
    def insertLeft(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = self.tail = new_node  # Si está vacía, el nuevo nodo es tanto la cabeza como la cola
        else:
            new_node.next = self.head  # El siguiente del nuevo nodo será la cabeza actual
            self.head.prev = new_node  # El anterior de la cabeza será el nuevo nodo
            self.head = new_node  # El nuevo nodo es ahora la cabeza
        self.size += 1
    
    # Inserta un elemento en el extremo derecho (final)
    def insertRight(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = self.tail = new_node  # Si está vacía, el nuevo nodo es tanto la cabeza como la cola
        else:
            new_node.prev = self.tail  # El anterior del nuevo nodo será la cola actual
            self.tail.next = new_node  # El siguiente de la cola será el nuevo nodo
            self.tail = new_node  # El nuevo nodo es ahora la cola
        self.size += 1
    
    # Elimina un elemento desde el extremo izquierdo (inicio)
    def removeLeft(self):
        if self.isEmpty():
            raise IndexError("removeLeft from empty deque")
        removed_data = self.head.data  # Obtenemos el dato a eliminar
        if self.head == self.tail:
            self.head = self.tail = None  # Si hay un solo nodo, la deque se vacía
        else:
            self.head = self.head.next  # La nueva cabeza es el siguiente nodo
            self.head.prev = None  # La cabeza ahora no tiene un nodo anterior
        self.size -= 1
        return removed_data
    
    # Elimina un elemento desde el extremo derecho (final)
    def removeRight(self):
        if self.isEmpty():
            raise IndexError("removeRight from empty deque")
        removed_data = self.tail.data  # Obtenemos el dato a eliminar
        if self.head == self.tail:
            self.head = self.tail = None  # Si hay un solo nodo, la deque se vacía
        else:
            self.tail = self.tail.prev  # La nueva cola es el nodo anterior
            self.tail.next = None  # La cola ahora no tiene un nodo siguiente
        self.size -= 1
        return removed_data
    
    # Devuelve el primer elemento sin eliminarlo (extremo izquierdo)
    def peekLeft(self):
        if self.isEmpty():
            raise IndexError("peekLeft from empty deque")
        return self.head.data
    
    # Devuelve el último elemento sin eliminarlo (extremo derecho)
    def peekRight(self):
        if self.isEmpty():
            raise IndexError("peekRight from empty deque")
        return self.tail.data
    
    # Devuelve el tamaño de la deque
    def __len__(self):
        return self.size
    
    # Método para representar la deque como una cadena
    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " <-> ".join(elements)

# Ejemplo de uso
if __name__ == "__main__":
    deque = Deque()
    
    # Insertar en ambos extremos
    deque.insertLeft(10)
    deque.insertRight(20)
    deque.insertLeft(5)
    deque.insertRight(25)
    
    print("Deque después de inserciones:", deque)
    print("Tamaño de la deque:", len(deque))
    
    # Consultar los elementos extremos
    print("Peek Left:", deque.peekLeft())  # 5
    print("Peek Right:", deque.peekRight())  # 25
    
    # Eliminar desde ambos extremos
    print("Remove Left:", deque.removeLeft())  # 5
    print("Remove Right:", deque.removeRight())  # 25
    
    print("Deque después de eliminaciones:", deque)
    print("Tamaño de la deque:", len(deque))
    
    # Verificar si la deque está vacía
    print("Está vacía?", deque.isEmpty())  # False
