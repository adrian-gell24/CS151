# Tony Karalekas
# Spring 2015
# CS 151 Project 4
# Task 3

# ------------------------------

import graphics
import display
import sys
import filter

# Task 3
# creating warhol-like collage
# using same image four times with
# four separate filters from filter file

def main(argv):
	if len(argv) <2:
		print "Usage: python show.py <filename>"
		exit()
		
	filename = argv[1]
	
# define pmap as one pixmap
	pmap = graphics.Pixmap( filename )
	'''read in one pixmap'''
	
# makes four copies of pixmap
	'''makes 4 copies'''
	map1 = pmap.clone()
	map2 = pmap.clone()
	map3 = pmap.clone()
	map4 = pmap.clone()

# filters for each separate square of warhol picture
	'''each picture gets separate filter from task 2'''
	filter.swapRedBlue(map1)
	filter.colorNegative(map2)
	filter.moreGreen(map3)
	filter.purpleHaze(map4)

# defines variable name for twice as large Pixmap
	big = graphics.Pixmap(2*pmap.getWidth(), 2*pmap.getHeight())
	'''make an empty pixmap big enough to hold 4 copies of this one'''
	
# places the four images at different locations 
# into the 'big' pixmap
# each of the four images gets a different filter
	filter.placePixmap( big, map1, 0, 0 )
	'''put the 4 filtered images into the big one'''
	filter.placePixmap( big, map2, 0, pmap.getHeight() )
	filter.placePixmap( big, map3, pmap.getWidth(), 0 )
	filter.placePixmap( big, map4, pmap.getWidth(), pmap.getHeight() )
	
# save the resulting image as a file name 'warhol.py'
	big.save( 'warhol.ppm' )
	
# call the test function with the command line strings as the argument
if __name__ == "__main__":
    main( sys.argv )
	
