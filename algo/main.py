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
    n = len(sys.argv)
    if n == 2 and validate_ordering_input(sys.argv[1]):
        run_program(sys.argv[1], False)
    if n == 3 and validate_ordering_input(sys.argv[2]):
        debug_flag = sys.argv[1]
        debug_option = validate_debug_input(debug_flag)
        if debug_option == 1:
            run_program(sys.argv[2], True)
        if debug_option == 2:
            run_program(sys.argv[2], False)
    if n > 3:
    	print("Error: received too many arguments")

def run_program(ordering_flag, debug_flag):
    if debug_flag:
        print("Running debug mode...")
    else:
        print("Running standard mode...")
    find_shortest_path(ordering_flag, debug_flag)

if __name__ == '__main__':
    main()