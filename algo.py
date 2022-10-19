import itertools
from utility import to_cycles

def generate_numeric_tokens(s):
    tokens = [ord(c) - 64 for c in s]
    max_index = tokens.index(max(tokens))
    tokens[max_index] = len(tokens)
    return tokens

def remove_cycle(arr, cycle):
    special = max(arr)
    if special not in cycle:
    	cycle.sort()
    	for c in cycle:
    		apply_movement_number(arr, c, special)
    		# print(map_to_letters(arr))
    	apply_movement_number(arr, cycle[0], special)
    	# print(map_to_letters(arr))
    else:
    	special_index = cycle.index(special)
    	# print("Special cycle:	", cycle)
    	cycle = cycle[special_index:] + cycle[:special_index]
    	# print("Rotated cycle:	", cycle)
    	for i in range(len(cycle) - 1, 0, -1):
    	    apply_movement_number(arr, cycle[i], special)
    	    # print(map_to_letters(arr))
    	    # print(arr)

def remove_all_cycles(arr, cycles):
    for i, cycle in enumerate(cycles):
        if len(cycle) == 1:
            continue
        remove_cycle(arr, cycle)

def apply_movement_number(arr, start_number, end_number):
    start_index = arr.index(start_number)
    end_index = arr.index(end_number)
    print(f"{start_index},{end_index}")
    apply_movement(arr, start_index, end_index)
    print(map_to_letters(arr))


def apply_movement(arr, start_index, end_index):
    arr[end_index], arr[start_index] = arr[start_index], arr[end_index]

def map_to_letters(arr):
    d = build_map(arr)
    result = [d[x-1] for x in arr]
    return result

def build_map(arr):
    arr_len = len(arr)
    d = {i : chr(i + ord('A')) for i in range(arr_len)}
    d[arr_len - 1] = '_'
    return d

def find_shortest_path(input, debug = False):
    numeric_tokens = generate_numeric_tokens(input)
    cycles = to_cycles(numeric_tokens)
    remove_all_cycles(numeric_tokens, cycles)





