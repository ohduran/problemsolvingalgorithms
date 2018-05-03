from stack import Stack


def to_str_stack(number, base):
    """Convert number to string in a given base."""
    s = Stack()
    convert_string = "0123456789ABCDEF"
    while number > 0:
        # base case
        if number < base:
            s.push(convert_string[number])
        # recursion
        else:
            s.push(convert_string[number % base])
        number = number // base
    res = ''
    while not s.is_empty():
        res = res + str(s.pop())
    return res
