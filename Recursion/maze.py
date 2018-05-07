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
        Read in a data file representing a maze,
        initializes the internal representation of the maze,
        and finds the starting point of the turtle.
        """
        pass

    def draw_maze(self):
        """Draw the maze in a window on the screen."""
        pass

    def update_position(self):
        """
        Update the internal representation of the Maze
        and change the position of the turtle in the window
        """
        pass

    def leave_breadcrumb(self):
        """Leave a breadcrumb in the current position."""
        pass

    def dead_end(self):
        """Mark the current position as a dead end."""
        pass

    def is_exit(self):
        """Return True if the current position is the EXIT."""
        pass


def search_from(maze, start_row, start_column):
    """Search until we find the exit, recursively."""
    maze.update_position(start_row, start_column)
    # base case 1 - if obstacle, return False
    if maze[start_row][start_column] == OBSTACLE:
        return False
    # base case 2 - if we have been there already, return False
    if maze[start_row][start_column] == BREADCRUMB:
        return False
    # base case 3 - success, and outside edge not occupied by OBSTACLE
    if maze.is_exit(start_row, start_column):
        maze.update_position(start_row, start_column)
        return True

    # recursion
    maze.leave_breadcrumb(start_row, start_column)
    north = search_from(maze, start_row - 1, start_column)
    south = search_from(maze, start_row + 1, start_column)
    east = search_from(maze, start_row, start_column + 1)
    west = search_from(maze, start_row, start_column - 1)

    if north or south or east or west:
        maze.update_position(start_row, start_column)
    else:
        maze.dead_end()
