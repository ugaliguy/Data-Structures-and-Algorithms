# Uses python3
import sys

def get_change(n):
	tens = n//10
	fives = (n - tens*10)//5
	ones = n%5
	n = tens + fives + ones
	return n

if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_change(n))
