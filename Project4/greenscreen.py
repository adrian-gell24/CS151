# Tony Karalekas
# Spring 2015
# CS 151 Project 4
# Task 4

# ------------------------------

import graphics
import display
import sys
import filter

# Task 4
# display the blue-screen image with
# background screen of different color


	
def greenscreen(argv):
	''' we want to remove green from green screen '''
	
	if len(argv) < 2:
		print "Usage: python show.py <filename>"
		exit()
	
	pm = graphics.Pixmap( 'me.ppm' )
	w= pm.getWidth()
	h = pm.getHeight()
	
	# this will loop through pixels and
	# find all super green pixels
	# and changed their color
	for i in range(w):
		for j in range(h):
			(r, g, b) = pm.getPixel( i, j )
			if g > r and g > b:
				pm.setPixel( i, j, (0.5*r, 0, 0.7*b) )
				'''gets rid of all the green in the pixels
					it has scanned through'''
			
	filename = argv[1]

	pm.save( 'newme.ppm' )

# call the test function with the command line strings as the argument
if __name__ == "__main__":
    greenscreen( sys.argv )
    
