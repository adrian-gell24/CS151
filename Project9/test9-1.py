# Bruce Maxwell
# Revised for spring 2013
# test function 1 for lab 8

import turtle_interpreter
import random

def main():
    """ draw a 4x4 square of alternating filled and unfilled squares """
    terp = turtle_interpreter.TurtleInterpreter()

    square = 'F-F-F-F-'
    fsquare = '{F-F-F-F-}'

    for i in range(4):
        for j in range(4):
            terp.place( -100 + j*50, -100 + i*50 )
            terp.color( (random.random(), random.random(), random.random() ) )
            if (j + (i % 2)) % 2 == 0:
                terp.drawString(square, 40, 90)
            else:
                terp.drawString(fsquare, 40, 90)

    terp.hold()

if __name__ == "__main__":
    main()
