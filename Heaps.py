class MaxHeap:
    def __init__(self):
        self.heap = []

    def print_heap(self):
        print(self.heap)

    def _left_node(self,index):
        return 2 * index + 1
    
    def _right_node(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)


max_heap = MaxHeap()

max_heap.insert(99)
max_heap.insert(72)
max_heap.insert(61)
max_heap.insert(58)

max_heap.print_heap()

max_heap.insert(100)

max_heap.print_heap()

max_heap.insert(75)

max_heap.print_heap()