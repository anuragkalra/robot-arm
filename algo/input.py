def validate_ordering_input(s):
    tokens = [c for c in s]
    tokens.sort()
    s_len = len(s)
    temp = []
    for i in range(s_len):
        temp.append(chr(i + ord('A')))
    temp[len(temp) - 1] = '_'
    if temp != tokens:
    	print("Error: Invalid token input")
    	return False
    return True

#True flags: True, true, TRUE, debug=True
#False flags: False, false, FALSE, debug=false
def validate_debug_input(s):
    if s == "True" or s == "true" or s == "TRUE" or s == "debug=True":
        return 1
    if s == "False" or s == "false" or s == "FALSE" or s == "debug=False":
        return 2
    else:
        print("Error: Invalid debug flag")
        return 3