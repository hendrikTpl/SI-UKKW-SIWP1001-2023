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
with CodeTimer('Linear Search'):
    for i in range(10):
        print('Hello World')
        pass
    
#measure function
class LinearSearch():
    @time_function
    def linear_search(self, nums: list[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1
        

ls = LinearSearch()
print(ls.linear_search([2, 5, 1, 3, 7], 1))
print(ls.linear_search([2, 5, 1, 3, 7], 9))