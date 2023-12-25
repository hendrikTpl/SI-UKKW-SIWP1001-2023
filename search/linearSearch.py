"""
Buat sebuag algorithm LinearSeach

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
    def time_function(func):
        def wrapper(self, List_1, item):
            start_time = time.time()
            result = func(self, List_1, item)
            end_time = time.time()
            runtime = end_time - start_time
            print(f"waktu eksekusi: {runtime} detik")
            return result
        return wrapper

    @time_function
    def linear(self, List_1, item):
        for i in range(len(List_1)):
            if item == List_1[i]:
                print("Item ada di index ke:", i)
                break
        else:
            print("Item tidak ditemukan")


linear_search = LinearSearch()

List_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item = 5

linear_search.linear(List_1, item)

