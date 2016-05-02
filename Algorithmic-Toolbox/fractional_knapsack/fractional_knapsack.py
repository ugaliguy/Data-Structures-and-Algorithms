# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    vwr = []
    if max(values)*capacity == 0:
    	return 0.0

    for i in range(len(weights)):
    	vwr.append([values[i],weights[i],float(values[i]/weights[i])])

    sorted_vwr = sorted(vwr, key = lambda ratio: ratio[2], reverse = True)
    for i in range(len(sorted_vwr)):
    	item_weight = min(sorted_vwr[i][1], capacity)
    	value += item_weight*sorted_vwr[i][2]
    	capacity -= item_weight

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
