import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)

    from search.linearSearch import LinearSearch
    from search.binarySearch import BinarySearch
    mylist = [6,9,12,17,19,28,31,38]
    print("Berikut list:", mylist)
    position = LinearSearch.search(mylist, 28)
    print("Element 28 at position:", position)
    position = BinarySearch.search(mylist, 28)
    print("Element 28 at position:", position)

