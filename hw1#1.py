"""
Homework-1 #1 
Penjumlahan ganjil genap dari dua buah List

Deskripsi: 
•	Misalkan ada dua buah List, katakan ListA dan ListB yang berisi bilangan Integer.
•	Kemudian buat sebuah list baru katakan saja ListGanjil yang berisi semua angka ganjil dari ListA dan ListB. 
•	Setelah itu buat list baru lagi, katakan ListGenap yang mana berisi semua angka genap dari ListA dan ListB
•	Jika jumlah semua angka di listGanjil lebih besar dari jumlah semua angka di listGenap, kembalikan sebuah tuple (listGanjil, listGenap). Sebaliknya, kembalikan tuple (listGenap, listGanjil)

Contoh:

Input: 
ListA = [1,2,3,4,5]
ListB = [6,7,8,9,10]

Output:
([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])

"""

# Possible Solution-1
def sum_odd_even_list(listA, listB):
    listGanjil = [num for num in listA if num % 2 != 0] + [num for num in listB if num % 2 != 0]
    listGenap = [num for num in listA if num % 2 == 0] + [num for num in listB if num % 2 == 0]
    
    if sum(listGanjil) > sum(listGenap):
        return (listGanjil, listGenap)
    else:
        return (listGenap, listGanjil)

# Test
listA = [1, 2, 3, 4, 5]
listB = [6, 7, 8, 9, 10]

print(sum_odd_even_list(listA, listB))
