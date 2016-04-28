# Uses python3
import sys

def memoize(fn, arg, m):
 memo = {}
 if arg not in memo:
  memo[arg] = fn(arg, m)
  return memo[arg]

def pisano(m):
	a,b = 1,1
	count = 1
	for i in range(6*m):
		if (a == 0 and b == 1):
			# print('count = ' + str(count))
			return count
		else:
			a,b = b%m, (a+b)%m
			count += 1

def fib(n, m):
 a,b = 1,1
 p = pisano(m)
 q = n//p
 r = n - q*p
 # print('r = ' + str(r))
 if r == 0:
 	return 0
 else:
 	for i in range(r-1):
 		a,b = b, (a+b)
 	return a

 

def get_fibonaccihuge(n, m):
	return memoize(fib,n, m)%m

#print(get_fibonaccihuge(292, 5))

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))
