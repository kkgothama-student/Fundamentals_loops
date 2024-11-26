# test_exercise.py

import unittest
from exercise import *

class TestExercise(unittest.TestCase):

    def test_sum_with_while(self):
        self.assertEqual(sum_with_while(1, 5), 15)
        self.assertEqual(sum_with_while(-3, 3), 0)

    def test_count_vowels_in_string(self):
        self.assertEqual(count_vowels_in_string("hello"), 2)
        self.assertEqual(count_vowels_in_string("HELLO"), 2)
        self.assertEqual(count_vowels_in_string("xyz"), 0)

    def test_filter_numbers(self):
        self.assertEqual(
            filter_numbers([1, -1, 2, -2, 0]),
            {
                'positive': [1, 2],
                'negative': [-1, -2],
                'even': [2, -2, 0],
                'odd': [1, -1]
            }
        )

    def test_fibonacci_sequence(self):
        self.assertEqual(fibonacci_sequence(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci_sequence(0), [])
        self.assertEqual(fibonacci_sequence(1), [0])

    def test_pascals_triangle(self):
        self.assertEqual(
            pascals_triangle(4),
            [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1]
            ]
        )

    def test_tower_of_hanoi(self):
        self.assertEqual(
            tower_of_hanoi(3, 'A', 'C', 'B'),
            [
                "Move disk 1 from A to C",
                "Move disk 2 from A to B",
                "Move disk 1 from C to B",
                "Move disk 3 from A to C",
                "Move disk 1 from B to A",
                "Move disk 2 from B to C",
                "Move disk 1 from A to C"
            ]
        )

    def test_find_dna_sequence(self):
        self.assertEqual(find_dna_sequence("ACGTACGTGACG", "TAC"), 2)
        self.assertEqual(find_dna_sequence("ACGTACGTGACG", "TAG"), -1)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))
        self.assertFalse(is_palindrome("hello"))

    def test_generate_permutations(self):
        self.assertEqual(
            sorted(generate_permutations("abc")),
            sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        )

    def test_is_valid_sudoku(self):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        self.assertTrue(is_valid_sudoku(board))

    def test_solve_n_queens(self):
        self.assertEqual(
            solve_n_queens(4),
            [
                [".Q..", "...Q", "Q...", "..Q."],
                ["..Q.", "Q...", "...Q", ".Q.."]
            ]
        )

    def test_longest_common_subsequence(self):
        self.assertEqual(longest_common_subsequence("abcde", "ace"), 3)
        self.assertEqual(longest_common_subsequence("abc", "def"), 0)

if __name__ == "__main__":
    unittest.main()
