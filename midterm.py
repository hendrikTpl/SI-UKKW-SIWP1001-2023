"""
Rewrite this code using 'While Looping'

"""

# for i in range (1,20):
# 	if  i % 2 == 0:
# 		print("bilangan genap lebih kecil dari 20:{}".format(i))
# 	else:
# 		print("bilangan ganjil lebih kecil dari 20:{}".format(i))


# i = 1
# while i < 20:
# 	if i % 2 == 0:
# 		print("bilangan genap lebih kecil dari 20:{}".format(i))
# 	else:
# 		print("bilangan ganjil lebih kecil dari 20:{}".format(i))
# 	i += 1


# """
# sort a list using buble sort technique
# """

# arr = [64, 34, 25, 12, 22, 11, 90]
# n = len(arr)
# print("The list is: ", arr)
# for i in range (n):
# 	for j in range (0, n-i-1):
# 		if arr[j] > arr[j+1]:
# 			arr[j], arr[j+1]= arr[j+1], arr[j]
# print("sorted list is: ", arr)


# """
# # Error code. You need to find the error and fix it
# # sort a list using bubble sort technique
# The error introduced here is inside the swapping of elements 
# in the list: arr[j], arr[j+1] = arr[j], arr[j].
# """
# arr = [64, 34, 25, 12, 22, 11, 90]
# n = len(arr)
# print("The list is: ", arr)
# for i in range(n):
# 	for j in range(0, n-i-1):
# 		if arr[j] > arr[j+1]:
# 			arr[j], arr[j+1]= arr[j], arr[j]
# print("Sorted list is: ", arr)


# """
# # Sort a list using the Quick Sort technique
# """
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr.pop()
#         items_greater = []
#         items_lesser = []
        
#         for item in arr:
#             if item > pivot:
#                 items_greater.append(item)
#             else:
#                 items_lesser.append(item)
                
#         return quick_sort(items_lesser) + [pivot] + quick_sort(items_greater)

# arr = [64, 34, 25, 12, 22, 11, 90]
# print("The list is:", arr)
# arr = quick_sort(arr)
# print("Sorted list is:", arr)

"""
Find the error in the following code
"""
# #1
# #a)
# y = x + 5
# print(x, y)

# #b)
# a = input("value: ")
# b =a/2
# print(a,b)

# #c)
# print(x=y=5)

#2
#a)
# temp = 90
# print temp

# #b)
# a =12
# b= a + b
# print(a And b)

# #c) 
# print("x="x)

# #3
# #a)
# a,b,c = 2,8,4
# print(a,b,c)
# c,b,a =a,b,c
# print(a;b;c)

# #b)
# x =23
# 4 = x

# #c)
# else = 21-4

# #4)
# ## find the error
# n = int(10)
# i = 0
# while i < n:
#     if i == 5:
#         break
#     print(i)
#     i += 1

# ## using while loop
n = int(10)
i = 0
while i < n:
    i += 1
    if i == 5:
        break
    print(i) 


# ## apa yang menjadi output skrip berikut ini
# name='Hari'
# age=18
# print(name,", you are ",age," now but ",end="")
# print("You will be ",age+1," next Year")

# x, y = 7, 12
# x, y, x = x + 6, y + 7, x + 10
# print(x, y)

# If condition1:
#     # code-block of statements when condition1 is true
# elif condition2:
#     # code-block of statements when condition2 is true
# elif condition3:
#     # code-block of statements when condition3 is true
# . . .
# else:
#     # code-block of statements when all above conditions are false.

# s = input("Enter String")
# RS = ""
# for ch in s:
#     RS = ch * 2 + RS
# print(RS + s)

# """
# Tuliskanlah skrip python untuk menampilkan output sebagai berikut ini
# #
# # #
# # # #
# # # # #
# # # # # #
# """

# n = int(input("enter limit: "))
# for i in range (1, n+1):
#     print("#" * i)


# #### Apa hasil keluaran dari kode berikut?
# d = {"a": 1, "b": 2}
# print(d.get("c", 3))

# #### Apa hasil keluaran dari kode berikut?
# x, y = 7, 12
# x, y, x = x + 6, y + 7, x + 10
# print(x, y)

# for i in range(1, 6):
#      print("# " * i)
