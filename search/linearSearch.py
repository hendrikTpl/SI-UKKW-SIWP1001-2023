"""
Buat sebuag algorithm LinearSeach

"""
import sys
import os
import time
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)
from util.time_measurement import time_function,  CodeTimer

class LinearSearch():
    @time_function
    def linier_search(nums, target):
        i = 0

        while i < len(nums):
            if nums[i] == target:
                return i
            i = i + 1
        return i

# nums = [2,4,5,6,7,8,9]
# target = 9

# print(linier_search(nums, target))