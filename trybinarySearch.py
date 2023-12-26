from typing import List
import time

from util.time_measurement import time_function, CodeTimer
class BinarySearch:
    @time_function
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid  # target ditemukan, lalu kembalikan indeksnya
            elif nums[mid] < target:
                low = mid + 1  # pindahin batas bawah
            else:
                high = mid - 1  # pindahin batas atas

        return -1  # kalau target tidak ditemukan, kembalikan -1

# contoh penggunaan:
binary_search_instance = BinarySearch()
nums_list_1 = [-1, 0, 3, 5, 9, 12]
target_value_1 = 9
result_1 = binary_search_instance.search(nums_list_1, target_value_1)
print(result_1)

nums_list_2 = [-1, 0, 3, 5, 9, 12]
target_value_2 = 2
result_2 = binary_search_instance.search(nums_list_2, target_value_2)
print(result_2)
