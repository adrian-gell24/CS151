# Tony Karalekas
# Spring 2015
# CS 151 Project 5
# mycoverphoto.py file
# 
# Extension 2
# --------------------------
import sys
import collage
import filter


# place my face on mount rushmore
# place myface.ppm on mtrushmore.ppm

# main function similar to that from test buildcollage.py file
def main( argv ):
	if len(argv) < 3:
		print 'You need more command line files you dumb dumb'
		
	'''new clist with command line files'''
	clist = [	[ argv[1], 0, 0, 'original', 1.0, False, None ],
				[ argv[2], 175, 25,'swapRedBlue', 1.0, False, None ],
			]

	# call readImages
	collage.readImages( clist )
	
	# call buildCollage
	dst = collage.buildCollage( clist )
	
	# save the image
	dst.save( 'p5extension2.ppm' )

	return

if __name__ == "__main__":
    main(sys.argv)