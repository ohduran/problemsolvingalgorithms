"""Stack class."""


class Stack():
    """Stack class - LIFO Linear Structure."""

    def __init__(self):
        """Define Stack."""
        self._items = []

    def push(self, item):
        """Add a new item on the stack."""
        self._items.append(item)  # O(1)

    def pop(self):
        """
        Remove the last added item.
        Return that item.
        """
        # return self._items.pop()  # O(1)
        item = self._items[-1]
        self._items = self._items[:len(self._items) - 1]
        return item

    def peek(self):
        """
        Return the last item from the Stack
        but does not remove it.
        """
        return self._items[-1]

    def is_empty(self):
        """Return True if items is empty."""
        # return self._items == []
        return len(self._items) == 0

    def size(self):
        """Return the number of items on the Stack."""
        return len(self._items)
