# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinMax(i, j, op, m, M):
    minimum = 100000   # Since the only numbers are the digits 0 - 9 
    maximum = -100000  # min and max are large enough
    for k in range(i, j):
        a = evalt(M[i][k], M[k+1][j], op[k])
        b = evalt(M[i][k], m[k+1][j], op[k])
        c = evalt(m[i][k], M[k+1][j], op[k])
        d = evalt(m[i][k], m[k+1][j], op[k])
        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    return(minimum, maximum)

def get_maximum_value(dataset):
    #write your code here
    ops = dataset[1:len(dataset):2]
    digits = dataset[0:len(dataset)+1:2]
    n = len(digits)
    #iniitializing matrices/tables
    m = [[0 for i in range(n)] for j in range(n)]  #minimized values
    M = [[0 for i in range(n)] for j in range(n)]  #maximized values
    for i in range(n):
        m[i][i] = int(digits[i])   #so that the tables will look like
        M[i][i] = int(digits[i])   #[[i, 0, 0...], [0, i, 0...], [0, 0, i,...]]
    for s in range(1,n):   #here's where I get confused
        for i in range(n-s):
            j = i + s
            m[i][j], M[i][j] = MinMax(i,j,ops,m,M)
    return M[0][n-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
