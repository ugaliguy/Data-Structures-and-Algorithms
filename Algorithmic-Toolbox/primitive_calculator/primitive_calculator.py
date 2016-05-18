# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    if n == 1:
        return [1]
    sequence += [n]
    if n % 3 == 0:
        n //= 3
        result = optimal_sequence(n)
        sequence += result
    else:
        if n % 2 == 1:
            n -= 1
            result = optimal_sequence(n)
            sequence += result
        else:
            result_1 = optimal_sequence(n - 1)
            result_2 = optimal_sequence(n // 2)
            if len(result_1) < len(result_2):
                sequence += result_1
            else:
                sequence += result_2
    return sequence

def greedy_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
