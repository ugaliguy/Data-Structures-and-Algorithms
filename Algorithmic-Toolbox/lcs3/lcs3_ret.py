#Uses python3

# This returns a longest commonn subsequence for three sequences

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

    # Quick lambda function to insert insertions/deletions.
    insert_indel = lambda word, i: word[:i] + ['-'] + word[i:]

    # Initialize the aligned strings as the input strings.
    a_aligned = a
    b_aligned = b
    c_aligned = c

    # Get the position of the highest scoring cell in the matrix and the high score.
    la = len(a) 
    lb = len(b)
    lc = len(c)
    max_score = lengths[la][lb][lc]
    
    # Backtrack to the edge of the matrix starting at the highest scoring cell.
    while i*j*k != 0:
        if backtrack[i][j][k] == 1:
            i -= 1
            c_aligned = insert_indel(c_aligned, j)
            a_aligned = insert_indel(a_aligned, k)
        elif backtrack[i][j][k] == 2:
            j -= 1
            b_aligned = insert_indel(b_aligned, i)
            a_aligned = insert_indel(a_aligned, k)
        elif backtrack[i][j][k] == 3:
            k -= 1
            b_aligned = insert_indel(b_aligned, i)
            c_aligned = insert_indel(c_aligned, j)
        elif backtrack[i][j][k] == 4:
            i -= 1
            j -= 1
            a_aligned = insert_indel(a_aligned, k)
        elif backtrack[i][j][k] == 5:
            i -= 1
            k -= 1
            c_aligned = insert_indel(c_aligned, j)
        elif backtrack[i][j][k] == 6:
            j -= 1
            k -= 1
            b_aligned = insert_indel(b_aligned, i)
        else:
            i -= 1
            j -= 1
            k -= 1

    # Prepend the necessary preceeding indels to get match lengths.
    while len(b_aligned) != max(len(b_aligned),len(c_aligned),len(a_aligned)):
        b_aligned = insert_indel(b_aligned, 0)
    while len(c_aligned) != max(len(b_aligned),len(c_aligned),len(a_aligned)):
        c_aligned = insert_indel(c_aligned, 0)
    while len(a_aligned) != max(len(b_aligned),len(c_aligned),len(a_aligned)):
        a_aligned = insert_indel(a_aligned, 0)

    return str(max_score), a_aligned, b_aligned, c_aligned

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