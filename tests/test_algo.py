import unittest
import sys
sys.path.insert(0, '../algo')
import algo

class TestMethods(unittest.TestCase):
    def test_generate_numeric_tokens(self):
        input = 'BC_A'
        tokens = algo.generate_numeric_tokens(input)
        expected = [2, 3, 4, 1]
        self.assertEqual(tokens, expected)

    def test_build_map(self):
        input = [1, 4, 3, 2]
        letter_map = algo.build_map(input)
        expected = {0: 'A', 1: 'B', 2: 'C', 3: '_'}
        self.assertEqual(letter_map, expected)

        input = [3, 1, 2]
        letter_map = algo.build_map(input)
        expected = {0: 'A', 1: 'B', 2: '_'}
        self.assertEqual(letter_map, expected)

    def test_to_cycles(self):
    	input = [2, 1, 4, 3]
    	cycles = algo.to_cycles(input)
    	expected = [[2, 1],[4, 3]]
    	self.assertEqual(cycles, expected)

    	input = [2, 3, 4, 1]
    	cycles = algo.to_cycles(input)
    	expected = [[2, 3, 4, 1]]
    	self.assertEqual(cycles, expected)

    def test_apply_movement(self):
    	arr = [1, 2, 3]
    	start_index = 0
    	end_index = 2
    	algo.apply_movement(arr, start_index, end_index)
    	expected = [3, 2, 1]
    	self.assertEqual(arr, expected)

    	arr = [1, 2, 3]
    	start_index = 2
    	end_index = 0
    	algo.apply_movement(arr, start_index, end_index)
    	expected = [3, 2, 1]
    	self.assertEqual(arr, expected)

    def test_apply_movement_number(self):
    	arr = [1, 2, 3]
    	start_number = 2
    	end_number = 3
    	moves = []
    	algo.apply_movement_number(arr, start_number, end_number, moves)
    	expected = [1, 3, 2]
    	self.assertEqual(arr, expected)

    	arr = [1, 2, 3]
    	start_number = 3
    	end_number = 1
    	moves = []
    	algo.apply_movement_number(arr, start_number, end_number, moves)
    	expected = [3, 2, 1]
    	self.assertEqual(arr, expected)

    def test_find_shortest_path(self):
    	input = 'BC_A'
    	moves = algo.find_shortest_path(input)
    	expected = [[1, 2], [0, 1], [3, 0]]
    	self.assertEqual(moves, expected)

    	input = 'A_CB'
    	moves = algo.find_shortest_path(input)
    	expected = [[3, 1]]
    	self.assertEqual(moves, expected)    	


if __name__ == '__main__':
    unittest.main()
