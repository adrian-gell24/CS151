# Tony Karalekas
# Spring 2015
# CS 151 Project 4

# Extension 1

# ------------------------------

# imports
import graphics
import display
import sys
import filter


def main(argv):
	if len(argv) <2:
		print "Usage: python show.py <filename>"
		exit()
		
	filename = argv[1]
	filename2 = argv[2]
	
# define pmap as one pixmap
	me = graphics.Pixmap( filename )
	monster = graphics.Pixmap( filename2 )
	'''read in one pixmap'''
	
# makes eight copies of pixmap
	'''makes 8 copies'''
	map1 = me.clone()
	map2 = monster.clone()
	map3 = me.clone()
	map4 = monster.clone()
	map5 = me.clone()
	map6 = monster.clone()
	map7 = me.clone()
	map8 = monster.clone()


# filters for each separate square of extension picture
	'''each picture gets separate filter from task 2'''
	filter.swapRedBlue(map1)
	filter.moreGreen(map2)
	filter.purpleHaze(map3)
	filter.colorNegative(map4)
	filter.swapRedBlue(map6)
	filter.moreGreen(map7)
	filter.purpleHaze(map8)
	filter.colorNegative(map5)

# defines variable name for larger Pixmap
	extension1 = graphics.Pixmap(4*me.getWidth(), 2*me.getHeight())
	'''make an empty pixmap big enough to hold 4 copies of this one'''
	
# places the eight images at different locations 
# into the 'extension1' pixmap
# each of the eight images gets a different filter
	filter.placePixmap( extension1, map2, 0, 0 )
	'''put the 4 filtered images into the big one'''
	filter.placePixmap( extension1, map1, me.getWidth(), 0 )
	filter.placePixmap( extension1, map4, 2*me.getWidth(), 0 )
	filter.placePixmap( extension1, map3, 3*me.getWidth(), 0 )
	filter.placePixmap( extension1, map5, 0, me.getHeight() )
	filter.placePixmap( extension1, map6, me.getWidth(), me.getHeight() )
	filter.placePixmap( extension1, map7, 2*me.getWidth(), me.getHeight() )
	filter.placePixmap( extension1, map8, 3*me.getWidth(), me.getHeight() )

	
# save the resulting image as a file name 'extension1.py'
	extension1.save( 'extension1.ppm' )
	
# call the test function with the command line strings as the argument
if __name__ == "__main__":
    main( sys.argv )
