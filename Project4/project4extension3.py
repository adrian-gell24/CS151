# Tony Karalekas
# Spring 2015
# CS 151 Project 4

# Extension 3

# ------------------------------

# imports
import graphics
import display
import sys
import filter
	
def placeNoGreenPixmap( me, monster, x, y ):
	''' used to position Pixmap in desired location '''
	for i in range(monster.getHeight()):
		for j in range(monster.getWidth()):
			(r, g, b) = monster.getPixel( j, i)
			if g > r and g > b:
				me.setPixel( x+j, y+i, (255, 255, 255) )
def main(argv):
	if len(argv) <2:
		print "Usage: python show.py <filename>"
		exit()
	monster = graphics.Pixmap( 'biggodzilla.ppm' )
	me = graphics.Pixmap( 'me.ppm' )
	'''read in one pixmap'''
	
	extension3 = graphics.Pixmap(monster.getWidth(), monster.getHeight())
	
	filter.placePixmap( extension3, monster , 0, 0 )
	placeNoGreenPixmap( extension3, me, 0, 0)
			


# save the resulting image as a file name 'extension3.py'
	extension3.save( 'extension3.ppm' )
	
# call the test function with the command line strings as the argument
if __name__ == "__main__":
    main(sys.argv)