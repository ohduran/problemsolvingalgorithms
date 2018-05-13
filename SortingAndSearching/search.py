"""Search methods."""


def sequential_search(a_list, item):
    """
    Use sequential search to find an item in a_list.

    Case            Best       Worst        Average
    True            1               n               n/2
    False           n               n               n
    """
    pos = 0
    while pos < len(a_list):
        if a_list[pos] == item:
            return True
        else:
            pos += 1

    return False


def ordered_sequential_search(a_list, item):
    """
    Assuming the list is ordered, use sequential search.

    Case            Best       Worst        Average
    True            1               n               n/2
    False           1               n               n/2
    """
    pos = 0
    looked_item = a_list[pos]
    while looked_item <= item:
        if looked_item == item:
            return True
        else:
            pos += 1
            looked_item = a_list[pos]
    return False


def binary_search(a_list, item):
    """
    Assuming that the list is ordered,
    go to position n/2 and check.
    If not there, recursively search in the subset list
    that results on dividing a_list in 2
    and take only the one where item might be (by compared to a_list[n/2])
    """
    first = 0
    last = len(a_list) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return False
