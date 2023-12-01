def bucket_sort(arr):
    buckets = [[] for _ in range(len(arr))]
    for num in arr:
        buckets[int(num * len(arr))].append(num)
    return [num for bucket in buckets for num in sorted(bucket)]

# Example usage:
my_list = [0.23, 0.56, 0.11, 0.75, 0.32, 0.88, 0.44]
sorted_list = bucket_sort(my_list)
print(sorted_list)
