def generate_numeric_tokens(s, debug = False):
    tokens = [ord(c) - 64 for c in s]
    max_index = tokens.index(max(tokens))
    tokens[max_index] = len(tokens)
    if debug:
        print("Numeric Tokens:  ", tokens)
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
    if debug:
        print("Input:   ", input)
    numeric_tokens = generate_numeric_tokens(input, debug)
    cycles = to_cycles(numeric_tokens, debug)
    remove_all_cycles(numeric_tokens, cycles)

def to_cycles(perm, debug = False):
    pi = {i + 1: perm[i] for i, _ in enumerate(perm)}
    cycles = []
    while pi:
        elem = next(iter(pi))
        this_elem = pi[elem]
        next_item = pi[this_elem]
        cycle = []
        while True:
            cycle.append(this_elem)
            del pi[this_elem]
            this_elem = next_item
            if next_item in pi:
                next_item = pi[next_item]
            else:
                break
        cycles.append(cycle)
    if debug:
        print("Cycles:  ", cycles)
    return cycles

