"""
Buat sebuag algorithm LinearSeach

"""
import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)
from util.time_measurement import time_function,  CodeTimer
#measure the line of code
with CodeTimer('tugas'):
    for i in range(10):
        #do something
        pass
    from typing import List
from util.decorators import time_decorator
#measure function
 


class LinearSearch():
    @time_decorator
    @time_function  
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i

ls = LinearSearch()

# Example usage:
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
index = ls.search(nums, target)

if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found in the list")
