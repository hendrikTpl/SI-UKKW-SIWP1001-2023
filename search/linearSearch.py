"""
Buat sebuag algorithm LinearSeach

"""
from typing import List
from util.decorators import time_decorator

class LinearSearch():
    @time_decorator
    def linear_search(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1
        pass

ls = LinearSearch()
print(ls.linear_search([2, 5, 1, 3, 7], 1))
print(ls.linear_search([2, 5, 1, 3, 7], 9))