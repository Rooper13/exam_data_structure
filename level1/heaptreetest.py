import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    result = []
    while arr:
        result.append(heapq.heappop(arr))
    return result

arr= [12,1,23,2,34,3]
print("sorted array is:", heap_sort(arr))