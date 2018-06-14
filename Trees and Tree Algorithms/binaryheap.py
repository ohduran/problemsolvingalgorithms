"""Binary Heap Implementation"""


class BinHeap(object):
    """
    Binary Heap

    Order Property: For every node x with parent p,
    the key in p is smaller than or equal to the key in x.
    """

    def __init__(self):
        """
        Creates a new, empty, binary heap.

        Since the entire binary heap can be represented by a single list,
        all the constructor will do is initialize the list and an attribute
        `current_size`.
        """
        self.heap_list = [None]
        self.current_size = 0

    def gain_heap_structure_property_up(self, position):
        """Percolate a newly added position to its proper position"""
        while position // 2 > 0:
            if self.heap_list[position] < self.heap_list[position // 2]:
                self.swap(position, position // 2)
            position = position // 2

    def gain_heap_structure_property_down(self, position):
        """
        We can restore heap structure by pushing the root
        node down the tree to its proper position.
        """
        while (position * 2) <= self.current_size:
            min_child = self.min_child(position)

            if self.heap_list[position] > self.heap_list[min_child]:
                self.swap(position, min_child)
            position = min_child

    def min_child(self, parent):
        """Obtain the minimum child under parent"""
        if parent * 2 + 1 > self.current_size:
            return parent * 2
        else:
            if self.heap_list[parent * 2] < self.heap_list[parent * 2 + 1]:
                return parent * 2
            else:
                return parent * 2 + 1

    def swap(self, position_a, position_b):
        """Swap two elements' positions."""
        self.heap_list[position_a], self.heap_list[position_b] = self.heap_list[position_b], self.heap_list[position_a]

    @property
    def is_empty(self):
        """Return True if the heap is empty"""
        return self.current_size == 0

    @property
    def size(self):
        """Return the number of positions in the heap"""
        return self.current_size

    def build_heap(self, key_list):
        """
        Builds a new heap from a list of keys.


        """
        i = len(key_list) // 2
        self.current_size = len(key_list)
        self.heap_list = [None] + key_list[:]
        while i > 0:
            self.gain_heap_structure_property_down(i)
            i -= 1
        return self


class MinHeap(BinHeap):
    """Min Heap"""

    def insert(self, position):
        """
        Add a new position to the heap.

        Appending will do the trick, but we need to regain
        structure property by using gain_heap_structure_property()
        """
        self.heap_list.append(position)
        self.current_size += 1

        self.gain_heap_structure_property_up(self.current_size)

    def find_min(self):
        """
        Return the position with the minimum key value,
        leaving the position in the heap.
        """
        if self.current_size > 0:
            return self.heap_list[1]

    def delete_min(self):
        """
        Return the position with the minimum key value,
        and deleting it from the heap.

        Since the heap property requires that the root of the tree
        be the smallest item, finding the minimum key is easy.

        The hard part is restoring full heap structure property.
        To do so, we move the last item to the root, and
        regain heap structure property all the way down.
        """
        if self.current_size > 0:
            min_key_value = self.heap_list[1]
            self.heap_list[1] = self.heap_list[self.current_size]
            self.current_size -= 1
            self.heap_list.pop()
            self.gain_heap_structure_property_down(1)
            return min_key_value
