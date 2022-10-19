from utility import to_cycles
from algo import *

input = 'BC_A'

print("input:	", input)

numeric_tokens = generate_numeric_tokens(input) #[2, 3, 4, 1]
print("numeric_tokens:	", numeric_tokens)

cycles = to_cycles(numeric_tokens)
print("cycles:	", cycles)

remove_all_cycles(numeric_tokens, cycles)
# print(numeric_tokens)
print("Completed:")
print(map_to_letters(numeric_tokens))

