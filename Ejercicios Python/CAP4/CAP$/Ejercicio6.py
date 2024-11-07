class QueueFullException(Exception):
    #Excepción para indicar que la cola está llena.
    pass

class QueueEmptyException(Exception):
    #Excepción para indicar que la cola está vacía.
    pass

class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) >= self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise QueueFullException("La cola está llena.")
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise QueueEmptyException("La cola está vacía.")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise QueueEmptyException("La cola está vacía.")
        return self.items[0]

    def __str__(self):
        return ', '.join(self.items)

class StoreQueueSimulation:
    def __init__(self):
        self.queues = {
            'A': Queue(5),
            'B': Queue(5),
            'C': Queue(5),
            'D': Queue(5)
        }
        self.customer_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

    def process_event(self, event):
        if event.islower():  # Nueva llegada
            queue_label = event.upper()
            if queue_label in self.queues:
                customer_id = f"{queue_label}{self.customer_count[queue_label] + 1}"
                self.customer_count[queue_label] += 1
                try:
                    self.queues[queue_label].enqueue(customer_id)
                    print(f"Cliente {customer_id} agregado a la cola {queue_label}.")
                except QueueFullException as e:
                    print(f"Error: {e}")
        elif event.isupper():  # Finalización de pago
            queue_label = event
            if queue_label in self.queues:
                try:
                    finished_customer = self.queues[queue_label].dequeue()
                    print(f"Cliente {finished_customer} ha completado el pago en la cola {queue_label}.")
                except QueueEmptyException as e:
                    print(f"Error: {e}")
        else:  # Cualquier carácter no alfabético
            self.print_queues()

    def print_queues(self):
        print("\nEstado actual de las colas:")
        for label, queue in self.queues.items():
            print(f"Cola {label}: {queue}")

def main():
    simulation = StoreQueueSimulation()
    events = "aababbAbA"  # Puedes cambiar esto por cualquier otra cadena de eventos

    for event in events:
        simulation.process_event(event)

    # Mostrar estado final de las colas
    simulation.print_queues()

if __name__ == "__main__":
    main()
