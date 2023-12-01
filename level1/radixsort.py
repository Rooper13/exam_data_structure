def radix_sort(arr):
    for exp in range(len(str(max(arr)))):
        output = [[] for _ in range(10)]
        for i in arr:
            output[i // 10**exp % 10].append(i)
        arr = [i for sublist in output for i in sublist]
    return arr

arr = [170, 45, 75, 90, 802, 24, 2, 66]
arr = radix_sort(arr)
print("Sorted array:", arr)
