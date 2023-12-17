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
from util.time_measurement import time_function,  CodeTimer

class BinarySearch():
    @time_function
    def binary_search(nums, target):
        low = 0
        high = len(nums) -1

        while low <= high:
            mid = low + (high-low) //2
            mid_value = nums[mid]

            if mid_value == target:
                return mid

            elif target < mid_value:
                high = mid -1
            
            else:
                low = mid +1

        return none

# nums_1 = [2,3,4,5,6,7,8,9]
# target_1 = 7

# print(search(nums_1, target_1))

