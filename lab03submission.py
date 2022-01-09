
# Task 01a: Converting Decimal Numbers to Binary iteratively

from turtle import *
def iter_binary(n):
    rem = ''
    while n > 0:
        rem = str(n % 2) + rem
        n = n // 2
    return rem


# Test Cases
print(iter_binary(1))
print(iter_binary(2))
print(iter_binary(3))
print(iter_binary(4))
print(iter_binary(9))



# Task 01b: Converting Decimal Numbers to Binary recursively
def binary(n):
    # account for '0'
    if n == 0:
        return ''
    elif n == 1:
        return '1'
    else:
        return binary(n // 2) + str(n % 2)


# Test cases
print(binary(1))
print(binary(2))
print(binary(3))
print(binary(4))
print(binary(9))


# Task 06: Drawing the Van Koch Snowflake Fractal
import turtle

def snowflake(tur, lengthSide, levels, color='blue', ps=2):
    tur.pensize(ps)
    tur.pencolor(color)
    if levels == 0:
        tur.forward(lengthSide)
        return
    lengthSide /= 3.0
    snowflake(tur, lengthSide, levels-1)
    tur.left(60)
    snowflake(tur, lengthSide, levels-1)
    tur.right(120)
    snowflake(tur, lengthSide, levels-1)
    tur.left(60)
    snowflake(tur, lengthSide, levels-1)

tur = turtle.Turtle()
screen = turtle.Screen()
screen.screensize(400, 400)

length = 300
levels = 3

tur.penup()
tur.backward(length/2)
tur.pendown()

for i in range(levels):
    snowflake(tur, length, 4)
    tur.right(120)


