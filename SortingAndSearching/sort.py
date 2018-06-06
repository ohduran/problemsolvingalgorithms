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
            a_list = insertion_sort(
                a_list,
                start=start_position,
                gap=sublist_count
                )
        sublist_count = sublist_count // 2
    return a_list


def merge_sort(a_list):
    """
    Apply Merge Sort algorithm.

    Merge Sort is a recursive algorithm
    that continually splits a list in half. If
    the list is empty or has one item, it is
    sorted by definition (base case). If
    the list has more than one item, we split
    the list in half and recursively invoke a merge
    sort on both halves.

    Once the two halves are sorted, the
    merge is performed: taking two smaller sorted lists
    and combine them together into a single sorted bigger list.
    """
    if len(a_list) <= 1:
        # a list with one element is sorted by definition
        return a_list
    # apply recursion if length is 2 or more
    else:
        middle_term = len(a_list) // 2
        left_half = a_list[:middle_term]
        right_half = a_list[middle_term:]

        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)

        return merge_lists(left_half, right_half)


def merge_lists(list_1, list_2):
    """Merge two sorted lists into one sorted list."""
    if len(list_1) == 0:
        return list_2
    if len(list_2) == 0:
        return list_1

    new_list = []
    length = len(list_1) + len(list_2)
    while len(new_list) < length:
        if len(list_1) == 0:
            new_list = new_list + list_2
        elif len(list_2) == 0:
            new_list = new_list + list_1

        elif list_1[0] < list_2[0]:
            new_list.append(list_1[0])
            list_1.remove(list_1[0])
        elif list_1[0] >= list_2[0]:
            new_list.append(list_2[0])
            list_2.remove(list_2[0])
    return new_list


def quick_sort(a_list):
    """
    Apply Quick Sort algorithm.

    The first value of the list is the pivot value,
    and it will be used to split the list.

    """
    quick_sort_helper(a_list, 0, len(a_list) - 1)


def quick_sort_helper(a_list, first_position, last_position):
    """Auxiliary function for quick_sort."""
    if first_position < last_position:

        split_point = partition(a_list, first_position, last_position)

        quick_sort_helper(a_list, first_position, split_point - 1)
        quick_sort_helper(a_list, split_point + 1, last_position)


def partition(a_list, first_position, last_position):
    """
    Auxiliary function for quick_sort_helper.
    Return the Split point.
    """
    pivot_value = a_list[first_position]

    left_mark = first_position + 1
    right_mark = last_position

    done = False
    while not done:

        # ignore anything on the left smaller than the pivot value
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark += 1

        # ignore anything on the right bigger than the pivot value
        while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark += 1

        if a_list[right_mark] < a_list[left_mark]:
            # items are in the correct position
            done = True
        else:
            # swap
            a_list[left_mark], a_list[right_mark] = a_list[right_mark], a_list[left_mark]

    # once everything is ordered, move the pivot value to its split point
    a_list[first_position], a_list[right_mark] = a_list[right_mark], a_list[first_position]

    return right_mark


print(quick_sort(A))
