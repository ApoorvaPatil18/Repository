def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Return the index of the target element
        elif arr[mid] < target:
            left = mid + 1  # Update the left boundary
        else:
            right = mid - 1  # Update the right boundary

    return -1  # Return -1 if the target element is not found

my_list = [1, 2, 3, 4, 5, 8, 9]
target_element = 5

result = binary_search(my_list, target_element)

if result == -1:
    print("Element not found")
else:
    print("Element found at index", result)
