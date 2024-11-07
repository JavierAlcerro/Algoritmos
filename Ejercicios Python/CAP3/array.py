class Array(object):
    def __init__(self, initialSize):  # Constructor
        self.__a = [None] * initialSize  # The array stored as a list
        self.__nItems = 0  # No items in array initially

    def __len__(self):  # Special def for len() func
        return self.__nItems  # Return number of items

    def get(self, n):  # Return the value at index n
        if 0 <= n < self.__nItems:  # Check if n is in bounds
            return self.__a[n]  # Only return item if in bounds

    def set(self, n, value):  # Set the value at index n
        if 0 <= n < self.__nItems:  # Check if n is in bounds
            self.__a[n] = value  # Only set item if in bounds

    def swap(self, j, k):  # Swap the values at 2 indices
        if (0 <= j < self.__nItems) and (0 <= k < self.__nItems):  # Check if indices are in bounds
            self.__a[j], self.__a[k] = self.__a[k], self.__a[j]

    def insert(self, item):  # Insert item at end
        if self.__nItems >= len(self.__a):  # If array is full
            raise Exception("Array overflow")  # Raise exception
        self.__a[self.__nItems] = item  # Item goes at current end
        self.__nItems += 1  # Increment number of items

    def find(self, item):  # Find index for item
        for j in range(self.__nItems):  # Among current items
            if self.__a[j] == item:  # If found
                return j  # Return index of element
        return -1  # Not found -> return -1

    def search(self, item):  # Search for item
        index = self.find(item)  # Find item index
        if index != -1:
            return self.get(index)  # Return item if found
        return None  # Return None if not found

    def delete(self, item):  # Delete first occurrence
        for j in range(self.__nItems):  # Search for the item
            if self.__a[j] == item:  # Found item
                self.__nItems -= 1  # One fewer at end
                for k in range(j, self.__nItems):  # Move items from right over 1
                    self.__a[k] = self.__a[k+1]
                return True  # Return success flag
        return False  # Couldn't find the item

    def traverse(self, function=print):  # Traverse all items and apply a function
        for j in range(self.__nItems):
            function(self.__a[j])

    def __str__(self):  # Special def for str() func
        ans = "["  # Surround with square brackets
        for i in range(self.__nItems):  # Loop through items
            if len(ans) > 1:  # Except next to left bracket
                ans += ", "  # Separate items with comma
            ans += str(self.__a[i])  # Add string form of item
        ans += "]"  # Close with right bracket
        return ans

    def bubbleSort(self):  # Sort by comparing adjacent values
        for last in range(self.__nItems-1, 0, -1):  # Bubble up
            for inner in range(last):  # Inner loop goes up to last
                if self.__a[inner] > self.__a[inner+1]:  # If element is less than adjacent
                    self.swap(inner, inner+1)  # Swap values

    def selectionSort(self):  # Sort by selecting min and swapping min to leftmost
        for outer in range(self.__nItems-1):
            min_index = outer  # Assume min is leftmost
            for inner in range(outer+1, self.__nItems):  # Hunt to right
                if self.__a[inner] < self.__a[min_index]:  # If we find new min
                    min_index = inner  # Update the min index
            self.swap(outer, min_index)  # Swap leftmost and min

    def insertionSort(self):  # Sort by repeated inserts
        for outer in range(1, self.__nItems):  # Mark one element
            temp = self.__a[outer]  # Store marked element in temp
            inner = outer  # Inner loop starts at mark
            while inner > 0 and temp < self.__a[inner-1]:  # If marked element is smaller
                self.__a[inner] = self.__a[inner-1]  # Shift element to the right
                inner -= 1
            self.__a[inner] = temp  # Move marked element to 'hole'

    def median(self):
        if self.__nItems == 0:
            raise Exception("El arreglo está vacío")  # Manejo de caso vacio

        # Ordenamos el arreglo
        self.bubbleSort()  

        #  indice medio
        mid = self.__nItems // 2

        # Si el numero de elementos es impar, devolvemos el elemento central
        if self.__nItems % 2 == 1:
            return self.__a[mid]
        # Si es par, devolvemos el promedio de los dos elementos centrales
        else:
            return (self.__a[mid - 1] + self.__a[mid]) / 2


