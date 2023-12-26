"""
Buat sebuag algorithm LinearSeach

"""
from typing import List
from util.time_measurement import time_function, CodeTimer

class Linear_Search():
    @time_function
    
    def search(input_list: list, element: int):
        list_len = len(input_list)
        for i in range(list_len):
            if input_list[i] == element:
                return i
            i = i + 1
        
        
mylist = [2,3,5,8,9,12,14,15,18,20]
print("Given list is:", mylist)
position = Linear_Search.search(mylist, 12)
print("Element 12 at position:", position)



   