def swap(a, b):
    return b, a


class MinHeap:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__size = 0
        self.__heap_arr = [None] * capacity

    def get_size(self):
        return self.__size

    def get_left_child(self, i):
        if i < self.__size and i * 2 + 1 < self.__size:
            return i * 2 + 1
        return None

    def get_right_child(self, i):
        if i < self.__size and i * 2 + 2 < self.__size:
            return i * 2 + 2
        return None

    def get_parent(self, i):
        if i <= 0 or i >= self.__size:
            return None
        return (i - 1) // 2

    def insert(self, data):
        if self.__size == self.__capacity:
            return None
        self.__size += 1
        self.__heap_arr[self.__size - 1] = data
        parent = self.get_parent(self.__size - 1)
        current = self.__size - 1
        while parent is not None and self.__heap_arr[parent] > self.__heap_arr[current]:
            self.__heap_arr[parent], self.__heap_arr[current] = self.__heap_arr[current], self.__heap_arr[parent]
            current = parent
            parent = self.get_parent(current)

    def get_min(self):
        if self.__size > 0:
            return self.__heap_arr[0]

    def heapify(self, s):
        smallest = s

        if self.get_left_child(s) is not None and self.__heap_arr[self.get_left_child(s)] < self.__heap_arr[smallest]:
            smallest = self.get_left_child(s)
        if self.get_right_child(s) is not None and self.__heap_arr[self.get_right_child(s)] < self.__heap_arr[smallest]:
            smallest = self.get_right_child(s)

        if smallest != s:
            self.__heap_arr[smallest], self.__heap_arr[s] = self.__heap_arr[s], self.__heap_arr[smallest]
            self.heapify(smallest)

    def extract_min(self):
        if self.__size <= 0:
            return None
        if self.__size == 1:
            self.__size -= 1
            return self.__heap_arr[self.__size]
        self.__size -= 1
        self.__heap_arr[0], self.__heap_arr[self.__size] = self.__heap_arr[self.__size], self.__heap_arr[0]
        self.heapify(0)
        return self.__heap_arr[self.__size]

    def decrease_key(self, i, data):
        self.__heap_arr[i] = data
        current = i
        parent = self.get_parent(i)
        while parent is not None and self.__heap_arr[parent] > self.__heap_arr[current]:
            self.__heap_arr[current], self.__heap_arr[parent] = self.__heap_arr[parent], self.__heap_arr[current]
            current = parent
            parent = self.get_parent(current)

    def delete_at(self, i):
        self.decrease_key(i, -1)
        return True if self.extract_min() is not None else False

    def __str__(self):
        output = ''
        for i in range(self.__size):
            output += str(self.__heap_arr[i]) + " "
        output += "\n"
        return output


if __name__ == '__main__':
    min_heap = MinHeap(10)
    min_heap.insert(5)
    min_heap.insert(4)
    min_heap.insert(3)
    # min_heap.insert(6)
    # min_heap.insert(7)
    # min_heap.insert(2)
    # min_heap.insert(1)

    print(min_heap.extract_min())
    print(min_heap)
    min_heap.delete_at(0)
    print(min_heap)


