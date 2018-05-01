from queue import Queue


def hot_potato(names, num):
    """
    Input a list of names,
    and the num to be used for counting.
    It returns the name of the last person
    remaining after repetitive counting by num.
    Upon passing the potato, the simulation
    will deque and immediately enqueue that person.
    """
    q = Queue()
    for name in names:
        q.enqueue(name)
        count = 0
    while q.size() > 1:

        top = q.dequeue()
        if count == num:
            count = 0
        else:
            count += 1
            q.enqueue(top)

    return q.dequeue()
