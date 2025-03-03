def inversions(a):
    if len(a) == 1:
        return 0
    else:
        q = (len(a))//2
        s = sorted(a[:q])
        r = sorted(a[q:])
        return inversions(a[:q]) + inversions(a[q:]) + mergeInversions(s,r)
    
def mergeInversions(a1, a2):
    count = 0 
    i = 0
    j = 0
    while (i < len(a1)) & (j < len(a2)):
        if a1[i] <= a2[j]:
            i += 1
        else:
            count += len(a1) - i
            j += 1
    return count

def simple_inversions(A):
    inv = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
                if A[i] > A[j]:
                    inv += 1
    return inv

li = []

from random import choice

for _ in range(100):
    li = [choice(list(range(100))) for _ in range(10)]
    assert simple_inversions(li) == inversions(li), f"{li} {simple_inversions(li)} {inversions(li)}"
