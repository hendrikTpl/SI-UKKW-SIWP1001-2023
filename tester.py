import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)
from utils.time_measurement import time_function,  CodeTimer
#measure the line of code
with CodeTimer('linearsearch'):
    for i in range(10):

        pass
#measure function
@time_function   
def search(numbers,target):
    for i, num in enumerate(numbers):
        if num == target:
            return i
    return -1
    
pass

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