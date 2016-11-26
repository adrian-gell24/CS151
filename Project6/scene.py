# Tony Karalekas
# Spring 2015
# CS 151 
#
# Project 6

# PART 2
#-----------------------------------------------------------
# imports

import time
import random
import graphics as gr
import complex_shape as cs


# -------------------------------------------------------
# PART 2 of Project 6

#----------------------------------------------

# part 5, 6, 7 lab
# functions used from lab
# for project 6
# USED TO DRAW FINAL SCENE

def draw( objlist, win ):
	""" Draw all of the objects in objlist in the window (win) """
	for item in objlist:
		item.draw(win)

def move( objlist, dx, dy ):
	""" Draw all of the objects in objlist by dx in the x-direction
	and dy in the y-direction """
	for item in objlist:
		item.move( dx, dy )

def undraw( objlist ):
	""" Undraw all of the objects in objlist """
	for item in objlist:
		item.undraw()

#--------------------------------

# main calling code

# this code is almost identical to test_scene from complex_shape.py
# this is because i used test to test my entire scene

def main():
	""" Create a window and plot a scene with a 
	of a steam plant in it. """
	win = gr.GraphWin( 'title', 1000, 700, False )
	
	# the three separate functions for objects
	landscape = cs.landscape_init(0, 385, 1.0)
	cannon = cs.cannon_init( 50, 300, 1.0 )
	ship = cs.ship_init( 700, 330, 1.0)

	#drawing the three separate object functions
	draw(landscape, win)
	draw(cannon, win)
	draw( ship, win)
		
	win.update()

	# ANIMATION for loop to shoot "big shot' and cannonballs
	for frame_num in range(100):
		time.sleep( 0.15 )
		print frame_num
		cs.cannonball_animation_frame( cannon, frame_num, win )
		win.update()
		if win.checkMouse():
			break

	win.getMouse()
	win.close() 
	
if __name__ == "__main__":
	main()