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
    	run_program(sys.argv[2], False)
    #     debug_flag = sys.argv[1]
    #     print(debug_flag)
    #     if validate_debug_input(debug_flag) == 1 or validate_debug_input(debug_flag) == 2:
    #     	print("dflag = ", debug_flag)
    #     	run_program(sys.argv[2], debug_flag)
    #     # if validate_ordering_input == 3:

    # if n > 3:
    # 	print("received too many arguments")

def run_program(ordering_flag, debug_flag):
    if debug_flag:
        print("Running debug mode...")
    else:
        print("Running standard mode...")
    find_shortest_path(ordering_flag, debug_flag)

if __name__ == '__main__':
    main()