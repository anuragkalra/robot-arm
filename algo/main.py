import sys
from algo import *
from input import *

# print("Running standard mode...")
# find_shortest_path(input)

# print("Running debug mode...")
# moves = find_shortest_path(input, debug=True)
# print(moves)
# find_shortest_path(input)

#BC_A
#true BC_A

def main():
    # input = 'BC_A'
    # print("Running standard mode...")
    # find_shortest_path(input)
    n = len(sys.argv)
    # print(n)
    if n == 2:
    	ordering_flag = sys.argv[1]
    	if validate_ordering_input(ordering_flag):
    		run_program(ordering_flag, False)
    # if n == 3:
    # 	debug_flag = sys.argv[1]
    # 	ordering_flag = sys.argv[2]
    # 	if validate_debug_input(debug_flag) and validate_ordering_input(ordering_flag):
    # 		run_program(ordering_flag, debug_flag)

def run_program(ordering_flag, debug_flag):
    if debug_flag:
        print("Running debug mode...")
    else:
        print("Running standard mode...")
    find_shortest_path(ordering_flag, debug_flag)

if __name__ == '__main__':
    main()