from search.search import Search
list = [5,2,3,1,6,7,4,8]
target = 4

ls = Search.ls(list, target)
bs = Search.bs(list, target)
print(ls)
print(bs)