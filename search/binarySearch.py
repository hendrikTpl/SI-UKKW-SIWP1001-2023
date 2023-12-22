"""
Diberikan sebuah array berisi integer nums yang telah diurutkan secara ascending, 
serta sebuah integer target, tuliskan sebuah fungsi untuk mencari target di dalam nums. 
Jika target ada, maka kembalikan indeksnya. Jika tidak, kembalikan -1.

algorithma binarySearch harus mencapai O(log n) runtime complexity.

Contoh 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Penjelasan: 9 ada di nums dan indeksnya adalah 4

Contoh 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Penjelasan: 2 tidak ada di nums jadi kembalikan -1

Batasan:
1 <= panjang nums <= 10^4
-10^4 < nums[i], target < 10^4
semua angka harus integer unik
semua angka di urutkan secara ascending

"""
from typing import List
from util.decorators import time_decorator

class BinarySearch():
    @time_decorator
    def search(self, nums: List[int], target: int) -> int:
        # write your code here
        pass
        
## Add the project root to sys.path
import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)
    import file timer
    from utils.time_measurement import time_function,  CodeTimer
    utils/time_measurement.py
    import functools
import time

class CodeTimer:
    def __init__(self, name=None):
        self.name = f"'{name}'" if name else ''

    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.perf_counter()
        self.took = (self.end - self.start) * 1000.0
        print(f"Code block {self.name} took: {self.took:.2f} ms")

def time_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = (end_time - start_time) * 1000.0
        print(f"Finished '{func.__name__}' in {run_time:.2f} ms")
        return result
    return wrapper

import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)
from utils.time_measurement import time_function,  CodeTimer

#measure the line of code
with CodeTimer('1,2,3,4,5,6,7,8,9,10'):
    for i in range(10):
        #do something
        pass
#measure function
@time_function   
def search(6):
   pass

left = 0
right = len (nums)-1
while left <= right:
mid = (left + right)//2
if nums [mid] == target: return mid
elif nums [mid] < target:
else:
left = mid+1
right = mid-1
return -1

