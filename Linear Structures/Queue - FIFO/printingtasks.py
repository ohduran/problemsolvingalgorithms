from queue import Queue
from random import randint


def has_task_been_created():
    """
    Return True if a random number
    between 1 and 180 equals 180.
    (1 task every 180 seconds = 20 task/hour)
    """
    return randint(1, 181) == 180


class Printer():
    """Object that prints Tasks."""

    def __init__(self, ppm):
        """Define constructor."""
        self._ppm = ppm
        self.current_task = None
        self.time_remaining = 0
        self.page_rate = 1

    def tick(self):
        """
        Decrement the internal timer
        and set the printer to idle if task is completed.
        """
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def is_busy(self):
        """Return True if the printer has a current task."""
        if self.current_task is not None:
            return True
        return False

    def start_next_task(self, task):
        self.current_task = task
        self.time_remaining = task.get_pages() * 60 / self.page_rate


class Task():
    """Task to be done."""

    def __init__(self, time):
        """Define constructor."""
        self.timestamp = time
        self.pages = randint(1, 21)

    def get_stamp(self):
        """Return time stamp."""
        return self.timestamp

    def get_pages(self):
        """Return the number of pages."""
        return self.pages

    def waiting_time(self, current_time):
        """Return the time left."""
        return current_time - self.timestamp
