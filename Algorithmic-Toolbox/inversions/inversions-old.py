# Uses python3
import sys

def merge(l, r):
    m = len(l) - 1
    n = len(r) - 1
    a = []
    i = 0
    j = 0
    inv = 0
    while i <= m and j <= n:
        if l[i] <= r[j]:
            # a.append(l[i])
            i += 1
        else:
            # a.append(r[j])
            inv += m - i
            j += 1
    # return a, inv
    return inv

def merge_sort(a):
    n = len(a)
    inv = 0
    if n >= 2:
        mid = n//2
        l = a[0: mid]
        r = a[mid: n]
        # l, l_inv = merge_sort(l)
        l_inv = merge_sort(l)
        # r, r_inv = merge_sort(r)
        r_inv = merge_sort(r)
        # a, a_inv = merge(l + [sys.maxsize], r + [sys.maxsize])
        a_inv = merge(l + [sys.maxsize], r + [sys.maxsize])
        inv = l_inv + r_inv + a_inv
    # return a, inv
    return inv

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2

    # number_of_inversions += get_number_of_inversions(a, b, left, ave)
    # number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    number_of_inversions = merge_sort(a)
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
