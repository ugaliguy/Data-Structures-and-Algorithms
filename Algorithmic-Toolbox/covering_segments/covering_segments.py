# Uses python3
import sys
from collections import namedtuple
from operator import attrgetter

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    start_sort = sorted(segments, key=attrgetter('start'))
    end_sort = sorted(segments, key=attrgetter('end'))
    points = []
    #write your code here
    minimum = start_sort[0].start - 1
    for i in range(len(segments)):
        begin = end_sort[i].start
        end = end_sort[i].end
        if begin > minimum:
            points.append(end)
            minimum = end
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
