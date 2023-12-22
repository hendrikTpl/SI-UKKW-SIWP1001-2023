import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)
from util.time_measurement import time_function,  CodeTimer

class Search:
    @staticmethod
    @time_function
    def linear_search(list, target):
        for i in range(len(list)):
            if list[i] == target:
                return f"Target {target} is found at index {i}"
        return "Target not found"

    @staticmethod
    @time_function
    def binary_search(list, target):
        list.sort()
        low = 0
        high = len(list) - 1

        while low <= high:
            mid = (low + high) // 2
            if list[mid] == target:
                return f"Target {target} found at index {mid}"
            elif list[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return "Target not found"

# list = [5,2,3,1,6,7,4,8]
# target = 4

# ls = Search.ls(list, target)
# bs = Search.bs(list, target)
# print(ls)
# print(bs)