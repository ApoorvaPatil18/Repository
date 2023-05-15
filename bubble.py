# Apoorva
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Compare adjacent elements and swap them if they are in the wrong order
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [40, 80, 25, 12]
bubble_sort(arr)
print("After bubble sort : ", arr)
