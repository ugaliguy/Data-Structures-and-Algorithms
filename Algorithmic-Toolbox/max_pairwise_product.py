# Uses python2
n = int(raw_input())
a = [int(x) for x in raw_input().split()]
assert(len(a) == n)

# result = 0

# for i in range(0, n):
#     for j in range(i+1, n):
#         if a[i]*a[j] > result:
#             result = a[i]*a[j]

max_1 = max(a)
a.remove(max_1)
max_2 = max(a)

result = max_1*max_2
print(result)
