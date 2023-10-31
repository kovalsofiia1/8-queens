import unittest
import os
from unittest.mock import patch

import my_rbfs as rbfs
import bfs_node as bfs
import common as c

class TestChessboardFunctions(unittest.TestCase):
    def test_is_safe(self):
        # Test case 1: Safe board configuration
        board1 = [1, 3, 0, 2]
        self.assertTrue(c.is_safe(board1))

        # Test case 2: Unsafe board configuration
        board2 = [1, 3, 2, 0]
        self.assertFalse(c.is_safe(board2))

        # Test case 3: Empty board should always be safe
        board3 = []
        self.assertTrue(c.is_safe(board3))

    def test_get_answer(self):
        # Test case 1: User enters one of the valid options
        with unittest.mock.patch('builtins.input', return_value='y'):
            self.assertEqual(c.get_answer("Choose 'y' or 'n': ", 'y', 'n'), 'y')

        # Test case 2: User enters an invalid option first, then a valid one
        with unittest.mock.patch('builtins.input', side_effect=['invalid', 'y']):
            self.assertEqual(c.get_answer("Choose 'y' or 'n': ", 'y', 'n'), 'y')

    def test_get_number_of_range(self):
        # Test case 1: User enters a valid number within the specified range
        with unittest.mock.patch('builtins.input', return_value='5'):
            self.assertEqual(c.get_number_of_range("Enter a number between 1 and 10: ", 1, 10), 5)

        # Test case 2: User enters a number below the minimum
        with unittest.mock.patch('builtins.input', side_effect=[0, 5]):
            self.assertEqual(c.get_number_of_range("Enter a number between 1 and 10: ", 1, 10), 5)

        # Test case 3: User enters a number above the maximum
        with unittest.mock.patch('builtins.input', side_effect=[15, 5]):
            self.assertEqual(c.get_number_of_range("Enter a number between 1 and 10: ", 1, 10), 5)

    def test_get_board(self):
        # Test case 1: User chooses to input queen positions
        with unittest.mock.patch('builtins.input', side_effect=[3, 2, 1, 4]):
            self.assertEqual(c.get_board(4, 'n'), [2, 1, 0, 3])

class TestNQueensRBFSSolver(unittest.TestCase):
    def test_node_creation(self):
        state = [0, 1, 2, 3]  # Example state
        node = rbfs.Node(state)
        self.assertEqual(node.state, state)
        self.assertIsNone(node.parent)
        self.assertEqual(node.g, 0)
        self.assertEqual(node.h, 0)
        self.assertEqual(node.f, 0)

    def test_generate_successors(self):
        state = [0, 1, 2,3]  # Example state
        node = rbfs.Node(state)
        successors = rbfs.generate_successors(node)
        self.assertTrue(isinstance(successors, list))
        self.assertEqual(len(successors), 12)  # There are 12 possible successor states for a 4x4 board

    def test_heuristic_f2(self):
        state = [1, 3, 0, 2]  # Example state with no conflicts
        self.assertEqual(rbfs.heuristic_f2(state), 0)

        state = [1, 0, 3, 3]  # Example state with conflicts
        self.assertEqual(rbfs.heuristic_f2(state), 3)

class TestNQueensBFSSolver(unittest.TestCase):
    def test_node_bfs_creation(self):
        state = [0, 1, 2]  # Example state
        node = bfs.NodeBFS(state)
        self.assertEqual(node.state, state)
        self.assertIsNone(node.parent)

    def test_solve_n_queens_bfs(self):
        # Test case 1: Solve a small board with a known solution
        initial_board = [1, 3, 0, 2]  # A 4x4 board with a known solution
        result = bfs.solve_n_queens_bfs(initial_board)
        self.assertIsNotNone(result)
        self.assertTrue(c.is_safe(result.state))

        # Test case 2: Try to solve an unsolvable board
        initial_board = [0, 0, 0]  # An unsolvable 3x3 board
        result = bfs.solve_n_queens_bfs(initial_board)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()