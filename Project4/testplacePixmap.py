# Bruce Maxwell
# spring 2011
# Updated by Stephanie Taylor Fall 2014
# project 4
# Test function for the placePixmap function
#

import sys
import graphics
import filter

# takes in a filename of a ppm image
# creates a new Pixmap twice as wide and copies
# the original image into it twice
def test( argv ):

    # test if the user provided a filename
    if len(argv) < 2:
        print 'usage: %s <image filename>' % (argv[0])
        exit()

    filename = argv[1]

    # see if we can open the file 
    try:
        srcImage = graphics.Pixmap( filename )
    except:
        print 'error: unable to open file %s' % (filename)
        exit()

    # create a new empty image that is the same height and twice as wide
    dstImage = graphics.Pixmap( srcImage.getWidth() * 2, srcImage.getHeight() )

    # place the original image into the empty image in two places
    filter.placePixmap( dstImage, srcImage, 0, 0 )
    filter.placePixmap( dstImage, srcImage, srcImage.getWidth(), 0 )

    # save the new image to the file duplicate.ppm
    dstImage.save( 'duplicate.ppm' )

    return

# call the test function with the command line strings as the argument
if __name__ == "__main__":
    test( sys.argv )