def quicksort(arr):
    if len(arr) <=1:
        return arr
    
    pivot = arr[len(arr)//2]
    right = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    left = [x for x in arr if x > pivot]

    return quicksort(left)+quicksort(middle)+quicksort(right)

arr = [12,11,10,21,1,3,34,9]
sort_arr = quicksort(arr)
print ("sorted array is:", sort_arr)