def knapsack(values, weights, capacity):
    items = sorted(zip(values, weights), key=lambda x: x[0] / x[1], reverse=True)
    return sum((min(w, capacity) * v / w, capacity := max(0, capacity - w))[0] for v, w in items)

# Example usage:
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

result = knapsack(values, weights, capacity)
print("Maximum value in knapsack:", result)
