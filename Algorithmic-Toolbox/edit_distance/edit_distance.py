# Uses python3
def edit_distance(s, t):
    # write your code here
    m = len(s)
    n = len(t)
    if m > n:
        return edit_distance(t,s)

    if n == 0:
        return m
    elif s == t:
        return 0

    distances = range(m + 1)
    for j, ch2 in enumerate(t):
        new_distances = [j + 1]
        for i, ch1 in enumerate(s):
            if ch1 == ch2:
                new_distances.append(distances[i])
            else:
                minimum = min(distances[i], distances[i + 1], new_distances[-1])
                new_distances.append(1 + minimum)
        distances = new_distances

    return distances[-1]

if __name__ == "__main__":
    print(str(edit_distance(input(), input())))