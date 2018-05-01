import unittest
from queue import Queue
from hotpotato import hot_potato
from printingtasks import has_task_been_created, Printer, Task


class TestQueue(unittest.TestCase):
    """Test Queue class."""

    def test_enqueue(self):
        """Enqueue must add a new item at the end of the queue."""
        q = Queue()
        self.assertEqual(len(q._items), 0)
        q.enqueue('hello')
        self.assertEqual(q._items, ['hello'])

    def test_is_empty(self):
        """Test is_empty method."""
        q = Queue()
        self.assertTrue(q.is_empty())
        q._items.append('hello')
        self.assertFalse(q.is_empty())

    def test_dequeue(self):
        """
        dequeue must return the first item on the list.
        And remove it from the list.
        """
        q = Queue()
        q._items.append('hello')
        q._items.append('world')
        q._items.append('hello')
        q.dequeue()
        self.assertEqual(q._items, ['world', 'hello'])

    def test_size(self):
        """Size must return length of the queue."""
        q = Queue()
        q._items.append('hello')
        q._items.append('world')
        q._items.append('hello')
        q._items.append('world')
        self.assertEqual(q.size(), 4)


class TestHotPotato(unittest.TestCase):
        """Test Hot Potato."""

        def test_1(self):
                """Test 1."""
                self.assertEqual(
                        hot_potato(
                                ['Bill',
                                 'David',
                                 'Susan',
                                 'Jane',
                                 'Kent',
                                 'Brad'],
                                7),
                        'Susan'
                )


class TestPrintingQueue(unittest.TestCase):
        """Printing Tasks test."""

        def test_has_task_been_created(self):
                """Test has_task_been_created function."""
                a = has_task_been_created()
                self.assertTrue(isinstance(a, bool))

        def test_Task(self):
                """Test Task class."""
                time = 10
                t = Task(time=time)
                self.assertEqual(t.timestamp, time)
                self.assertTrue(t.pages >= 1)
                self.assertTrue(t.pages <= 21)

        def test_Task_get_stamp(self):
                """Test get_stamp method."""
                time = 10
                t = Task(time=time)
                self.assertEqual(t.get_stamp(), time)

        def test_Task_get_pages(self):
                """Test get_pages method."""
                t = Task(10)
                pages = t.pages
                self.assertEqual(t.get_pages(), pages)

        def test_Task_waiting_time(self):
                """Test waiting_time method."""
                time = 10
                t = Task(time=time)
                current_time = 100
                self.assertEqual(
                        t.waiting_time(current_time),
                        current_time - time)

        def test_Printer(self):
                """Test Printer class."""
                pages_per_minute = 60
                p = Printer(pages_per_minute)
                self.assertEqual(p._ppm, pages_per_minute)

        def test_Printer_tick(self):
                """Test Printer tick method."""
                pass



if __name__ == '__main__':
    unittest.main()
