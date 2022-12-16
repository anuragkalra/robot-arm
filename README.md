# Description

This python program simulates a robot arm moving containers between holders. The program relies on an installation of python3. The core method, ```find_shortest_path``` returns a python List which contains the sequence of moves that a robot arm can take to bring the containers to a sorted order.

This program provides a command-line-interace which allows for two options:

### Single option: ordering_flag
```python3 main.py 'BC_A'```
Passing only an ordering will run the program in standard (non-debug) mode.
Invalid ordering_flag option will lead to an error message and program exit.

### Two options: debug_flag, ordering_flag
```python3 main.py true 'BC_A'```
debug_flag can take values of 'True', 'true', 'TRUE', 'debug=True' or 'False', 'false', 'FALSE', 'debug=False'
Invalid debug_flag option will lead to to an error message and program exit.
Running in debug mode will show additional logging to demonstrate the state of the algorithm.

### Example program execution
```
cd main
python3 main.py 'BC_A'
1,2
0,1
3,0
```
```
python3 main.py 'BC_S'
Error: Invalid token input
```
```
python3 main.py true 'BC_A'
Running debug mode...
Input:    BC_A
Numeric Tokens:   [2, 3, 4, 1]
Cycles:   [[2, 3, 4, 1]]
Removing Cycle:   [2, 3, 4, 1]
1,2
['B', '_', 'C', 'A']
0,1
['_', 'B', 'C', 'A']
3,0
['A', 'B', 'C', '_']
```
```
python3 main.py false 'BC_A'
1,2
0,1
3,0
```

### Testing
```
cd tests
python3 test_algo.py -b
......
----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```
