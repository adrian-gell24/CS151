# Tony Karalekas
# Spring 2015
# CS 151 Project 4
# Filter.py file
# Task 1 and Task 2

# --------------------------

# imports 

import graphics
import display
import sys

#------------------------------

# Task 2
# create define multiple filters
# similar to original swapRedBlue() from lab
# but different varieties/more complex


def swapRedBlue( pixm ):
	'''first filter from class -- simple'''
	for i in range( pixm.getHeight() ):
		for j in range( pixm.getWidth() ):
			(r, g, b) = pixm.getPixel( j, i )
			pixm.setPixel( j, i, (b,g,r) )
	return 
	
def colorNegative( pixm ):
	'''creates negative color filter'''
	for i in range( pixm.getHeight() ):
		for j in range( pixm.getWidth() ):
			(r, g, b) = pixm.getPixel( j, i )
			pixm.setPixel( j, i, (255-r, 255-g, 255-b) )
	return 

def purpleHaze( pixm ):
	'''creates purple haze filter'''
	for i in range( pixm.getHeight() ):
		for j in range( pixm.getWidth() ):
			(r, g, b) = pixm.getPixel( j, i )
			if b > r and b > g:
				pixm.setPixel( j, i, (0.75*r, 0.3*g, 0.7*b) )
			elif r > b and r >g:
				pixm.setPixel( j, i, (0.5*r, 0.5*g, 0.7*b) )
			elif g > b and g >r:
				pixm.setPixel( j, i, (0.65*r, 0.25*g, 0.75*b) )
	return 

def moreGreen( pixm ):
	'''creates extra green filter'''
	for i in range( pixm.getHeight() ):
		for j in range( pixm.getWidth() ):
			(r, g, b) = pixm.getPixel( j, i )
			pixm.setPixel( j, i, (0.3*r, g, 0.5*b) )
	return 

# =========================================================

# Task 1
# create placePixmap file
# takes four arguments
# places pixmap file at 0,0
# then have it copy and display to the right of original image

# this places Pixmap image/file at given location
def placePixmap( dst, src, x, y ):
	''' used to position Pixmap in desired location '''
	for i in range(src.getHeight()):
		for j in range(src.getWidth()):
			(r, g, b) = src.getPixel( j, i )
			dst.setPixel( x+j, y+i, (r,g,b) )



#-----------------------------


# code from lab4
# used throughout project4
# test function for filters
'''useful test function'''

def main(argv):
	''' reads in an image file and displays it in a window '''
	
	if len(argv) < 2:
		print "Usage: python show.py <filename>"
		exit()
		
	filename = argv[1]

	dst = graphics.Pixmap( filename )
	
	purpleHaze( dst )
	'''change this filter function to test out other filters'''
	
	win = display.displayPixmap( dst, filename )
	
	win.getMouse()
	
if __name__ == "__main__":
	main( sys.argv )


	