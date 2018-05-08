import unittest
from what_is_recursion import list_sum, factorial, to_str, is_palindrome
from towersofhanoi import tower_of_hanoi
from maze import Maze


class TestWhatIsRecursion(unittest.TestCase):
    """Test What is Recursion functions."""

    def test_list_sum(self):
        """Test list_sum function."""
        self.assertEqual(list_sum([1, 2, 3]), 6)
        self.assertEqual(list_sum([1, 3, 5, 7, 9]), 25)

    def test_factorial(self):
        """Test factorial function."""
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(3), 6)

    def test_to_str(self):
        """Test to_str function."""
        self.assertEqual(to_str(1453, 10), '1453')
        self.assertEqual(to_str(1453, 16), '5AD')

    def test_is_palindrome(self):
        """Test is_palindrome function."""
        self.assertFalse(is_palindrome('palindrome'))
        self.assertTrue(is_palindrome('madam'))
        self.assertTrue(is_palindrome(
                'Reviled did I live, said I, as evil I did deliver'))
        self.assertTrue(is_palindrome(
                'Able was I ere I saw Elba'))


class TestStackFrames(unittest.TestCase):
        """Test stackframes module."""

        def test_to_str(self):
            """Test to_str function."""
            self.assertEqual(to_str(1453, 10), '1453')
            self.assertEqual(to_str(1453, 16), '5AD')


class TestTowerOfHanoi(unittest.TestCase):
        """Test Tower of Hanoi."""

        def test_n(self):
                """Test n."""
                for n in range(1, 10):
                        moves = tower_of_hanoi(n, "a", "b", "c")
                        self.assertEqual(len(moves), 2**n - 1)

        def test_3(self):
            """Test 3."""
            moves = tower_of_hanoi(3, "a", "b", "c")
            len_moves = 2**3 - 1
            expected_moves = [
                ['a', 'b'],
                ['a', 'c'],
                ['b', 'c'],
                ['a', 'b'],
                ['c', 'a'],
                ['c', 'b'],
                ['a', 'b']
            ]

            self.assertEqual(len(moves), len_moves)
            self.assertEqual(moves, expected_moves)


class TestMaze(unittest.TestCase):
        """Maze tests."""

        def test_1(self):
                """Test instantiation method for Maze class."""
                m = Maze(maze_file_name='Recursion/maze.txt')

                maze_list = m.maze
                columns = m.columns
                self.assertTrue(isinstance(maze_list, list))
                print(maze_list)
                print(columns)


if __name__ == '__main__':
    unittest.main()
