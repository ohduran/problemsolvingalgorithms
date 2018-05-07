"""
How do you find your way out of a maze?
- We will assume that our maze is divided up into 'squares'.
- Each square is either open or occupied by a section of wall.
- Turtle can only pass through the open squares of the maze.


Procedure:
- Starting point is going North one square
- If we cannot go Nourth, try South, then West, then East.
- If none is possible, then we failed.

- We must remember where we are coming from to avoid infinite loops.
    - bread crumb: if we have been there before, we can't go there.

4 base cases:
- The turtle has run into a wall
- The turtle has found a bread crumb
- We have found the EXIT
- We have explored a square unsuccesfully in all four directions

"""


class Maze:
    """Will draw the maze for the turtle to walk across."""

    def __init__(self):
        """
        Reads in a data file representing a maze,
        initializes the internal representation of the maze,
        and finds the starting point of the turtle.
        """
        pass
