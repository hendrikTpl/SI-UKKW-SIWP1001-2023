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


@time_function
def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

number = [3, 8, 4, 6, 2]
target = 4

with CodeTimer('LinearSearch'):
    result = linear_search(number, target)

if result != -1:
    print(f"Target {target} ditemukan {result}.")
else:
    print(f"Target {target} tidak ditemukan dalam array.")