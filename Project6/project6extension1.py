# Tony Karalekas
# Spring 2015
# CS 151 
#
# Lab 6
# EXTENSION
#----------------------------------------

# imports

import time
import random
import graphics as gr

#-----------------------------------------

# part 5, 6, 7 lab
# functions used from lab
# for project 6
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

#----------------------------------------
# part 1 of the project6
# two complex init objects

def cannon_init(x, y, scale):
	""" Create the list of objects needed to draw a cannon
	at position (x,y) with the given scale """
	
	shapes = []
	
	'''the separate rectangle are parts of the cannon
		the cannonball is the large "first shot" cannonball'''
	
	r1 = gr.Rectangle( gr.Point(x,y), gr.Point(x+scale*100, y+scale*50) )
	r1.setFill(gr.color_rgb(185, 185, 185))
	shapes.append( r1 )
	
	r2 = gr.Rectangle( gr.Point(x+scale*100, y+scale*10), gr.Point(x+scale*200, y+scale*40) )
	r2.setFill(gr.color_rgb(185, 185, 185))
	shapes.append( r2 )
	
	r3 = gr.Rectangle( gr.Point(x+scale*200, y+scale*20) , gr.Point(x+scale*250, y+scale*30) )
	r3.setFill(gr.color_rgb(185, 185, 185))
	shapes.append( r3 )
	
	r4 = gr.Rectangle( gr.Point(x+scale*15, y+scale*50) , gr.Point(x+scale*40, y+scale*85) )
	r4.setFill(gr.color_rgb(176, 133, 85 ))
	shapes.append( r4 )
	
	r5 = gr.Rectangle( gr.Point(x+scale*115, y+scale*40) , gr.Point(x+scale*140, y+scale*85) )
	r5.setFill(gr.color_rgb(176, 133, 85 ))
	shapes.append( r5 )
	
	cannonball = gr.Circle( gr.Point(x+250*scale,y+25*scale), 20)
	cannonball.setFill( gr.color_rgb(230, 230, 250))
	shapes.append( cannonball )
	
	return shapes
	
def landscape_init( x, y, scale):
	""" Create the list of objects needed to draw a landscape
		at position (x,y) with the given scale """
		
	shapes = []
	'''3 rectangle and 1 circle for different parts of 
		landscape like sky, sun, grass, and water'''
		
	sky = gr.Rectangle( gr.Point(x,y-500*scale), gr.Point(x+scale*1000, y+scale*500) )
	sky.setFill(gr.color_rgb( 135, 206, 235))
	shapes.append( sky )
	
	sun = gr.Circle( gr.Point(x+200*scale,y-250*scale), 70)
	sun.setFill( gr.color_rgb(255, 69, 0))
	shapes.append( sun )
	
	grass = gr.Rectangle( gr.Point(x,y), gr.Point(x+scale*450, y+scale*350) )
	grass.setFill(gr.color_rgb( 0, 128, 0))
	shapes.append( grass )
	
	water= gr.Rectangle( gr.Point(x+scale*450, y), gr.Point(x+scale*1000, y+scale*700) )
	water.setFill(gr.color_rgb( 70, 130, 180))
	shapes.append( water )
	
	return shapes

def ship_init( x, y, scale ):
	""" Create the list of objects needed to draw a ship
		at position (x,y) with the given scale """

	shapes = []
	'''separate rectangles triangles for the 
		body of the ship, mast, and flag and
		circle for the windows'''
	
	body = gr.Rectangle( gr.Point(x,y), gr.Point(x+scale*200, y+scale*100) )
	body.setFill(gr.color_rgb( 218, 165, 32))
	shapes.append( body )
	
	mast = gr.Rectangle( gr.Point(x+scale*100, y-250*scale), gr.Point(x+scale*110, y) )
	mast.setFill(gr.color_rgb( 222, 184, 135))
	shapes.append( mast )
	
	t1 = gr.Polygon( gr.Point(x, y), gr.Point(x-scale*50, y+scale*50), gr.Point(x, y+scale*100 ))
	t1.setFill(gr.color_rgb( 218, 165, 32))
	shapes.append( t1 )
	
	t2 = gr.Polygon( gr.Point(x+scale*200, y), gr.Point(x+scale*250, y+scale*50), gr.Point(x+scale*200, y+scale*100 ))
	t2.setFill(gr.color_rgb(218, 165, 32))
	shapes.append( t2 )
	
	flag = gr.Polygon( gr.Point(x+scale*110, y-150*scale), gr.Point(x+scale*160, y-200*scale), gr.Point(x+scale*110, y-250*scale) )
	flag.setFill(gr.color_rgb( 255, 0, 255))
	shapes.append( flag )
	
	window1 = gr.Circle( gr.Point(x+40*scale, y+50*scale), 10)
	window1.setFill( gr.color_rgb(230, 230, 250))
	shapes.append( window1 )
	
	window2 = gr.Circle( gr.Point(x+100*scale, y+50*scale), 10)
	window2.setFill( gr.color_rgb(230, 230, 250))
	shapes.append( window2 )

	window3 = gr.Circle( gr.Point(x+160*scale, y+50*scale), 10)
	window3.setFill( gr.color_rgb(230, 230, 250))
	shapes.append( window3 )

	return shapes
	
