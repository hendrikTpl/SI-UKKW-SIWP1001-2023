import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)
from utils.time_measurement import time_function,  CodeTimer

@time_function   
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

nums = [1,2,3,4,5,6,8,9,10,11]
print("Data : ", nums)

target = int(input("Mau search data apa : "))
result = binary_search(nums, target)


if result != -1:
    print(f"target: {target}")
    print(f"Output: {result}")
    print(f"Penjelasan: {target} ada di nums dan indeksnya adalah {result}")
else:
    print(f"target: {target}")
    print(f"Output: {result}")
    print(f"Penjelasan: {target} tidak ada di nums, kembalikan -1")
pass