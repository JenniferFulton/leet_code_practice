# O(n^2) because you will loop through the list twice

# How does this work for alpha?

def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(min_index + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
    if i != min_index:
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return(arr)

print(selection_sort([10,6,9,7,2,3,1,4,5,8]))
