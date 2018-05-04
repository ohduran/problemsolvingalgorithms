from turtle import Turtle, Screen


turtle = Turtle()
window = Screen()


def draw_spiral(turtle, line_len):
    # base case
    if line_len > 0 :
        turtle.forward(line_len)
        turtle.right(90)
        # recursion
        draw_spiral(turtle, line_len - 5)


# draw_spiral(turtle, 100)
# window.exitonclick()


def tree(branch_len, turtle):
    if branch_len > 5:
        turtle.forward(branch_len)
        turtle.right(20)
        tree(branch_len - 15, turtle)
        turtle.left(40)
        tree(branch_len - 10, turtle)
        turtle.right(20)
        turtle.backward(branch_len)


def main_tree():
        t = Turtle()
        window = Screen()
        t.left(90)
        t.up()
        t.backward(100)
        t.down()
        t.color('green')
        tree(75, t)
        window.exitonclick()


def draw_triangle(points, color, turtle):
        turtle.fillcolor(color)
        turtle.up()
        turtle.goto(points[0][0], points[0][1])
        turtle.down()
        turtle.begin_fill()
        turtle.goto(points[1][0], points[1][1])
        turtle.goto(points[2][0], points[2][1])
        turtle.goto(points[0][0], points[0][1])
        turtle.end_fill()


def get_mid(p1, p2):
        return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points, degree, turtle):
        color_map = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
        draw_triangle(points, color_map[degree], turtle)
        # recursion until degree is 0
        if degree >= 0:
                sierpinski(
                        [
                                points[0],
                                get_mid(points[0], points[1]),
                                get_mid(points[0], points[2]),
                        ],
                        degree - 1, turtle)
                sierpinski(
                        [
                                points[1],
                                get_mid(points[0], points[1]),
                                get_mid(points[1], points[2]),
                        ],
                        degree - 1, turtle)
                sierpinski(
                        [
                                points[2],
                                get_mid(points[2], points[1]),
                                get_mid(points[0], points[2]),
                        ],
                        degree - 1, turtle)


def main():
        turtle = Turtle()
        window = Screen()
        my_points = [[-100, 50], [0, 100], [100, -50]]
        sierpinski(my_points, 3, turtle)
        window.exitonclick()


if __name__ == '__main__':
        main()
