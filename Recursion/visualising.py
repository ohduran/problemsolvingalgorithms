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


def main():
        t = Turtle()
        window = Screen()
        t.left(90)
        t.up()
        t.backward(100)
        t.down()
        t.color('green')
        tree(75, t)
        window.exitonclick()


if __name__ == '__main__':
        main()
