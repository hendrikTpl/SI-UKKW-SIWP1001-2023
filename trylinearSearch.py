from typing import List
import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
        return result
    return wrapper

class LinearSearch():
    @time_decorator
    def search(self, nums: List[int], target: int) -> int:
        """
        Mencari nilai target dalam daftar menggunakan algoritma linear search.

        Parameters:
        - nums (List[int]): List angka yang akan dicari.
        - target (int): Nilai yang ingin dicari dalam daftar.

        Returns:
        - int: Indeks pertama tempat target ditemukan, atau -1 jika tidak ditemukan.
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i  # mengembalikan indeks kalau target ditemukan
        return -1  # mengembalikan -1 kalau target tidak ditemukan

# contoh penggunaan:
if __name__ == "_main_":
    linear_search = LinearSearch()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 6
    result = linear_search.search(nums, target)
    
    if result != -1:
        print(f"Target {target} ditemukan pada indeks {result}.")
    else:
        print(f"Target {target} tidak ditemukan dalam daftar.")