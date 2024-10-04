def min_boats(weights, max_weight):
    weights.sort()
    boats = 0
    left = 0
    right = len(weights) - 1

    # If one man weights more than the max weight, return -1
    if any(w > max_weight for w in weights):
        return -1

    while left <= right:
        if weights[left] + weights[right] <= max_weight:
            left += 1
        right -= 1
        boats += 1

    return boats


MAX_WEIGHT = int(input())
N = int(input())
WEIGHTS = [int(input()) for _ in range(N)]

print(min_boats(WEIGHTS, MAX_WEIGHT))
