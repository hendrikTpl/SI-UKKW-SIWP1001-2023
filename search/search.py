class Search:
    @staticmethod
    def ls(list, target):
        for i in range(len(list)):
            if list[i] == target:
                return f"Target {target} is found at {i+1}"
        return "Target not found"

    @staticmethod
    def bs(list, target):
        list.sort()
        low = 0
        high = len(list) - 1

        while low <= high:
            mid = (low + high) // 2
            if list[mid] == target:
                return f"Target {target} found at {mid+1}"
            elif list[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return "Target not found"

# list = [5,2,3,1,6,7,4,8]
# target = 4

# ls = Search.ls(list, target)
# bs = Search.bs(list, target)
# print(ls)
# print(bs)