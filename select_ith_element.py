def select(arr, i):
    n = len(arr)
    x = []
    ia = 0 
    while ia < n:
        x.append(arr[ia:ia+5])
        ia += 5
    medians = []
    for j in x:
        medians.append(sorted(j)[(len(j) + 1)//2 - 1])
    y = sorted(medians)[(len(medians) +1)//2 - 1]
    lower = [a for a in arr if a < y]
    upper = [a for a in arr if a > y]
    k = len(lower)
    if i == k + 1:
        return y
    elif i < k + 1:
        return select(lower, i)
    else:
        return select(upper, i - len(lower) - 1)

print(select([1,2,8,9,3,4,6,7,17,13,21,5,11], 11))