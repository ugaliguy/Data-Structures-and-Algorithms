# Uses python3
import sys

def gcd(a,b):
	# Take advantage of constraint a,b > 0 to simplify
	# calculation of gcd
	if a == 0:
		return b
	elif b ==0:
		return a
	elif a >= b:
		a_prime = a%b
		return gcd(a_prime,b)
	elif a < b:
		b_prime = b%a
		return gcd(b_prime,a)

def lcm(a, b): 
	# Try using the formula lcm(a,b) = a*b/gcd(a,b)
	m = max(a,b)
	n = a + b - m
	# Note the importance of making factors smaller before multiplying
	# If we calculate a*b/gcd then large products can lead to 
	# incorrect answers
	return int(m/gcd(a, b))*n 

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

