

class Dequeue():
    """Dequeue abstract data type."""

    def __init__(self):
        """Define constructor."""
        self._items = []

    def add_front(self, item):
        """Add an item at the front of the dequeue."""
        self._items.insert(0, item)

    def remove_front(self):
        """Remove the first item."""
        return self._items.pop(0)

    def add_rear(self, item):
        """Add an item at the front of the dequeue."""
        self._items.append(item)

    def remove_rear(self):
        """Remove item at the end of the dequeue."""
        return self._items.pop()

    def size(self):
        """Return the length of the dequeue."""
        return len(self._items)

    def is_empty(self):
        """Return True if the dequeue is empty."""
        return self._items == []
