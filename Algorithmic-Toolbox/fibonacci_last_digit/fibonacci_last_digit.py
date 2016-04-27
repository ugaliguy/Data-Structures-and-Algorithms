# Uses python3
import sys

def get_fibonacci_last_digit(n):
	fib_last = [0,1] # Last digits of first two Fibonacci numbers
	for i in range(2, n+1):
		fib_last.append((fib_last[i-1] + fib_last[i-2])%10)
	return fib_last[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
