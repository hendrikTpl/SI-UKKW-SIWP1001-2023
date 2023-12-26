import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)

from search.linearSearch import Linear_Search
from search.binarySearch import BinarySearch
mylist = [2,3,5,8,9,12,14,15,18,20]
print("Given list is:", mylist)
position = Linear_Search.search(mylist, 12)
print("Element 12 at position:", position)
position = BinarySearch.search(mylist, 12)
print("Element 12 at position:", position)