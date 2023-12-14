# varInput = int(input("masukan input array number: "))

# # Initialize an empty  array
# arr = []

# # Get input for each element and store in the list
# for i in range(varInput):
#     value = float(input(f"Enter element {i + 1}: "))  # We use float to allow decimal values
#     arr.append(value)

# # Divide each element by two
# divided_arr = [x/2 for x in arr]

# print("Original Array:", arr)
# print("Divided by Two:", divided_arr)

varInput = input("Input list (comma-separated): ")
varInput = [int(i) for i in varInput.split(',')]

#  index tngahnya
mid = len(varInput) // 2

# potong dua bagian dari panjang list input: listA and listB
listA = varInput[:mid]
listB = varInput[mid:]

print("listA:", listA)
print("listB:", listB)

# TODO
# lakukan logic selanjutnya dengan listA dan listB
# ... 
