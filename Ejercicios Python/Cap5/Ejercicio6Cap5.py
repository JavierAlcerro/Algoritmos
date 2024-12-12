from collections import *

class Queue:
    def __init__(self):
        self.items = deque()
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def insert(self, data):
        self.items.append(data)
    
    def remove(self):
        if self.isEmpty():
            raise IndexError("remove from empty queue")
        return self.items.popleft()
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("peek from empty queue")
        return self.items[0]
    
    def __str__(self):
        return " -> ".join(map(str, self.items))
    
    def __iter__(self):
        return iter(self.items)
    
class PriorityQueue:
    def __init__(self):
        # Diccionario de colas, donde cada clave es una prioridad
        self.queues = {}
    
    def insert(self, priority, data):
        # Si no existe una cola para esa prioridad, la creamos
        if priority not in self.queues:
            self.queues[priority] = Queue()
        self.queues[priority].insert(data)
    
    def remove(self, priority=None):
        # Si no se especifica prioridad, buscamos la cola de mayor prioridad
        if priority is None:
            # Buscar la prioridad más alta que tenga al menos un elemento
            sorted_priorities = sorted(self.queues.keys(), reverse=True)
            for p in sorted_priorities:
                if not self.queues[p].isEmpty():
                    priority = p
                    break
            else:
                raise IndexError("remove from empty priority queue")
        
        # Si la cola de la prioridad especificada está vacía, lanzamos un error
        if self.queues[priority].isEmpty():
            raise IndexError(f"remove from empty priority queue with priority {priority}")
        
        # Eliminar el primer elemento de la cola de la prioridad seleccionada
        return self.queues[priority].remove()
    
    def priorities(self):
        # Iterador para recorrer las prioridades con al menos un elemento
        for priority in sorted(self.queues.keys(), reverse=True):
            if not self.queues[priority].isEmpty():
                yield priority
    
    def __len__(self):
        # Devuelve el número total de elementos en todas las colas de prioridad
        return sum(len(q) for q in self.queues.values())
    
    def __str__(self):
        # Representación de la cola prioritaria con todas sus colas de prioridad
        result = []
        for priority in sorted(self.queues.keys(), reverse=True):
            result.append(f"Priority {priority}: {self.queues[priority]}")
        return "\n".join(result)
    
    def __iter__(self):
        # Iterador completo que recorre todos los elementos de todas las colas de prioridad
        for priority in sorted(self.queues.keys(), reverse=True):
            for item in self.queues[priority]:
                yield item


# Ejemplo de uso
if __name__ == "__main__":
    pq = PriorityQueue()
    
    # Insertar elementos con diferentes prioridades
    pq.insert(2, "A")
    pq.insert(1, "B")
    pq.insert(3, "C")
    pq.insert(2, "D")
    pq.insert(1, "E")
    pq.insert(3, "F")
    
    print("Cola prioritaria:")
    print(pq)
    
    # Ver el número total de elementos
    print("\nTotal de elementos:", len(pq))  # 6
    
    # Eliminar elementos de la cola prioritaria
    print("\nEliminando elementos:")
    print("Removed:", pq.remove())  # C (prioridad 3)
    print("Removed:", pq.remove())  # F (prioridad 3)
    print("Removed:", pq.remove())  # A (prioridad 2)
    print("Removed:", pq.remove())  # D (prioridad 2)
    
    print("\nCola prioritaria después de eliminar elementos:")
    print(pq)
    
    # Insertar un elemento con nueva prioridad
    pq.insert(2, "G")
    pq.insert(3, "H")
    
    print("\nCola prioritaria después de insertar elementos con nuevas prioridades:")
    print(pq)
    
    # Verificar prioridades
    print("\nPrioridades existentes:")
    for priority in pq.priorities():
        print(f"Priority {priority}")
    
    # Iterar sobre todos los elementos
    print("\nIterando sobre todos los elementos:")
    for item in pq:
        print(item)
    
    # Eliminar el último elemento
    print("\nEliminando el último elemento (prioridad 1):")
    print(pq.remove())  # B (prioridad 1)
