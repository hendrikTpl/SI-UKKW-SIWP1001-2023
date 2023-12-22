import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)
from utils.time_measurement import time_function,  CodeTimer

class linearSearch:
    @time_function   
    def LinearSearch(data, search):

        indeks = len(data)
        value = False
        data1 = []

        for i in range(0, indeks):
            if search == data[i]:
                value = True
                data1.append(i)

        if value == True:
            print("Data ditemukan!!!")
            for i in data1:
                print("Data terdapat di indeks : ", i)
        else:
            print("Data tidak tersedia")


data = [2,3,4,6,8,9,10,1,2,3,5,8,6,11]
print("Data : ", data)

search = int(input("Mau search data apa : "))
linearSearch.LinearSearch(data, search)
pass