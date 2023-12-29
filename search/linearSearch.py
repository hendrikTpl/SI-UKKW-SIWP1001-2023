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
with CodeTimer('LS24'):
    for i in range(10):
        #do something
        pass
#measure function

from typing import List
from util.decorators import time_decorator

class LinearSearch():
    @time_decorator
    @time_function 
    def search(self, nums: List[int], target: int) -> int: 
        for i in range(len(nums)): 
            if nums[i] == target: 
                return i 
        return -1 
            
ls = LinearSearch()

nums = [3, 1, 4, 7, 5]
target = 5
index = ls.search(nums, target)
print(f"Index of {target} in nums: {index}")