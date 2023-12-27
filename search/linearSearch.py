"""
Buat sebuag algorithm LinearSeach

"""
from typing import List
from util.decorators import time_decorator

class LinearSearch():
    @time_decorator
    def search(self, nums: List[int], target: int) -> int:
        # write your code here
        n = len(nums)
        nums.append(target)
        for i in range(n):
            if nums[i] == target:
                return i
        return -1

Lsr = LinearSearch()
print(Lsr.search([3, 8, 4, 6, 2], 4))  
print(Lsr.search([3, 8, 4, 6, 2], 4))