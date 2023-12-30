"""
Buat sebuah algorithm LinearSeach

"""
from typing import List
from util.decorators import time_decorator

class LinearSearch():
    @time_decorator
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

searcher = LinearSearch()

nums = [8, 5, 8, 1, 4, 9, 3]
target = 4

index = searcher.search(nums, target)

if index != -1:
    print(f"Found target at index {index}")
else:
    print("Target not found")
pass