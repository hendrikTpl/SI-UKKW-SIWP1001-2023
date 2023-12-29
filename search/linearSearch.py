"""
Buat sebuag algorithm LinearSeach

"""
import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)

from util.decorators import time_decorator

import time

@time_decorator
def LinearSearch(array, n, x):

    start_time = time.perf_counter()

    for i in range(0, n):
        if (array[i] == x):
            end_time = time.perf_counter() 
            runtime = (end_time - start_time) * 1000.0
            return i, runtime
        end_time = time.perf_counter()
    runtime = end_time - start_time
    return -1, runtime


array = [2, 4, 0, 1, 9]
x = 1
n = len(array)

result, time_of_execution = LinearSearch(array, n, x)

if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)

    print(f"Execution time of {time_of_execution}: seconds")