"""
Tower of Hanoi:
Transfer a number of disks from one of the three poles to another,
with two important constraints:
    1. You could only move one disk at a time.
    2. You could never place a larger disk on top of a smaller one.

Peg 1                   Peg 2                   Peg 3
from_pole          with_pole          to_pole

Outline of how to move a tower of height=height
from the starting pole to the goal pole:

    1. Move a tower of height -1 to an intermediate pole, using the final pole.
    2. Move the remaining disk to the final pole.
    3. Move the tower of height -1 from the intermediate pole to the final pole
        using the original pole.
"""


def move_disk(from_pole, to_pole, moves):
    """Express the movement of the disk."""
    # print("Moving disk from ", from_pole, " to ", to_pole)
    moves.append([from_pole, to_pole])


def move_tower(height, from_pole, to_pole, with_pole, moves):
    """Recursively apply Tower of Hanoi strategy."""
    if height > 0:
        move_tower(height - 1, from_pole, with_pole, to_pole, moves)
        move_disk(from_pole, to_pole, moves)
        move_tower(height - 1, with_pole, to_pole, from_pole, moves)


def tower_of_hanoi(height, pole1, pole2, pole3):
    """Return the moves to solve a tower of hanoi of height=height."""
    moves = []
    move_tower(height, pole1, pole2, pole3, moves)
    return moves
