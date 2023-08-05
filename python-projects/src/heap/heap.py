class MinHeap:
    def __init__(self, size: int):
        self.heap = [-1]*size
        self.size = 0

    def __heap_down(self, node: int = 0):
        if node >= len(self.heap):
            return
        left_child = node * 2 + 1
        right_child = node * 2 + 2
        largest = node
        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child
        if largest != node:
            self.heap[largest], self.heap[node] = self.heap[node], self.heap[largest]
            self.__heap_down(largest)

    def __heap_up(self, node):
        if node <= 0:
            return
        parent = int((node - 1)/2)
        if self.heap[node] > self.heap[parent]:
            self.heap[parent], self.heap[node] = self.heap[node], self.heap[parent]
            self.__heap_up(parent)

    def add(self, element: int):
        if self.size < len(self.heap):
            self.heap[self.size] = element
            self.size += 1
            self.__heap_up(self.size - 1)
        elif element < self.heap[0]:
            self.heap[0] = element
            self.__heap_down()


heap = MinHeap(6)
elements = [5, 7, 11, 45, 77, 4, 101, 88, 1, 3, 7, 2, 643, 63, 4, 87, 96]
for el in elements:
    heap.add(el)

print(heap.heap)
