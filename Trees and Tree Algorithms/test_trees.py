import unittest
import trees
import binaryheap


class TestTrees(unittest.TestCase):
    """Test Trees."""

    def test_binary_tree_root_methods(self):
        """Test the initial behaviour of the Binary Tree."""
        r = trees.BinaryTree('a')
        self.assertEqual(r.get_root_value(), 'a')

        r.set_root_value('hello')
        self.assertEqual(r.get_root_value(), 'hello')

    def test_binary_tree_left_methods(self):
        """Test left child functionality."""
        r = trees.BinaryTree('a')
        self.assertIsNone(r.get_left_child())

        r.insert_left('b')
        self.assertTrue(isinstance(r.get_left_child(), trees.BinaryTree))
        self.assertEqual(r.get_left_child().get_root_value(), 'b')

    def test_binary_tree_right_methods(self):
        """Test right child functionality."""
        r = trees.BinaryTree('a')
        self.assertIsNone(r.get_right_child())

        r.insert_right('c')
        self.assertTrue(isinstance(r.get_right_child(), trees.BinaryTree))
        self.assertEqual(r.get_right_child().get_root_value(), 'c')

    def test_minheap_isempty(self):
        """Test Binary Heap isempty() method"""
        bn = binaryheap.MinHeap()
        # minheap must be initialised empty
        self.assertTrue(bn.is_empty)

    def test_minheap_insert(self):
        bn = binaryheap.MinHeap()

        bn.insert(5)

        self.assertEqual(bn.heap_list, [None, 5])

    def test_minheap_insert_several_values(self):
        bn = binaryheap.MinHeap()

        bn.insert(5)
        bn.insert(11)
        bn.insert(9)
        bn.insert(18)
        bn.insert(14)
        bn.insert(21)
        bn.insert(19)
        bn.insert(17)
        bn.insert(27)
        bn.insert(33)

        expected_result = [None, 5, 11, 9, 17, 14, 21, 19, 18, 27, 33]

        self.assertEqual(expected_result, bn.heap_list)

    def test_minheap_size(self):
        bn = binaryheap.MinHeap()

        bn.insert(5)
        bn.insert(11)
        bn.insert(9)
        bn.insert(18)
        bn.insert(14)
        bn.insert(21)
        bn.insert(19)
        bn.insert(17)
        bn.insert(27)
        bn.insert(33)

        expected_result = 10

        self.assertEqual(expected_result, bn.size)

    def test_build_heap(self):
        """Test build_heap method"""
        expected_result = [None, 5, 11, 9, 17, 14, 21, 19, 18, 27, 33]
        key_list = sorted(expected_result[1:])

        bn = binaryheap.MinHeap().build_heap(key_list)

        self.assertEqual(bn.size, len(key_list))
        self.assertEqual(bn.heap_list, expected_result)

    def test_find_min(self):
        """Test find_min method"""
        bn = binaryheap.MinHeap()

        bn.insert(5)
        bn.insert(7)
        bn.insert(3)
        bn.insert(11)

        expected_result = [3, 5, 7, 11]
        result = [bn.delete_min() for key in range(bn.size)]

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
