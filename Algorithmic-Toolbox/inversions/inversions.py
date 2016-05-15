# Uses python3
import sys

def merge(a,b):
    c = []
    i = 0
    j = 0
    inv = 0
    m = len(a)
    n = len(b)
    while ( i < m and j < n):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inv += (m - i )

    for p in range(i,m):
         c.append(a[p])

    for q in range(j,n):
         c.append(b[q])

    return c, inv

def merge_sort(a):
    if len(a)>1:
        mid = len(a)//2
        left = a[0: mid]
        right = a[mid: len(a)]
        
        left, left_inv = merge_sort(left)
        right, right_inv = merge_sort(right)
        
        merged, split_inv = merge(left,right)
        
        return merged,(left_inv+right_inv+split_inv)
    else:
        return a,0

def inversions(a):
    count = 0
    if len(a) <= 1:
        return count

    merged, count = merge_sort(a)
    return count

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(inversions(a))