"""
Buat sebuag algorithm LinearSeach

"""
import sys
import os
from typing import List

current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)
from util.time_measurement import time_function,  CodeTimer
from util.decorators import time_decorator
#measure the line of code
with CodeTimer('Line'):
    for j in range(10):
        pass

#measure function





 # write your code here
class LinearSearch():
    @time_decorator 
    @time_function  
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == target:
                return i
            i += 1
        return -1

search = LinearSearch()
nums = [2, 3, 4, 10, 40]
x = 4
result = search.search(nums,x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
pass