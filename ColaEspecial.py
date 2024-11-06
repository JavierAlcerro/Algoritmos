class ColaEspecial:
    def _init_(self, size=10):
        self.size = size
        self.queue = [None] * self.size
        self.direction = 1  
    
    def esta_llena(self):
        return all(self.queue)
    
    def insertar(self, elemento):
        if not self.esta_llena():
            for i in range(self.size):
                if self.queue[i] is None:
                    self.queue[i] = elemento
                    return
        else:
            self.proceso_especial(elemento)
    
    def proceso_especial(self, elemento):
        if self.direction == 1:  
            for i in range(self.size - 1, 0, -1):
                self.queue[i] = self.queue[i - 1]
            self.queue[0] = elemento
        else: 
            for i in range(self.size - 1):
                self.queue[i] = self.queue[i + 1]
            self.queue[self.size - 1] = elemento
        
        self.direction *= -1
    
    def imprimir_cola(self):
        print("Estado de la cola:", self.queue)