def bird_init(x,y,scale):
	""" Create the list of objects needed to draw a bird
		at position (x,y) with the given scale """

	bird = []
	'''separate rectangles triangle and circle for the 
		body of the bird, beak, and legs'''
	
	body = gr.Rectangle( gr.Point(x,y), gr.Point(x+scale*75, y+scale*25) )
	body.setFill(gr.color_rgb( 107, 142, 35))
	bird.append( body )
	
	leg1 = gr.Rectangle( gr.Point(x, y+25*scale), gr.Point(x+scale*10, y+40*scale) )
	leg1.setFill(gr.color_rgb( 95, 158, 160))
	bird.append( leg1 )
	
	leg2 = gr.Rectangle( gr.Point(x+30, y+25*scale), gr.Point(x+scale*40, y+40*scale) )
	leg2.setFill(gr.color_rgb( 95, 158, 160))
	bird.append( leg2 )
	
	head = gr.Circle( gr.Point(x+75*scale, y-5*scale), 15)
	head.setFill( gr.color_rgb(127, 255, 215))
	bird.append( head )
	
	beak = gr.Polygon( gr.Point(x+85*scale, y*scale), gr.Point(x+scale*105, y-scale*10),
	gr.Point(x+scale*85, y-scale*20 ))
	beak.setFill(gr.color_rgb( 255, 215, 0))
	bird.append( beak )
	
	return bird
	
	

#----------------------------------

def cannonball_animation_frame(shapes, frame_num, win):
	"""Cannonball animation. The animation will
		involve one big cannonball shooting out of the cannon.
		shapes is a list containing the graphics objects needed to draw
		the cannonball scene.
		frame_num is a number indicating which frame of the animation
		it is. win is the GraphWin object containing the scene.
		This animates by creating up to 20 little cannonball circles too. 
		Each circle creeps across the screen until it gets to the edge"""
	p1 = shapes[2].getP1()
	p2 = shapes[2].getP2()
	
	dy = p2.getY() - p1.getY()
	newy = (p1.getY() + p2.getY())*0.5
	newx = p2.getX() - dy*0.5
	
	if frame_num %2 == 0 and len(shapes) < 22:
		c = gr.Circle(gr.Point( newx, newy), 0.4*dy)
		c.setFill(gr.color_rgb(150, 150, 150))
		c.draw(win)
		shapes.append(c)
		
	for shape in shapes[5:]:
		shape.move( 25, 0)
		center = shape.getCenter()
		
		if center.y < 0:
			mx = newx - center.getX()
			my = newy - center.getY()
			shape.move( mx, my )
			
def bird_animation_frame(bird, frame_num, win):
	"""Bird animation. The animation will
		involve one bird flying above the water.
		bird is a list containing the graphics objects needed to draw
		the bird scene.
		frame_num is a number indicating which frame of the animation
		it is. win is the GraphWin object containing the scene.
		The bird creeps across the screen until it gets to the boat on fire"""
	p1 = bird[2].getP1()
	p2 = bird[2].getP2()
	
	dy = p2.getY() - p1.getY()
	newy = (p1.getY() + p2.getY())*0.5
	newx = p2.getX() - dy*0.5
		
	for item in bird:
		item.move( 5, 0 )	
		
		
#--------------------------------------------------

# main calling code

def test_scene():
	""" Create a window and plot a scene with a 
	of a steam plant in it. """
	win = gr.GraphWin( 'title', 1000, 700, False )

	# the four separate functions for objects
	landscape = landscape_init(0, 385, 1.0)
	cannon = cannon_init( 50, 300, 1.0 )
	ship = ship_init( 700, 330, 1.0)
	bird = bird_init( 300, 100, 1.0)
	
	#drawing the four separate object functions
	draw(landscape, win)
	draw(bird, win)
	draw(cannon, win)
	draw( ship, win)
		
	win.update()

	# ANIMATION for loop to shoot "big shot' and cannonballs, and BIRD
	for frame_num in range(60):
		time.sleep( 0.15 )
		print frame_num
		cannonball_animation_frame( cannon, frame_num, win )
		bird_animation_frame( bird, frame_num, win)
		win.update()
		if win.checkMouse():
			break
	for frame_num in range(65,300):
		time.sleep( 0.05 )
		bird_animation_frame( bird, frame_num, win)
		'''make bird go faster here to avoid boat on fire'''
		fire = []
		c = gr.Circle( gr.Point(800, 300), 10)
		c.draw( win )
		fire.append( c )
		for item in fire:
			dx = random.randint( -80, 80 )
			dy = random.randint( -115, 100 )
			item.move( dx, dy )	
			hot = [ gr.color_rgb( 255, 255, 0 ), gr.color_rgb( 255, 0, 0 ),
			gr.color_rgb( 255, 69, 0 ), gr.color_rgb(255,165,0)]
			item.setFill( random.choice(hot) )
		if random.random() < 0.2:
			oldshape = random.choice( fire )
			newshape = oldshape.clone()
			newshape.draw( win )
			fire.append( newshape )
			
		win.update()
		
		if win.checkMouse() != None:
			break 
	
	
	
	
	
	
	
	

	win.getMouse()
	win.close() 
	
if __name__ == "__main__":
	test_scene()
	