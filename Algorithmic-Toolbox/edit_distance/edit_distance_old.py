# Uses python3
def edit_distance(s, t):
    #write your code here
    m = len(s)
    n = len(t)
    if s == t:
    	return 0
    elif m == 0:
    	return n
    elif n == 0:
    	return m
    distances = [[0 for i in range(m + 1)] for j in range(n + 1)]
    # distances = []
    for i in range(m + 1):
    	distances[i][0] = i
    for j in range(n + 1):
    	distances[0][j] = j

    for i in range(1, m + 1):
    	for j in range(1, n + 1):
    		diff = 1
    		if s[i - 1] == t[j - 1]:
    			diff = 0
    		distances[i][j] = min(distances[i][j - 1] + 1, distances[i - 1][j] + 1, distances[i - 1][j - 1] + diff)
    # print('BLAH!')
    # print(distances[m][n]) 
    return distances[m][n]

if __name__ == "__main__":
    print(edit_distance(input(), input()))