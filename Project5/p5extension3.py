# Tony Karalekas
# Spring 2015
# CS 151 Project 5
# Extension 3

# --------------------------
import sys
import collage
import filter

# main function similar to that from test buildcollage.py file
def main( argv ):	

	if len(argv) == 2:
		'''new clist with 1 command line files'''
		clist1 = [	[ argv[1], 0, 0, 'colorNegative', 1.0, False, None ],
					]	
		# call readImages
		collage.readImages( clist1 )
		# call buildCollage
		dst = collage.buildCollage( clist1 )
		# save the image
		dst.save( 'p5extension3a.ppm' )
		
		#for 3a i used snorlax.ppm
	
	elif len(argv) == 4:
		'''new clist with 3 command line files'''
		clist2 = [	[ argv[1], 0, 0, 'swapRedBlue', .90, False, None ],
				[ argv[2], 600, 0, 'colorNegative', 0.75, False, None ],
				[ argv[3], 300, 0, 'purpleHaze', 0.65, False, None],
				]
		# call readImages
		collage.readImages( clist2 )
		# call buildCollage
		dst = collage.buildCollage( clist2 )
		# save the image
		dst.save( 'p5extension3b.ppm' )
		
		#for 3b i used stephcurry.ppm
	
	else:
		'''new clist with 5 command line files'''
		clist3 = [	[ argv[1], 0, 0, 'swapRedBlue', .90, False, None ],
				[ argv[2], 400, 500, 'colorNegative', 0.75, False, None ],
				[ argv[3], 0, 500, 'purpleHaze', 0.8, False, None],
				[ argv[4], 400, 0, 'moreGreen', 0.50, False, None],
				[ argv[5], 125, 100, 'original', 1.0 , True, None] 
				]
		# call readImages
		collage.readImages( clist3 )
		# call buildCollage
		dst = collage.buildCollage( clist3 )
		# save the image
		dst.save( 'p5extension3c.ppm' )
		
		#for 3c i used me.ppm and myface.ppm


	return



if __name__ == "__main__":
	main(sys.argv)