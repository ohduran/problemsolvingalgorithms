from queue import Queue
from printingtasks import Printer, Task, has_task_been_created
import random


def simulation(seconds, pages_per_minute):
    """Define simulation."""
    printer = Printer(pages_per_minute)
    queue = Queue()
    waiting_times = []

    for current_second in range(seconds):

        if has_task_been_created():
            task = Task(current_second)
            queue.enqueue(task)

        if (not printer.is_busy()) and (not queue.is_empty()):
            next_task = queue.dequeue()
            waiting_times.append(next_task.waiting_time(current_second))
            printer.start_next_task(next_task)

        printer.tick()
    average_wait = sum(waiting_times) / len(waiting_times)
    return average_wait, queue.size()


for i in range(10):
    print(simulation(3600, 5))
