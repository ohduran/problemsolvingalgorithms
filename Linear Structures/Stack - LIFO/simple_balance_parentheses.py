from stack import Stack


def basic_par_checker(symbol_string):
    """
    Each opening symbol
    must have a corresponding closing symbol.

    If a symbol is an opening parenthesis,
    push it on the stack as a signal that
    the closing symbol must appear later.
    If a closing symbol appears, pop the stack.

    If at any time there is no opening symbol on the Stack
    to match a closing symbol that has just appear, the string
    is not balanced.
    """
    s = Stack()
    index = 0
    while index < len(symbol_string):
        symbol = symbol_string[index]
        if symbol == "(":
            s.push(symbol)
        elif symbol == ")":
            if s.is_empty():
                return False
            s.pop()

        index += 1
    return s.is_empty()


# print(par_checker('((()))'))
# print(par_checker('(((()))'))
