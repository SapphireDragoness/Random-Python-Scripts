import turtle
import argparse

iterations = 10

""" parser = argparse.ArgumentParser(
    prog = 'dragon_curve_generator',
    description = 'Dragon curve generator'
)

parser.add_argument('iterations', metavar = 'iterations', type = int, help = 'number of iterations to be performed')

args = parser.parse_args() """

def iterate(sequence):
    sequence = sequence.append(0).append(map(lambda x: 1 if x == 0 else 0, sequence[::-1]))
    return sequence

def generateSequence(iterations):
    sequence = list((0))
    for i in range(0, iterations):
        sequence = iterate(sequence)
    return sequence

t = turtle.Turtle()
t.hideturtle()
t.speed("fastest")
t.color("#054b8c")

s = turtle.Screen()
s.title("Dragon Curve Generator")
s.bgcolor("black")
s.screensize(1920, 1080)
s.setup(width=1.0, height=1.0, startx=None, starty=None)

t.forward(10)
for x in generateSequence(iterations):
    if x == 0:
        t.right(90)
        t.forward(10)
    else:
        t.left(90)
        t.forward(10)

t.write("Click to exit")
s.exitonclick()
