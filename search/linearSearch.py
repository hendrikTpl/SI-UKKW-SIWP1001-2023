"""
Buat sebuah algorithm LinearSeach

definisikan linear search terlebih dahulu 
lalu buat fungsi untuk mencari target 
tuliskan sebuah fungsi untuk mencari target di dalam nums. 
Jika target ada, maka kembalikan indeksnya. Jika tidak, kembalikan -1.

"""
import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)
from util.time_measurement import time_function,  CodeTimer


import time


class LinearSearch:
    def linearSearch(self, List, target):
        start_time = time.time()
        i = 0
        pos = -1
        while i < len(List):
            if List[i] == target:
                pos = i
                end_time = time.time()
                runtime = end_time - start_time
                return True, pos, runtime
            i = i + 1

        end_time = time.time()
        runtime = end_time - start_time
        return False, pos, runtime

List = [3, 5, 7, 9, 11, 13]
target = 13

linear_search_instance = LinearSearch()
hasil, pos, runtime = linear_search_instance.linearSearch(List, target)

if hasil:
    print(f'Found at {pos} waktu eksekusinya :{runtime} detik')
else:
    print(f'Not Found waktu eksekusinya :{runtime} detik')
