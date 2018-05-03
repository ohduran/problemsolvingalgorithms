class Node:
    """A collection of nodes make up a linked list."""

    def __init__(self, data):
        """Define constructor."""
        self._data = data
        self.next = None  # points to nothing (end of list).

    def set_next(self, new_next):
        """
        By default, the node is the last one in the list.
        Change that using set_next.
        """
        self.next = new_next

    def get_data(self):
        """Return data stored in node."""
        return self._data

    def get_next(self):
        """Get the next Node."""
        return self.next


class UnorderedList:
    """Data Structure built from a collection of nodes."""

    def __init__(self):
        """Define constructor."""
        self.head = None  # initially pointed to nothing (empty)

    def is_empty(self):
        """Check if self is pointing to a Node or not."""
        return self.head is None

    def add(self, item):
        """Add a new item at the front of the list. O(1)"""
        temp = Node(item)

        # the last Node now points to the added Node
        temp.set_next(self.head)

        self.head = temp

    def size(self):
        """Return the size of the linked list. O(n)."""
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        """Return True if item is on the list. O(n)."""
        current = self.head
        while current is not None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def remove(self, item):
        """Remove a Node containing an item on the list. O(n)."""
        if not self.search(item):
            raise Exception('The item wasn\'t found.')

        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        # found, now point previous node to the next,
        # and leave current in limbo.
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


class OrderedList(UnorderedList):
    """
    Ordered List class, a collection of nodes indexed,
    but the numbers inside must be in order.

    Inherits __init__, is_empty, size and remove from UnorderedList.
    """

    def search(self, item):
        """Return True if the item is on the list. O(n)."""
        current = self.head
        while current is not None:
            if current.get_data() == item:
                return True
            else:
                if current.get_data() > item:
                    return False
                current = current.get_next()
        return False

    def add(self, item):
        """Add a new item on the correct position."""
        current = self.head
        previous = None
        stop = False

        while current is not None and not stop:
            if current.get_data > item:
                stop = True  # position found
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous is None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)
