# Bruce Maxwell
# spring 2013
# test program for lsystem and interpreter
#

import turtle
import sys
import lsystem as ls
import turtle_interpreter as it


# takes in the list of strings from the command line
# reads in an lsystem file, generates the string and
# draws two copies of a pair of shapes
def main(argv):

    # check if there are enough arguments
    if len(argv) < 4:
        print 'usage: %s <lsystem filename> <distance> <angle>' % (argv[0])
        exit()

    # create the lsystem from a file
    lsys = ls.createLsystemFromFile( argv[1] )

    # build the lsystem string with 3 iterations
    lstr = ls.buildString( lsys, 3 )

    dist = float( argv[2] )
    angle = float( argv[3] )

    # draw the lsystem
    turtle.tracer(False)
    turtle.left(90)
    it.drawString( lstr, dist, angle )
    
    # wait
    turtle.update()
    it.hold()


if __name__ == "__main__":
    main( sys.argv )


    
