def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target element
    return -1  # Return -1 if the target element is not found

my_list = [4, 2, 8, 5, 1, 9, 3]
target_element = 5

result = linear_search(my_list, target_element)

if result == -1:
    print("Element not found")
else:
    print("Element found at index", result)
