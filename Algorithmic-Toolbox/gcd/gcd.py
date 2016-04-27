# Uses python3
import sys

def gcd(a, b):
    if b == 0:
    	return a
    elif a == 0:
    	return b
    elif a >= b:
    	a_prime = a%b
    	return gcd(a_prime,b)
    elif a < b:
    	b_prime = b%a
    	return gcd(b_prime,a)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
