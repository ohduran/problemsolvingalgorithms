def list_sum(numbers):
    """Sum all the numbers in a list."""
    # base case
    if len(numbers) == 1:
        return numbers[0]
    # recursion
    else:
        return numbers[0] + list_sum(numbers[1:])


def factorial(number):
    """Return number * (number -1) * ... 1"""
    # base case
    if number == 0:
        return 1
    # recursion
    else:
        return number * factorial(number - 1)


def to_str(n, base):
    """Convert an integer n to a string in any base."""
    if base > 16:
        raise Exception('This won\'t work for a base bigger than 16')
    convert_string = "0123456789ABCDEF"

    # base case
    if n < base:
        return convert_string[n]
    # recursion
    else:
        digit = n % base  # the remainder of dividing by base is the current digit
        new_n = n / base  # recursively look at the all remainding digits.
        return to_str(new_n, base) + convert_string[digit]


def is_palindrome(palindrome_candidate):
    """Return True if the string is a palindrome."""
    # remove whitespaces
    palindrome_candidate = ''.join(palindrome_candidate.split(' '))
    palindrome_candidate = ''.join(palindrome_candidate.split(','))
    palindrome_candidate = ''.join(palindrome_candidate.split('.'))
    palindrome_candidate = ''.join(palindrome_candidate.split(';'))
    palindrome_candidate = palindrome_candidate.lower()
    # base case
    if len(palindrome_candidate) == 1:
        return True
    elif len(palindrome_candidate) == 2:
        if palindrome_candidate[0] == palindrome_candidate[-1]:
            return True
        return False
    # recursion
    else:
        if palindrome_candidate[0] == palindrome_candidate[-1]:
            return is_palindrome(palindrome_candidate[1:-1:])
        return False
