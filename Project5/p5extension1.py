# Tony Karalekas
# Spring 2015
# CS 151 Project 5
# mycoverphoto.py file
# 
# Extension 1
# --------------------------
import sys
import collage
import filter


# place myself inside Michael Jackson's Thriller Video
# place me.ppm inside thriller.ppm


# main function similar to that from test buildcollage.py file
def main( argv ):
	if len(argv) < 3:
		print 'You need more command line files you dumb dumb'
		
	'''new clist with command line files'''
	clist = [	[ argv[1], 0, 0, 'original', .80, False, None ],
				[ argv[2], 675, 200,'original', 1.0, True, None ],
			]

	# call readImages
	collage.readImages( clist )
	
	# call buildCollage
	dst = collage.buildCollage( clist )
	
	# save the image
	dst.save( 'p5extension1.ppm' )

	return

if __name__ == "__main__":
    main(sys.argv)