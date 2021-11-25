import heapq as hp
import random


def heapify(x):
    def heapify_inner(nums, heapsize, root_index):
        largest = root_index
        left = 2 * root_index + 1
        right = 2 * root_index + 2
        if left < heapsize and nums[largest] < nums[left]:
            largest = left
        if right < heapsize and nums[largest] < nums[right]:
            largest = right
        if largest != root_index:
            nums[largest], nums[root_index] = nums[root_index], nums[largest]
            heapify_inner(nums, heapsize, largest)

    n = len(x)
    for i in range(n, -1, -1):
        heapify_inner(x, n, i)
    return x


def add(heap, x):
    heap.append(x)
    i = len(heap) - 1
    while i > 0 and heap[(i - 1) // 2] < heap[i]:
        heap[(i - 1) // 2], heap[i] = heap[i], heap[(i - 1) // 2]
        i = (i - 1) // 2
    return heap


def heap_remove(heap):
    heap[0], heap[-1] = heap[-1], heap[0]
    heap.pop()
    i = 0
    print(heap)
    while 2 * i + 2 < len(heap):
        if heap[i] > heap[2 * i + 1]:
            if heap[2 * i + 1] < heap[2 * i + 2]:
                heap[i], heap[2 * i + 1] = heap[2 * i + 1], heap[i]
                i = 2 * i + 1
            else:
                heap[i], heap[2 * i + 2] = heap[2 * i + 2], heap[i]
                i = 2 * i + 2
        elif heap[i] > heap[2 * i + 2]:
            if heap[2 * i + 1] < heap[2 * i + 2]:
                heap[i], heap[2 * i + 1] = heap[2 * i + 1], heap[i]
                i = 2 * i + 1
            else:
                heap[i], heap[2 * i + 2] = heap[2 * i + 2], heap[i]
                i = 2 * i + 2
        else:
            break
    if 2 * i + 1 == len(heap) and heap[i] > heap[2 * i + 1]:
        heap[i], heap[2 * i + 1] = heap[2 * i + 1], heap[i]
    return heap


a = [random.randrange(0, 100) for _ in range(30)]
hp.heapify(a)
print(a)
b = heap_remove(a)
print(b)
hp.heapify(b)
print(b)


