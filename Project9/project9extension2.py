# Tony Karalekas
# Spring 2015
# CS 151 Project 9
#
# Extension 2
#---------------------------------------------
#imports

import lsystem as ls
import shapes as s
import turtle
import turtle_interpreter as it

#===========================================================

def tile(x, y, scale):

	# draw the pentagon tiles
	p = s.Pentagon(scale, (0,0,0))
	p.setColor("Aquamarine")
	p.draw(x, y, 50, 108)
	p.setColor("Blue")
	p.draw(x+12.5, y+15, 25, 108)
	
	# draw cross tiles
	c = s.Cross(scale, (0,0,0))
	c.setColor("Red")
	c.draw(x+65, y-10, 15, 90)
	c.setColor('Green')
	c.draw(x+70, y-15, 5, 90)
	
	st= s.Star(scale, (0,0,0))
	st.setColor("Gold")
	st.draw(x+22.5, y+35, 7, 90)


def mosaic(x, y, scale, Nx, Ny):
	for i in range(Nx):
		for j in range(Ny):
			tile(x+100*i, y+100*j, scale)
			
			
def main():
	mosaic(-250, -250, 1, 5, 5)
	
	#wait	
	it.TurtleInterpreter().hold()
	
if __name__ == "__main__":
	main()