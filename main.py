import time 
import argparse
import ast
from complexity.example import contoh
from search.linearSearch import LinearSearch
from search.binarySearch import BinarySearch
from search.hashSearch import HashSearch

def parse_input(input_str):
    try:
        #validasi inputnya
        input_list = ast.literal_eval(input_str)
        if not isinstance(input_list, list):
            raise ValueError
        return input_list
    except (ValueError, SyntaxError):
        raise argparse.ArgumentTypeError(f"Invalid list input: {input_str}")

def main ():
    parser = argparse.ArgumentParser(description="mengukur algorithm runtime.")
    parser.add_argument('algorithm', help='nama algorithm', choices=['linear_search', 'binary_search', 'hash_search','examples'])
    parser.add_argument('--in_data', type=parse_input, help='Input list in Python list format, e.g., "[1, 2, 3]"')
    parser.add_argument('--target', type=int, help='Target number for search algorithms')
    args = parser.parse_args()

    if args.algorithm == 'linear_search':
        if args.in_data is not None and args.target is not None:
            searcher = LinearSearch()
            result = searcher.search(args.in_data, args.target)
            print("Linear Search")
            print("Input: {}".format(args.in_data))
            print("Target: {}".format(args.target))
            print("Found at index: {}".format(result))
    elif args.algorithm == 'binary_search':
        if args.in_data is not None and args.target is not None:
            searcher = BinarySearch()
            result = searcher.search(args.in_data, args.target)
            print("Binary Search")
            print("Input: {}".format(args.in_data))
            print("Target: {}".format(args.target))
            print("Found at index: {}".format(result))
    elif args.algorithm == 'hash_search':
        if args.in_data is not None and args.target is not None:
            searcher = HashSearch()
            result = searcher.search(args.in_data, args.target)
            print("Hash Search")
            print("Input: {}".format(args.in_data))
            print("Target: {}".format(args.target))
            print("Found at index: {}".format(result))
    elif args.algorithm == 'examples':
        if args.in_data is not None:
            ex = contoh(args.in_data)
            ex.access_element(2)
            ex.find_max()
            ex.binary_search(3)
            ex.bubble_sort()
            ex.sum_triplets()

if __name__ == "__main__":

    main()

    # arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    # ex = contoh(arr)
    
    # index_to_access = 2
    # t1 = time.time()
    # t_constant = ex.access_element(index_to_access)
    # t2 = time.time()
    # t_exec = t2 - t1

    # print("Running time of t_constant: {}".format(t_exec))




