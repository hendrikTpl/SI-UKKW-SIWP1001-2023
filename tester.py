import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)

from search.binarySearch import BinarySearch
from search.linearSearch import LinearSearch

nums_1 = [0,1,2,3,4,5,6,7,8,9]
target_1 = 7

print(BinarySearch.binary_search(nums_1, target_1))
print(LinearSearch.linier_search(nums_1, target_1))