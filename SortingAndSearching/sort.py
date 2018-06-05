"""Sorting algorithms."""


A = [15, 5, 4, 18, 12, 19, 14, 10, 8, 20]


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


def insertion_sort(a_list, start=0, gap=1):
    """
    Apply Insertion Sort algorithm.
    With start, it sorts only a_list[a:].
    With gap, it takes jumps of length gap
    between elements of the list.
    """
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position -= gap

        a_list[position] = current_value
    return a_list


def shell_sort(a_list):
    """Apply Shell Sort algorithm."""
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            a_list = insertion_sort(a_list, start=start_position, gap=sublist_count)
        sublist_count = sublist_count // 2
    return a_list


print(shell_sort(A))
