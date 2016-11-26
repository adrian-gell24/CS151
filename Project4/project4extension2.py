# Tony Karalekas
# Spring 2015
# CS 151 Project 4
# Extension 2

# ------------------------------

import graphics
import display
import sys
import filter

# Task 4
# display the blue-screen image with
# background screen of different color

def greenscreen(argv):
	''' reads in an image file and displays it in a window '''
	
	if len(argv) < 2:
		print "Usage: python show.py <filename>"
		exit()
	
	pm = graphics.Pixmap( 'me.ppm' )
	w= pm.getWidth()
	h = pm.getHeight()
	# splits the pixmap into four separate corners
	# using four for loops with different coordinate ranges
	for i in range(w/2):
		for j in range(h/2):
			'''this one for example, takes the corner of the
				pixmap that has a width/2 and a height/2'''
			(r, g, b) = pm.getPixel( i, j )
			if g > r and g > b:
				pm.setPixel( i, j, (0.5*r, 0, 0.7*b) )
	for i in range(w/2):
		for j in range(h):
			(r, g, b) = pm.getPixel( i, j )
			if g > r and g > b:
				pm.setPixel( i, j, (0.25*r, 0, b) )
	for i in range(w):
		for j in range(h/2):
			(r, g, b) = pm.getPixel( i, j )
			if g > r and g > b:
				pm.setPixel( i, j, (0.75*r, 0, .25*b) )
	for i in range(w):
		for j in range(h):
			(r, g, b) = pm.getPixel( i, j )
			if g > r and g > b:
				pm.setPixel( i, j, (0.5*r, 0.7*g, 0.2*b) )
			
	filename = argv[1]
	
# save the resulting image as a file name 'extension2.py'
	pm.save( 'extension2.ppm' )

# call the test function with the command line strings as the argument
if __name__ == "__main__":
    greenscreen( sys.argv )