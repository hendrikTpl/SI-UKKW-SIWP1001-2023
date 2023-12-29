"""
Buat sebuag algorithm LinearSeach

"""
import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)
from util.time_measurement import time_function, CodeTimer

import time

class LinearSearch:
    def time_function(func):
        def wrapper(self, data, cari):
            start_time = time.time()
            result = func(self, data, cari)
            end_time = time.time()
            runtime = end_time - start_time
            print(f"Finished: {runtime} detik")
            return result
        return wrapper

    @time_function
    def linear(self , data, cari):
        for i in range(len(data)):
            if cari == data[i]:
                print("item ada :", i)
                break
        else:
            print("item tiada")

linear_search = LinearSearch()

data = [21, 24, 25, 27, 30, 31, 44, 56]
cari = 56

linear_search.linear(data, cari)