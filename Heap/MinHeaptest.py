from src.minHeap import *

# Print('Heap')

h1 = MinHeap([1, 11, 9, 2, 3])
h1.buildHeap()
h1.heapPrint()
h1.insert(7)
h1.insert(5)
h1.insert(9)
h1.insert(4)
h1.insert(11)
h1.insert(19)
h1.insert(20)
h1.insert(21)
h1.insert(11)
h1.heapPrint()
h1.deleteMin()
h1.heapPrint()