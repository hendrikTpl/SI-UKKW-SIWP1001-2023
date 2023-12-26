"""
Buat sebuag algorithm LinearSeach

"""
from typing import List
from util.time_measurement import time_function, CodeTimer

class LinearSearch():
    @time_function
    def search(nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
