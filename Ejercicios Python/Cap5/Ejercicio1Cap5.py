class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    # Generador para iterar sobre los nodos
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    # Método traverse() usando el iterador
    def traverse(self):
        for data in self:
            print(data)
    
    # Método __str__() usando el iterador
    def __str__(self):
        return ' -> '.join(str(data) for data in self)
    
    # Método __len__() usando el iterador
    def __len__(self):
        return sum(1 for _ in self)

# Ejemplo de uso
if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    ll.head.next = second
    second.next = third
    
    print("Traversing the list:")
    ll.traverse()
    
    print("\nString representation of the list:")
    print(str(ll))
    
    print("\nLength of the list:")
    print(len(ll))
