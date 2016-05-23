# Uses python3

# The goal in this problem is given a set of segments on a line and a set of points 
# on a line, to count, for each point, the number of segments which contain it.


import sys
import random

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r-1)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    lpr = {}
    for i in range(len(starts)):
        lpr[starts[i]] = 'l'
        lpr[ends[i]] = 'r'

    for j in range(len(points)):
        lpr[points[j]] = 'p'    
    #write your code here

    #randomized_quick_sort(lpr, 0, len(lpr))
    sorted(lpr.items(), key=lambda x: x[1])
    print('lpr = ' + str(lpr))
    #for i in range(len(lpr)):
    for k in range(2*len(starts) + len(points)):
        if lpr[k] == 'l' and lpr[k + 1] == 'p' and lpr[k + 2] == 'r':
            # The indexing is off here.
            # I want to find substrings of length 3 that spell 'lpr'
            # count those.
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    #print('data = ' + str(data))
    cnt = fast_count_segments(starts, ends, points)
    print(len(cnt))
    for x in cnt:
        print(x, end=' ')
