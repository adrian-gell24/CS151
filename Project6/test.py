# Tony Karalekas
# Spring 2015
# CS 151 
#
# Lab 6

#----------------------------------------

# imports

import time
import random
import graphics as gr

#-----------------------------------------
# part 1, 2, 3, 4 lab
# the purpose of the function is to make a Circle 
# and then have it move randomly around the screen 
# until the user clicks in the window.

def main():
	win = gr.GraphWin("Circle", 500, 500, False )
	shapes = []
	c = gr.Circle( gr.Point(250, 250), 10)
	c.draw( win )
	shapes.append( c )
	
	while True:
		time.sleep( 0.1 )
		for shape in shapes:
			dx = random.randint( -10, 10 )
			dy = random.randint( -10, 10 )
			shape.move( dx, dy )
			
			r = random.randint( 0, 255 )
			g = random.randint( 0, 255 )
			b = random.randint( 0, 255 )
			color = gr.color_rgb( r, g, b )
			shape.setFill( color )
		if random.random() < 0.2:
			oldshape = random.choice( shapes )
			newshape = oldshape.clone()
			newshape.draw( win )
			shapes.append( newshape )
			
		win.update()
		
		if win.checkMouse() != None:
			break 
	
	win.close()




if __name__ == "__main__":
	main()