class Node:
    def __init__(self, data=None):
        self.data = data  # Almacena el dato del nodo
        self.next = None  # Apunta al siguiente nodo en la lista

class CircularLinkedList:
    def __init__(self):
        self._last = None  # La referencia al último nodo, que puede apuntar a cualquier nodo de la lista
        self.size = 0  # Número de nodos en la lista
    
    # Verifica si la lista está vacía
    def isEmpty(self):
        return self._last is None
    
    # Inspecciona el primer elemento (el siguiente del último nodo)
    def peekFirst(self):
        if self.isEmpty():
            raise IndexError("peekFirst from empty list")
        return self._last.next.data
    
    # Inserta un nuevo nodo al principio de la lista
    def insertFirst(self, data):
        new_node = Node(data)
        if self.isEmpty():
            new_node.next = new_node  # El nodo apunta a sí mismo, ya que es la única entrada
            self._last = new_node  # Si la lista está vacía, el nuevo nodo es el único y último
        else:
            new_node.next = self._last.next  # El nuevo nodo apunta al antiguo primer nodo
            self._last.next = new_node  # El último nodo apunta al nuevo nodo
        self.size += 1
    
    # Inserta un nuevo nodo al final de la lista
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
    
    # Elimina el primer nodo de la lista
    def deleteFirst(self):
        if self.isEmpty():
            raise IndexError("deleteFirst from empty list")
        if self._last.next == self._last:  # Solo hay un nodo
            self._last = None
        else:
            self._last.next = self._last.next.next  # El segundo nodo se convierte en el primero
        self.size -= 1
    
    # Busca un nodo por su valor
    def search(self, key):
        if self.isEmpty():
            return None
        current = self._last.next  # Comienza desde el primer nodo
        while True:
            if current.data == key:
                return current  # Retorna el nodo si encuentra el valor
            current = current.next
            if current == self._last.next:  # Hemos dado una vuelta completa a la lista
                break
        return None
    
    # Mueve la referencia _last al siguiente nodo
    def step(self):
        if self.isEmpty():
            raise IndexError("step on empty list")
        self._last = self._last.next  # Mueve la referencia al siguiente nodo
    
    # Mueve la referencia _last al siguiente nodo que contenga el valor "key"
    def seek(self, key):
        if self.isEmpty():
            raise IndexError("seek on empty list")
        current = self._last.next  # Comienza desde el primer nodo
        while True:
            if current.data == key:
                self._last = current  # Establece _last en el nodo encontrado
                return
            current = current.next
            if current == self._last.next:  # Hemos dado una vuelta completa a la lista
                break
        raise ValueError(f"Value {key} not found in the list")
    
    # Representación en cadena de la lista
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

# Ejemplo de uso
if __name__ == "__main__":
    cll = CircularLinkedList()
    
    # Inserciones
    cll.insertFirst(10)
    cll.insertLast(20)
    cll.insertFirst(5)
    cll.insertLast(30)
    
    # Mostrar la lista
    print("Lista circular:", cll)  # 5 -> 10 -> 20 -> 30
    
    # Buscar un elemento
    node = cll.search(20)
    if node:
        print("Elemento encontrado:", node.data)
    else:
        print("Elemento no encontrado")
    
    # Avanzar el puntero _last
    cll.step()
    print("Después de step(), lista circular:", cll)  # 10 -> 20 -> 30 -> 5
    
    # Mover _last hasta el nodo con valor 30
    cll.seek(30)
    print("Después de seek(30), lista circular:", cll)  # 30 -> 5 -> 10 -> 20
    
    # Eliminar el primer elemento
    cll.deleteFirst()
    print("Después de deleteFirst(), lista circular:", cll)  # 5 -> 10 -> 20
    
    # Inspeccionar el primer elemento
    print("Primer elemento:", cll.peekFirst())  # 5
    
    # Verificar si la lista está vacía
    print("¿Está vacía?", cll.isEmpty())  # False
