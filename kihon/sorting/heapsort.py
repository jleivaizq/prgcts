
def heapsort(A):

    A.insert(0,0)
    heap_size = len(A)-1

    def max_heapify(i):
        """Keeps heap property inside a Heap"""

        largest = reduce(lambda i,j: i if A[i] > A[j] else j,
                         [x for x in [i, i << 1, i << 1 | 1] if x <= heap_size])
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            max_heapify(largest)
    
    def build_max_heap():
        """Build a Heap from a unsorted array"""

        for i in range(heap_size >> 1, 1, -1):
            max_heapify(i)

    build_max_heap()

    for i in range(len(A)-1, 1, -1):
        A[i], A[1] = A[1], A[i]
        heap_size -= 1
        max_heapify(1)

    A.pop(0)
        
if __name__ == '__main__':
    values = [16,4,10,14,7,9,3,2,8,1]
    heapsort(values)
    assert values == [1,2,3,4,7,8,9,10,14,16]

