# Uses python3

# The goal in this problem is given a set of segments on a line and a set of points 
# on a line, to count, for each point, the number of segments which contain it.


import sys
import collections


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    points_dict = collections.defaultdict(set)

    pairs = []
    for i in starts:
        pairs.append((i, 'l'))
    for i in ends:
        pairs.append((i, 'r'))
    for i in range(len(points)):
        point = points[i]
        pairs.append((point, 'p'))
        points_dict[point].add(i)    
    #write your code here

    sorted_pairs = sorted(pairs, key=lambda x: (x[0], x[1]))

    lpr = 0
    for pair in sorted_pairs:
        if pair[1] == 'l':
            lpr += 1
        if pair[1] == 'r':
            lpr -= 1
        if pair[1] == 'p':
            indices = points_dict[pair[0]]
            for i in indices:
                cnt[i] = lpr

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
    # print(len(cnt))
    for x in cnt:
        print(x, end=' ')
