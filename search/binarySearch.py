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
import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)

from util.decorators import time_decorator

import time

@time_decorator
def binary_search(array, target):
    low = 0
    high = len(array) - 1
    
    start_time = time.perf_counter() 

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            end_time = time.perf_counter()
            runtime = (end_time - start_time) * 1000.0
            return mid, runtime
        
        elif array[mid] < target:
            low = mid + 1
            
        else:
            high = mid - 1
            
    end_time = time.time()
    runtime = (end_time - start_time) * 1000.0
    return -1, runtime

array = [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
target = 144
result, time_of_execution = binary_search(array, target)

if result != -1:
    print(f"Int. found at index {result}")
else:
    print("Int. not found")
    
    print(f"Execution time of {binary_search.time_of_execution}: seconds")