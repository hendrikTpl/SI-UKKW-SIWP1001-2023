from search.linearSearch import linear_search


numbers = [4, 2, 5, 1, 7, 3, 6, 8]
target = 5
result = linear_search(numbers, target)

if result != -1:
    print(f"Target {target} found at index: {result}")
else:
    print(f"Target {target} not found in the array.")

numbers = [4, 2, 5, 1, 7, 3, 6, 8]
target = 9

result = linear_search(numbers, target)

if result != -1:
    print(f"Target {target} found at index: {result}")
else:
    print(f"Target {target} not found in the array.")
    pass