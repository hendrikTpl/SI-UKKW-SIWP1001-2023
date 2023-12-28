import sys
import os

current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)

from util.time_measurement import time_function, CodeTimer

@time_function
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 

    return -1

number = [-1, 0, 3, 5, 9, 12]
target = 9

with CodeTimer('Linear Search'):
    result = linear_search(number, target)

if result != -1:
    print(f"Number {target} berada di indeks ke {result}")
else:
    print(f"Number {target} tidak ditemukan")