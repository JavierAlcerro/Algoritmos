class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def insert(self, item, priority):
        #Inserta un nuevo elemento en la cola de prioridad.
        self.elements.append((item, priority))

    def remove(self):
        #Elimina y retorna el elemento de mayor prioridad.
        if self.is_empty():
            raise IndexError("La cola de prioridad está vacía.")
        # Encuentra el índice del elemento con la mayor prioridad
        highest_priority_index = 0
        for i in range(1, len(self.elements)):
            if self.elements[i][1] > self.elements[highest_priority_index][1]:
                highest_priority_index = i
        # Elimina y retorna el elemento de mayor prioridad
        return self.elements.pop(highest_priority_index)

    def peek(self):
        #Retorna el elemento de mayor prioridad sin eliminarlo.
        if self.is_empty():
            raise IndexError("La cola de prioridad está vacía.")
        highest_priority_index = 0
        for i in range(1, len(self.elements)):
            if self.elements[i][1] > self.elements[highest_priority_index][1]:
                highest_priority_index = i
        return self.elements[highest_priority_index]

    def __str__(self):
        #Devuelve una representación en forma de cadena de la cola de prioridad.
        return ', '.join(f"{item} (Prioridad: {priority})" for item, priority in self.elements)

# Programa de prueba
if __name__ == "__main__":
    pq = PriorityQueue()

    # Inserciones
    pq.insert("tarea 1", 1)
    pq.insert("tarea 2", 3)
    pq.insert("tarea 3", 2)

    # Mostrar contenido de la cola de prioridad
    print("Contenido de la cola de prioridad:")
    print(pq)

    # Ver el elemento de mayor prioridad
    print("Elemento de mayor prioridad:", pq.peek())

    # Eliminar el elemento de mayor prioridad
    print("Elemento eliminado:", pq.remove())
    print("Contenido de la cola de prioridad después de eliminar:")
    print(pq)

    # Eliminar otro elemento de mayor prioridad
    print("Elemento eliminado:", pq.remove())
    print("Contenido de la cola de prioridad después de eliminar:")
    print(pq)

    # Intentar eliminar de una cola vacía
    pq.remove()  # Esto debería funcionar sin problemas, pero luego se vaciará
    try:
        print("Intentando eliminar de la cola de prioridad vacía...")
        pq.remove()
    except IndexError as e:
        print(e)
