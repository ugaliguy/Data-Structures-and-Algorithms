# python3

import random

p = 1000000007 #big prime
x = random.randint(1,p-1)

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def precompute_hashes(text,pattern_length,pattern,x):
    h = [0 for i in range(len(text)- len(pattern)+1)]
    s = text[len(text)-pattern_length:]
    h[len(text)-pattern_length] = poly_hash(s)
    y = 1
    for i in range(1,pattern_length+1):
        y = y*x % p

    for i in range(len(text)-pattern_length-1,-1,-1):
        h[i] = (x*h[i+1] + ord(text[i]) - y*ord(text[i+pattern_length])) % p
    return h

def poly_hash(pattern): 
    ans = 0
    for c in reversed(pattern):
        ans = (ans * x + ord(c)) % p
    return ans

def get_occurrences(pattern, text):
    result = []
    pHash = poly_hash(pattern)
    h = precompute_hashes(text,len(pattern),pattern,x)
    for i in range(0,len(text)-len(pattern)+1):
        if pHash != h[i]:
            continue
        if pattern == text[i:i+len(pattern)]:
            result.append(i)
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

