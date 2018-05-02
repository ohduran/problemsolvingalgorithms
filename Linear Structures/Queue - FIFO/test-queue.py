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

        def test_Printer_new_task(self):
                """Test Printer new_task method."""
                pages_per_minute = 60
                time = 10
                p = Printer(pages_per_minute)
                t = Task(time=time)
                pages = t.get_pages()
                p.start_next_task(t)

                self.assertEqual(p.time_remaining, 60*pages/p.page_rate)
                self.assertEqual(p.current_task, t)

        def test_Printer_isbusy(self):
                """Test isbusy method."""
                pages_per_minute = 60
                time = 10
                p = Printer(pages_per_minute)

                self.assertFalse(p.is_busy())

                t = Task(time=time)
                p.start_next_task(t)

                self.assertTrue(p.is_busy())

        def test_Printer_tick(self):
                """Test Printer tick method."""
                pages_per_minute = 60
                time = 10
                p = Printer(pages_per_minute)
                t = Task(time=time)
                pages = t.get_pages()
                p.start_next_task(t)

                time_remaining = 60*pages/p.page_rate

                self.assertEqual(p.time_remaining, time_remaining)

                p.tick()
                time_remaining -= 1

                self.assertEqual(p.time_remaining, time_remaining)

                while time_remaining > 0:
                        time_remaining -= 1
                        p.tick()

                self.assertIsNone(p.current_task)


if __name__ == '__main__':
    unittest.main()
