def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

my_list = [1, 3, 5, 7, 9]
target_element = 5

result = linear_search(my_list, target_element)

if result != -1:
    print(f"Element {target_element} ditemukan di indeks {result}.")
else:
    print(f"Element {target_element} tidak ditemukan dalam list.")

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = arr[mid]

        if mid_element == target:
            return mid
        elif mid_element < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
target_element = 7

result = binary_search(sorted_list, target_element)

if result != -1:
    print(f"Element {target_element} ditemukan di indeks {result}.")
else:
    print(f"Element {target_element} tidak ditemukan dalam list.")