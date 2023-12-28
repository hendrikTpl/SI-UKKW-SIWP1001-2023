"""
Buat sebuag algorithm LinearSeach

"""
from typing import List
# from util.decorators import time_decorator
from ..utils.time_measurement import time_function, CodeTimer

class LinearSearch:
    @time_function
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
    

# contoh linarsearch
nums = [1, 2, 3, 4, 5]
target = 3

searcher = LinearSearch()
result = searcher.search(nums, target)

if result != -1:
    print(f"Target {target} ditemukan pada indeks {result}.")
else:
    print(f"Target {target} tidak ditemukan.")
