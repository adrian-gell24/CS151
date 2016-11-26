# Tony Karalekas
# Spring 2015
# CS 151 Project 5
# mycoverphoto.py file
# 
# Task 5
# --------------------------
import sys
import collage
import filter


# coverphoto using maine.ppm images
# about three times as wide as it is high
# at least two filters

# main function similar to that from test buildcollage.py file
def main( argv ):
	if len(argv) < 6:
		print 'You need more command line files you dumb dumb'
		
	'''new clist with command line files'''
	clist = [	[ argv[1], 0, 0, 'swapRedBlue', .60, False, None ],
				[ argv[2], 200, 0,'colorNegative', 0.85, False, None ],
				[ argv[5], 800, 0, 'swapRedBlue', 0.60, False, None],
				[ argv[4], 600, 0, 'colorNegative', 0.85, False, None],
				[ argv[3], 400, 0, 'swapRedBlue', 1.0, False, None]
			]

	# call readImages
	collage.readImages( clist )
	
	# call buildCollage
	dst = collage.buildCollage( clist )
	
	# save the image
	dst.save( 'mycoverphoto.ppm' )

	return

if __name__ == "__main__":
    main(sys.argv)