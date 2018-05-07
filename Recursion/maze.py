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
from turtle import Turtle, setup, setworldcoordinates, tracer, update


class Maze:
    """Will draw the maze for the turtle to walk across."""

    def __init__(self, maze_file_name):
        """
        Read in a data file representing a maze,
        initializes the internal representation of the maze,
        and finds the starting point of the turtle.
        """
        self.maze = []
        maze_file = open(maze_file_name, 'r')

        rows = 0
        for line in maze_file:
            row_list = []
            columns = 0
            for square in line[:-1]:
                row_list.append(square)
                if square == 'S':
                    self.start_row = rows
                    self.start_col = columns
                columns += 1
            rows += 1
            self.maze.append(row_list)

        self.rows = rows
        self.columns = columns
        self.x_translate = - columns / 2
        self.y_translate = rows / 2

        self.turtle = Turtle(shape='turtle')

        setup(width=600, height=600)
        setworldcoordinates(
            - (columns - 1) / 2 - .5,
            - (rows - 1) / 2 - .5,
            (columns - 1) / 2 + .5,
            (rows - 1) / 2 + .5
        )

    def draw_maze(self):
        """Draw the maze in a window on the screen."""
        for y in range(self.rows):
            for x in range(self.columns):
                if self.maze[y][x] == OBSTACLE:
                    self.draw_centered_box(
                        x + self.x_translate,
                        -y + self.y_translate,
                        'tan'
                    )
        self.turtle.color('black', 'blue')

    def draw_centered_box(self, x, y, color):
        """Draw a wall."""
        tracer(0)
        self.turtle.up()
        self.turtle.goto(x-.5, y-.5)
        self.turtle.color('black', color)
        self.turtle.setheading(90)
        self.turtle.down()
        self.turtle.begin_fill()
        for i in range(4):
            self.turtle.forward(1)
            self.turtle.right(90)
            self.turtle.end_fill()
            update()
            tracer(1)

    def move_turtle(self, x, y):
        """Move the turtle to coordinates [y][x] in the maze."""
        self.turtle.up()
        self.turtle.setheading(self.turtle.towards(
            x + self.x_translate,
            -y + self.y_translate))
        self.turtle.goto(x + self.x_translate, -y + self.y_translate)

    def drop_breadcrumb(self, color):
        """Change the maze to reflect a breadcrumb."""
        self.turtle.dot(color)

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
    # base case 4 - we have found a dead end.
    else:
        maze.dead_end()

    return north or south or east or west
