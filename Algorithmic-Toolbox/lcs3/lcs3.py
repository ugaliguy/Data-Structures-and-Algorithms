#Uses python3

import sys

def lcs3(a, b, c):
    # Returns the alignment of three sequences a, b, and u.
    # Initialize the matrices.
    lengths = [[[0 for k in range(len(c)+1)] for j in range(len(b)+1)] for i in range(len(a)+1)]
    backtrack = [[[0 for k in range(len(c)+1)] for j in range(len(b)+1)] for i in range(len(a)+1)]

    # Fill in the Score and Backtrack matrices.
    for i in range(1, len(a)+1):
        for j in  range(1, len(b)+1):
            for k in  range(1, len(c)+1):
                scores = [lengths[i-1][j-1][k-1] + int(a[i-1] == b[j-1] == c[k-1]), lengths[i-1][j][k], lengths[i][j-1][k], lengths[i][j][k-1], lengths[i-1][j][k-1], lengths[i][j-1][k-1]]
                backtrack[i][j][k], lengths[i][j][k] = max(enumerate(scores), key=lambda p: p[1])

    # Get the position of the highest scoring cell in the matrix and the high score.
    la = len(a) 
    lb = len(b)
    lc = len(c)
    max_score = lengths[la][lb][lc]
    return max_score

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
