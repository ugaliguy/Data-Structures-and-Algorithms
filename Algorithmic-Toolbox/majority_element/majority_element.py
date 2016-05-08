# Uses python3
import sys

def get_majority_element(a, left, right):
    # if left == right:
    #     return -1
    # if left + 1 == right:
    #     return a[left]
    #write your code here
      
    maj = a[0]
    count = 1
    for num in a:
        if num == maj:
            count += 1
        elif count == 0:
            maj = num
            count = 1
        else:
            count -= 1

    maj_count = 0
    for i in range(len(a)):
        if a[i] == maj:
            maj_count += 1

    if maj_count > n//2:
        return maj
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
