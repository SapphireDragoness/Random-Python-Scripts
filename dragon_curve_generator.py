import turtle
import argparse

parser = argparse.ArgumentParser(
    prog = 'dragon_curve_generator',
    description = 'Dragon curve generator'
)

parser.add_argument('iterations', metavar = 'iterations', type = int, help = 'number of iterations to be performed')
parser.add_argument('color', metavar = 'color', type = str, help = 'color of the curve')

args = parser.parse_args()

def iterate(sequence):
    sequence = sequence + "0" + swap(sequence[::-1])
    return sequence

def swap(sequence):
    auxSequence = ""
    for x in sequence:
        if x == "0":
            auxSequence += "1"
        else: 
            auxSequence += "0"
    return auxSequence


def generateSequence(iterations):
    sequence = "0"
    for i in range(0, iterations):
        sequence = iterate(sequence)
    return sequence

t = turtle.Turtle()
t.hideturtle()
t.speed("fastest")
t.color(args.color)

s = turtle.Screen()
s.title("Dragon Curve Generator")
s.bgcolor("black")
s.screensize(1920*2, 1080*2)
s.setup(width=1.0, height=1.0, startx=None, starty=None)

t.forward(10)
for x in generateSequence(args.iterations):
    if x == "0":
        t.right(90)
        t.forward(10)
    else:
        t.left(90)
        t.forward(10)

t.write("Click to exit")
s.exitonclick()
