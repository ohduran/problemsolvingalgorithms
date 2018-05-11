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
from turtle import Turtle, setup, tracer, update


BREADCRUMB = "-"
BREADCRUMB_COLOR = 'black'
OBSTACLE = "+"
OBSTACLE_COLOR = 'red'
PART_OF_PATH = "o"
PART_OF_PATH_COLOR = 'green'


class Maze:
    """Will draw the maze for the turtle to walk across."""

    def __init__(self, maze_file_name):
        """
        Read in a data file representing a maze,
        initializes the internal representation of the maze,
        and finds the starting point of the turtle.
        """
        with open(maze_file_name, 'r') as maze_file:
            self.maze = [[square for square in line if square != '\n']
                         for line in maze_file]
            self.rows = sum((1 for line in maze_file))
            # maze assumed to have rows of the same length
            self.columns = len(self.maze[0])

            self.start_row, self.start_column = [(row_number, row.index('S'))
                                                 for row_number, row
                                                 in enumerate(self.maze)
                                                 if 'S' in row][0]
        self.width = self.columns / 2
        self.height = self.rows / 2
        self.t = Turtle(shape='turtle')
        setup(width=600, height=600)

    def draw_maze(self):
        """Draw the maze in Tkinter."""
        for y in range(self.rows):
            for x in range(self.columns):
                if self.maze[y][x] == OBSTACLE:
                    self.draw_centered_box(x + self.width,
                                           - y - self.height, 'tan')
        self.t.color('black', 'blue')

    def draw_centered_box(self, x, y, color):
        """Draw a box centered in (x, y)."""
        tracer(0)
        self.t.up()
        self.t.goto(x-0.5, y-0.5)
        self.t.color('black', color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
            self.t.end_fill()
            update()
            tracer(1)

    def move_turtle(self, x, y):
        """Move turtle to coordinates x, y."""
        self.t.up()
        self.t.setheading(self.t.towards(x + self.width, -y - self.height))
        self.t.goto(x + self.width, -y - self.height)

    def drop_color(self, color):
        """Drop a breadcrumb of a certain color."""
        self.t.dot(color)

    def move_to(self, row, col):
        """Move the turtle to row=row and column=col."""
        self.move_turtle(col, row)

    def is_exit(self, row, col):
            """
            Return True
            if the position of the turtle is the end of the maze.
            """
            first_row = row == 0
            last_row = row == self.rows - 1
            first_column = col == 0
            last_column = col == self.columns - 1
            return first_row or last_row or first_column or last_column

    def __getitem__(self, idx):
            return self.maze[idx]


def search_from(maze, start_row, start_column):
    """Search until we find the exit, recursively."""
    maze.move_to(start_row, start_column)
    # base case 1 - if obstacle, return False
    if maze[start_row][start_column] == OBSTACLE:
        return False
    # base case 2 - if we have been there already, return False
    if maze[start_row][start_column] == BREADCRUMB:
        return False
    # base case 3 - success, and outside edge not occupied by OBSTACLE
    if maze.is_exit(start_row, start_column):
        maze.drop_color(PART_OF_PATH)
        return True

    # recursion
    maze.drop_color(PART_OF_PATH)
    north = search_from(maze, start_row - 1, start_column)
    south = search_from(maze, start_row + 1, start_column)
    east = search_from(maze, start_row, start_column + 1)
    west = search_from(maze, start_row, start_column - 1)

    where = north or south or east or west
    if where is True:
            maze.drop_color(PART_OF_PATH)
            return where

    # base case 4 - we have found a dead end.
    else:
        maze.drop_color(BREADCRUMB)
        return False
