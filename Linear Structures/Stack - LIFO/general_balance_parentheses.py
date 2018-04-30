from stack import Stack


def general_par_checker(symbol_string):
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

    General case accounts for {, [, (   -- types of symbols match as well.
    """
    s = Stack()
    index = 0
    while index < len(symbol_string):
        symbol = symbol_string[index]
        if symbol in "([{":
            s.push(symbol)
        elif symbol in ")]}":
            if s.is_empty():
                return False
            top = s.pop()
            if not matches(top, symbol):
                return False

        index += 1
    return s.is_empty()


def matches(open, close):
    """Open and close symbol must match."""
    opens = '[{('
    closes = ']})'

    return opens.index(open) == closes.index(close)
