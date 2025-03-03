def max_heapify(arr, i):
    n = len(arr) - 1
    l = 2*i + 1
    r = 2*i + 2
    if l <= n:
        if arr[l] > arr[i]:
            largest = l 
        else: largest = i
    else: largest = i 
    if r <=n:
        if arr[r] > arr[largest]:
            largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        return max_heapify(arr, largest)
    else:
        return arr

def make_max_heap(arr):
    n = len(arr)
    for i in range((n+1)//2 - 1, -1, -1):
        arr = max_heapify(arr, i)
    return arr

def heapsort(arr):
    heaped_arr = make_max_heap(arr)
    new_arr = []
    while heaped_arr != []:
        new_arr = [heaped_arr[0]] + new_arr
        heaped_arr = max_heapify(heaped_arr[1:], 0)
    return new_arr




print(heapsort([4,1,3,2,16,9,10,14,8,7]))