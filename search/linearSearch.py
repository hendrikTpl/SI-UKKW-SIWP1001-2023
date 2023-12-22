"""
Buat sebuag algorithm LinearSeach

"""
from typing import List
from util.decorators import time_decorator

class LinearSearch():
    @time_decorator
    def search(self, nums: List[int], target: int) -> int:
        # write your code here
        pass
 main.py LinearSearch --indata "<1,2,3,4,5,6,7,8,9,10,11>" target:5
    data ditemukan!!!
    data terdapat di indeks:5
main.py LinearSearch --indata "<1,2,3,4,5,6,7,8,9,10,11>" target:15
    data tidak tersedia
