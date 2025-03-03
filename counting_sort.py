def counting_sort(arr, k):
    b = []
    n = len(arr)
    for i in range(n):
        b.append(0)
    counts = []
    for i in range(k+1):
        counts.append(0)
    for j in arr:
        counts[j] += 1
    for i in range(1, k+1):
        counts[i] += counts[i-1]
    for j in range(1,n+1):
        current = arr[n-j]
        b[counts[current]-1] = current
        counts[current] -= 1
    return b

print(counting_sort([2,5,3,0,2,3,0,3], 5))

