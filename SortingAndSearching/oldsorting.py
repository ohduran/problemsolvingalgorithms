# coding=utf-8
import random
import time


def f_insert(new_index, old_index, l):
    # Only works if new_index < old_index
    l2 = []
    length = len(l)
    x = 0
    while x < length:
        if x != new_index:
            l2.append(l[x])
            x += 1
        else:
            l2.append(l[old_index])
            count = 1
            for y in range(new_index + 1, old_index):
                l2.append(l[y])
                count += 1
            l2.append(l[new_index])
            x += count + 1
    return l2


def f_merge(arr1, arr2):
    # asume both lists are sorted
    l2 = []
    length = len(arr2) + len(arr1)
    while len(l2) < length:
        i = 0
        j = 0
        if len(arr1) == 0:
            l2 = l2 + arr2[j::]
            return l2
        elif len(arr2) == 0:
            l2 = l2 + arr1[i::]
            return l2
        elif arr1[i] < arr2[j]:
            l2.append(arr1[i])
            del arr1[0]
        else:
            l2.append(arr2[j])
            del arr2[0]
    return l2


def selection_sort(arr):
    # Set our timer
    selection_start = time.time()
    # Avoid calculating length by storing it in memory
    n = len(arr)
    # for each position in the list
    for i in xrange(0, n):
        # set the minimum element to be the first, and build the iteration from here
        mini = arr[i]
        # from the i´th element until the end
        for j in xrange(i, n):
            # if the current is less than the current minimum, set the minimum as the current
            mini = min(mini, arr[j])
        # take the index of the minimum element
        aa = arr.index(mini)
        # and thus swap the min element with the i´th
        arr[i], arr[aa] = arr[aa], arr[i]
    # print the time for comparison purposes
    print "Selection: Time elapsed: ", time.time() - selection_start
    return arr


def bubble_sort(arr):
    # Set our timer
    bubble_start = time.time()
    # Avoid calculating length by storing it in memory
    n = len(arr)
    # Set the swap counter to 10 to start the while loop
    swaps = 10
    # while we have swapped on the last iteration
    while swaps > 0:
        # Set the swaps counter to 0
        swaps = 0
        # Start the iteration
        for i in xrange(0, n - 1):
            # if the i´th and the next one are not sorted
            if arr[i + 1] < arr[i]:
                # Swap
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # Set the counter of swaps +1
                swaps += 1
    # print the time for comparison purposes
    print "Bubble: Time elapsed: ", time.time() - bubble_start
    return arr


def insertion_sort(arr):
    # Set our timer
    insertion_start = time.time()
    # Avoid calculating length by storing it in memory
    n = len(arr)
    # And we iterate
    for i in xrange(0, n - 1):
        # assume the first i´th element sublist is sorted, and insert the new one
        for j in xrange(0, i + 1):
            # If the first element outside the sublist is less than the j´th element, take its place
            if arr[i + 1] < arr[j]:
                arr = f_insert(j, i + 1, arr)

    # print the time for comparison purposes
    print "Insertion: Time elapsed: ", time.time() - insertion_start
    return arr


def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return arr
    elif n % 2 == 0:
        a = arr[0:n / 2:]
        b = arr[n / 2::]
        return f_merge(merge_sort(a), merge_sort(b))
    elif n % 2 != 0:
        a = arr[0:(n - 1) / 2:]
        b = arr[(n - 1) / 2::]
        return f_merge(merge_sort(a), merge_sort(b))

# N = 10000
# a = [int(round(random.random() * 100, 0)) for x in xrange(N)]

# selection_sort(a)
# bubble_sort(a)
# insertion_sort(a)
# merge_sort(a)
