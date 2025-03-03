def find_nth_element(a1, a2):
    print(a1,a2)
    if len(a1) == 1: return max(a1[0], a2[0])
    mid = (1+len(a1))//2
    if len(a1)%2 != 0:
        halves = [a1[:mid], a1[mid-1: ], a2[:mid], a2[mid-1:]]
        corner_elements = [halves[0][-2], halves[1][1], halves[2][-2], halves[3][1]]
    else:
        halves = [a1[:mid], a1[mid:], a2[:mid], a2[mid:]]
        corner_elements = [a1[mid-1],a1[mid], a2[mid-1], a2[mid]]
    max1 = halves[return_max_index(corner_elements)]
    min = halves[return_min_index(corner_elements)]
    halves.remove(max1)
    halves.remove(min)
    return find_nth_element(halves[0], halves[1])

def return_max_index(arr):
    i = 0
    m = arr[0]
    for j in range(1, len(arr)):
        if arr[j] > m:
            m = arr[j]
            i = j
    return i 

def return_min_index(arr):
    i = 0
    m = arr[0]
    for j in range(1, len(arr)):
        if arr[j] < m:
            m = arr[j]
            i = j
    return i 

print(find_nth_element([1,2,5,7,8], [3,6,9,12,21]))