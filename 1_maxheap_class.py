from heapq import heappop, heappush


class MaxHeap:
    def __init__(self):
        self.max_heap = []

    def insert(self, val):
        heappush(self.max_heap, -val)

    def delete(self):
        if self.max_heap:
            return -1 * heappop(self.max_heap)
        return None

    def get_max(self):
        if self.max_heap:
            return -1 * self.max_heap[0]
        return None


if __name__ == "__main__":
    heap = MaxHeap()

    print("Delete from empty heap: ", heap.delete())

    heap.insert(4)
    heap.insert(2)
    heap.insert(1)

    max_num = heap.delete()
    print("Deleted highest number from heap: ", max_num)
    max_num = heap.get_max()
    print("Max number in heap is: ", max_num)
