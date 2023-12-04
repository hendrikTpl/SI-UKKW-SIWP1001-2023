from typing import List
from util.decorators import time_decorator

class HashSearch():
    @time_decorator
    def search(self, nums: List[int], target: int) -> int:
        hash_table = {}
        for i in range(len(nums)):
            hash_table[nums[i]] = i
        return hash_table.get(target, -1)
    