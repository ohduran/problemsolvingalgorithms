from stack import Stack


def dec_to_bin_divide_by_base(number, base):
    """Keep track of the digits for the binary result."""
    s = Stack()
    while number > 0:
        rem = number % base
        s.push(rem)
        number = number // base

    binary_string = ""
    while not s.is_empty():
        binary_string = binary_string + str(s.pop())
    return binary_string
