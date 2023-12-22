# import sys
# import os
# current_script_path = os.path.abspath(_file_)
# project_root = os.path.dirname(os.path.dirname(current_script_path))
# if project_root not in sys.path:
#     sys.path.append(project_root)

from search.search import Search

list = [5,2,3,1,6,7,4,8]
target = 4

ls = Search.linear_search(list, target)
bs = Search.binary_search(list, target)
print(ls)
print(bs)