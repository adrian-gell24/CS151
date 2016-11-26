# Tony Karalekas
# Spring 2015
# CS 151 Project 7
#
# grid.py version 1
#---------------------------------------------
# imports

import sys
import turtle
import lsystem as ls
import turtle_interpreter as it 

#----------------------------------------------

def main(argv):
	'''creates a set of 9 trees based on a lsystem
		in a 3x3 grid.'''

	# check if there are enough arguments
	if len(argv) < 1:
		print "Usage : python grid.py <in_filename>"
		exit()
		
	lsys_filename = argv[1]

	# create the lsystems from a file
	lsys = ls.createLsystemFromFile( lsys_filename )
	
	x = [-200, 0, 200]
	y = [100, -150, -350] 
	iters = [1, 2, 3]
	angles = [22, 46, 60]
	dist = 10
	for c in range( len(iters)):
		for r in range( len(iters)):
			turtle.up()
			turtle.speed(300)
			turtle.goto(x[c], y[r])
			turtle.setheading(0)
			turtle.left(90)
			s = ls.buildString( lsys, iters[c] )
			turtle.down()
			it.drawString( s, dist, angles[r] )
			
	
	# wait and update
	turtle.update()
	it.hold()
	
# main calling code
if __name__ == '__main__':
	main(sys.argv)
			
			
			
			
			