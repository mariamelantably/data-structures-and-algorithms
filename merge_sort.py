from math import inf

def merge_sort(arr):
    if len(arr) <= 1: return arr
    else:
        mid = (len(arr) + 1)//2
        return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))
    
def merge(a1, a2):
    a1.append(inf)
    a2.append(inf)
    newa = []
    i = 0
    j = 0
    while (len(newa) != len(a1) + len(a2) - 2):
        if a1[i] < a2[j]:
            newa.append(a1[i])
            i += 1
        else:
            newa.append(a2[j])
            j += 1
    return newa
    
print(merge_sort([1,7,9,8,3,4,13,21]))