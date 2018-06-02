"""Sorting algorithms."""


def bubble_sort(a_list):
    """Apply Bubble Sort algorithm."""
    for item in reversed(range(len(a_list))):
        for i in range(item):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
    return a_list


def selection_sort(a_list):
    """Apply Selection Sort algorithm."""
    for slot in reversed(range(len(a_list))):
        pos_of_max = 0
        for location in range(1, slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
        a_list[slot], a_list[pos_of_max] = a_list[pos_of_max], a_list[slot]
    return a_list


def insertion_sort(a_list):
    """Apply Insertion Sort algorithm."""
    for index in range(1, len(a_list)):
        value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > value:
            a_list[position] = a_list[position - 1]

            position -= 1

        a_list[position] = value

    return a_list
