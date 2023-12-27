# """
# Diberikan sebuah array berisi integer nums yang telah diurutkan secara ascending, 
# serta sebuah integer target, tuliskan sebuah fungsi untuk mencari target di dalam nums. 
# Jika target ada, maka kembalikan indeksnya. Jika tidak, kembalikan -1.

# algorithma binarySearch harus mencapai O(log n) runtime complexity.

# Contoh 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Penjelasan: 9 ada di nums dan indeksnya adalah 4

# Contoh 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Penjelasan: 2 tidak ada di nums jadi kembalikan -1

# Batasan:
# 1 <= panjang nums <= 10^4
# -10^4 < nums[i], target < 10^4
# semua angka harus integer unik
# semua angka di urutkan secara ascending

# """
import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)
from util.time_measurement import time_function,  CodeTimer


import time


class BinarySearch:
    def binarySearch(self, data, target):
        start_time = time.time()
        low = 0
        high = len(data) - 1  

        temp = False

        while low <= high and not temp:
            mid = (low + high) // 2

            if data[mid] == target:
                temp = True
                print("Nilai", target, "berada di index ke-", mid)
            
            else:
                if target < data[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        
        end_time = time.time()
        runtime = end_time - start_time
        print (f'waktu eksekusinya :{runtime} detik')
        
        return temp  
        

data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 80

binary_search_instance = BinarySearch()
hasil = binary_search_instance.binarySearch(data, target)

if hasil:
    print("Nilai", target, "ditemukan")
else:
    print("Nilai", target, "tidak ditemukan")
