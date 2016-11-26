# Tony Karalekas
# Spring 2015
# CS 151 Project 5
# mycollage.py file
# Task 4

# --------------------------
import sys
import collage
import filter


# main function similar to that from test buildcollage.py file
def main( argv ):
	if len(argv) < 6:
		print 'You need more command line files you dumb dumb'
		
	'''new clist with command line files'''
	clist = [	[ argv[1], 0, 0, 'swapRedBlue', .90, False, None ],
				[ argv[2], 400, 400, 'colorNegative', 0.75, False, None ],
				[ argv[3], 0, 350, 'purpleHaze', 0.65, False, None],
				[ argv[4], 450, 0, 'moreGreen', 0.50, False, None],
				[ argv[5], 125, 50, 'original', 1.0 , True, None] 
			]
	# call readImages
	collage.readImages( clist )
	# call buildCollage
	dst = collage.buildCollage( clist )
	# save the image
	dst.save( 'mycollage.ppm' )
	return
if __name__ == "__main__":
	main(sys.argv)
	
