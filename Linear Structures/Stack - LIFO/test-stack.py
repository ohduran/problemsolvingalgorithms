import unittest
from stack import Stack
from simple_balance_parentheses import basic_par_checker
from general_balance_parentheses import general_par_checker
from convertdecimalstobinary import dec_to_bin_divide_by_2
from convertdecimalstobase import dec_to_bin_divide_by_base

class TestStack(unittest.TestCase):
    """Test the Stack class."""

    def test_isempty(self):
        """Test that a stack is empty upon instantiation."""
        s = Stack()
        self.assertTrue(s.is_empty())

    def test_push(self):
        """Test that push inserts an item on the stack."""
        s = Stack()
        s.push(item='hello')
        self.assertTrue(len(s._items) == 1)
        self.assertEqual(s._items, ['hello'])

    def test_pop(self):
        """
        Test that pop removes the last item
        and returns it as a variable.
        """
        variable_1 = 'hello'
        variable_2 = 'world'
        s = Stack()
        s.push(variable_1)
        s.push(variable_2)
        self.assertEqual(s._items, [variable_1, variable_2])

        result = s.pop()
        self.assertEqual(s._items, [variable_1])
        self.assertEqual(result, variable_2)

    def test_peek(self):
        """Test that peek returns the last added item."""
        s = Stack()
        variable = 'hello'
        s.push(variable)
        result = s.peek()

        self.assertEqual(variable, result)

    def test_size(self):
        """Test that size returns the size of the stack."""
        s = Stack()
        s.push('hello')
        size = s.size()
        self.assertEqual(size, len(s._items))


class TestSimpleBalanceParentheses(unittest.TestCase):
        """Test Simple Balance Parentheses."""

        def test_1(self):
                """Test 1."""
                self.assertTrue(basic_par_checker('((()))'))

        def test_2(self):
                """Test 2."""
                self.assertFalse(basic_par_checker('(((()))))'))


class TestGeneralBalanceParentheses(unittest.TestCase):
        """Test General Balance Parentheses."""

        def test_1(self):
                """Test 1."""
                self.assertTrue(general_par_checker('()'))

        def test_2(self):
                """Test 2."""
                self.assertTrue(general_par_checker('{{([][])}()}'))


class TestConvertDecimalstoBinary(unittest.TestCase):
        """Test Convert Decimals to Binary."""

        def test_1(self):
                """Test 1."""
                self.assertEqual(dec_to_bin_divide_by_2(2), '10')

        def test_2(self):
                """Test 2."""
                self.assertEqual(dec_to_bin_divide_by_2(42), '101010')


class TestConvertDecimalstoBase(unittest.TestCase):
        """Test Convert Decimals to Base."""

        def test_1(self):
                """Test 1."""
                self.assertEqual(dec_to_bin_divide_by_base(42, 2), '101010')

        def test_2(self):
                """Test 2."""
                self.assertEqual(dec_to_bin_divide_by_base(25, 16), '19')



if __name__ == '__main__':
    unittest.main()
