"""Sorting algorithms."""


def bubble_sort(a_list):
    """Bubble Sort algorithm."""
    for item in reversed(range(len(a_list))):
        for i in range(item):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
    return a_list
