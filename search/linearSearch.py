"""
Buat sebuag algorithm LinearSeach

"""
import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)

from util.decorators import time_decorator

import time

def linear_search(data, target):
    start_time = time.time()  # Catat waktu mulai eksekusi
    for i in range(len(data)):
        if data[i] == target:
            end_time = time.time()  # Catat waktu berakhir eksekusi jika elemen ditemukan
            runtime = end_time - start_time
            return i, runtime
    end_time = time.time()  # Catat waktu berakhir eksekusi jika elemen tidak ditemukan
    runtime = end_time - start_time
    return -1, runtime

# Contoh penggunaan
data = [1, 3, 5, 7, 9, 11, 13]
target = 9

hasil_pencarian, waktu_eksekusi = linear_search(data, target)

if hasil_pencarian != -1:
    print(f"Elemen {target} ditemukan pada indeks {hasil_pencarian}.")
else:
    print(f"Elemen {target} tidak ditemukan dalam data.")

print(f"Waktu eksekusi: {waktu_eksekusi} detik.")


