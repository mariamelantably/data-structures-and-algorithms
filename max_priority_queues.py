from heaps import max_heapify, make_max_heap
import math 
def find_maximum(heap):
    return heap[0]

def extract_maximum(heap):
    n = len(heap)
    if heap == []:
        raise "HeapOverflowError"
    root = heap[0]
    heap[0] = heap[-1]
    heap = heap[:n-1]
    max_heapify(heap, 0)
    return (root, heap)

def parent(i):
    return i//2

def increase_key_value(heap, i, key):
    if key < heap[i]:
        raise "New key should be greater than or equal to current key"
    heap[i] = key
    while i > 1 and heap[parent(i)] < heap[i]:
        heap[i], heap[parent(i)] = heap[parent(i)], heap[(i)]
        i = parent(i)
    return heap

def insert(heap, key):
    heap.append(-math.inf)
    return increase_key_value(heap, len(heap), key)

def initialise_priority_queue(arr):
    return make_max_heap(arr) #makes the priority queue as a heap