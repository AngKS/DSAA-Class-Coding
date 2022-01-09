# import turtle


# def drawSquare(t, dim=50, x=0, y=0, col='blue', ps=2):
#     t.pencolor(col)
#     t.pensize(ps)
#     t.up()
#     t.goto(x, y)
#     t.down()

#     for i in range(4):
#         t.forward(dim)
#         t.right(90)


# def DrawNestedSquare(tur, dim):
#     if dim >= 5:
#         drawSquare(tur, dim, x=-(dim / 2), y=(dim / 2), col='red')
#         DrawNestedSquare(tur, dim - 5)


# def drawBlockySpiral(tur, line_len=100, reduce_len=5, col='red', ps=2):
#     tur.pencolor(col)
#     tur.pensize(ps)
#     if line_len >= 5:
#         tur.forward(line_len)
#         tur.right(90)
#         drawBlockySpiral(tur, line_len - reduce_len, reduce_len, col, ps)

# # Main program
# tur = turtle.Turtle()  # is like a pen
# scr = turtle.Screen()  # is like a canvas tur.speed('fastest') # how fast the turtle goes
# # Setting the screen dimensions
# w, h = 200, 200
# # Canvas dimensions scr.setup(w+50, h+50) # Window dimension
# scr.screensize(w, h)
# # Draw your things here
# # DrawSquare(tur, dim=200, x=-100, y=100, col='green', ps=4)
# # DrawNestedSquare(tur, dim=200)

# drawBlockySpiral(tur, line_len=100, reduce_len=5, col='red')

# # When we click we will stop
# scr.exitonclick()

# Task 07: Fractal Tree

import turtle


def DrawTree(tur, line_len=50, col='red', ps=2):
    if line_len >= 5:
        tur.pencolor = col
        tur.pensize(ps)

        # main branch
        tur.forward(line_len)

        # left branch
        tur.left(20)
        DrawTree(tur, line_len-10)

        # assume turtle goes back to where it started the left branch
        tur.right(40)
        DrawTree(tur, line_len-10)

        # need to bring turtle back to where the main branch started
        tur.left(20)
        tur.backward(line_len)


# Main program
tur = turtle.Turtle()  # is like a pen
scr = turtle.Screen()  # is like a canvas tur.speed('fastest') # how fast the turtle goes
# Setting the screen dimensions
w, h = 200, 200
# Canvas dimensions scr.setup(w+50, h+50) # Window dimension
scr.screensize(w, h)
# Draw your things here

tur.left(90)
DrawTree(
    tur,
    line_len=60,
    ps=2
)

# When we click we will stop
scr.exitonclick()
