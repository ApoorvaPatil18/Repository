def insertion_sort(arr):
    n = len(arr)
    # Loop through the array, starting from the second element
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            # Shift the value at index j to index j+1 in the array
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = [20, 50, 10, 30]
insertion_sort(arr)
print("After insertion sort : ", arr) 