# Tony Karalekas
# Spring 2015
# CS 151 Lab 4
#

# --------------------------

# tool for looking at ppm image

import graphics
import display
import sys
import filter

def main(argv):
	''' reads in an image file and displays it in a window '''
	
	if len(argv) <2:
		print "Usage: python show.py <filename>"
		exit()
		
	filename = argv[1]
	
	pixm = graphics.Pixmap( filename )
	
	# put a little test code
	# (r, g, b) = pixm.getPixel( 42, 35 )
	#print "color:", r, g, b
	#pixm.setPixel( 42, 35, (b,g,r) )
	
	win = display.displayPixmap( pixm, filename )
	
	win.getMouse()
	
if __name__ == "__main__":
	main( sys.argv )