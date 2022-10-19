import unittest
from algo import *

class TestMethods(unittest.TestCase):
    def test_generate_numeric_tokens(self):
        input = 'BC_A'
        tokens = generate_numeric_tokens(input)
        expected = [2, 3, 4, 1]
        self.assertEqual(tokens, expected)

    def test_build_map(self):
        input = [1, 4, 3, 2]
        letter_map = build_map(input)
        expected = {0: 'A', 1: 'B', 2: 'C', 3: '_'}
        self.assertEqual(letter_map, expected)

        input = [3, 1, 2]
        letter_map = build_map(input)
        expected = {0: 'A', 1: 'B', 2: '_'}
        self.assertEqual(letter_map, expected)

if __name__ == '__main__':
    unittest.main()