# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    # result = 0
    # for x in w:
    #     if result + x <= W:
    #         result = result + x
    # return result
    bars = [[0 for i in range(n + 1)] for j in range(W + 1)]
    for i in range(1, n + 1):
    	for wt in range(1, W + 1):
    		bars[wt][i] = bars[wt][i - 1]
    		if w[i-1] <= wt:
    			bars[wt][i] = max(bars[wt - w[i-1]][i-1] + w[i -1], bars[wt][i])
    return bars[W][n]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
