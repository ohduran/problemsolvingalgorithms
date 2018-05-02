from dequeue import Dequeue


def palindrome_checker(word):
    """Return True if word reads the same forward and backward."""
    d = Dequeue()
    for character in word:
        d.add_rear(character)
    backwards = "".join([d.remove_rear() for character in word])

    if word == backwards:
        return True
    return False
