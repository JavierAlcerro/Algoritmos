def bubbleSortBidireccional(self):  
    izquierda = 0
    derecha = self.__nItems - 1

    while izquierda < derecha:
        #mover el elemento mas grande hacia la derecha
        for inner in range(izquierda, derecha):
            if self.__a[inner] > self.__a[inner + 1]:
                self.swap(inner, inner + 1)
        derecha -= 1  

        #mover el elemento mas pequeño hacia la izquierda
        for inner in range(derecha, izquierda, -1):
            if self.__a[inner] < self.__a[inner - 1]:
                self.swap(inner, inner - 1)
        izquierda += 1 
