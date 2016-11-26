# Tony Karalekas
# Spring 2015
# CS 151 Project 9
#
# mosaic.py version 1
#---------------------------------------------
#imports

import lsystem as ls
import shapes as s
import turtle
import turtle_interpreter as it

#===========================================================

def tile(x, y, scale):

	# draw the square tiles
	sq = s.Square(scale, (0,0,0))
	sq.setColor("Aquamarine")
	sq.draw(x, y, 90, 90)
	
	#draw crosses
	c = s.Cross(scale, (0,0,0))
	c.setColor("Red")
	c.draw(x+45 ,y+45 , 7, 90)
	
	#draw stars
	st = s.Star(scale, (0,0,0))
	st.setColor("Orchid")
	st.draw(x+20, y+70, 10, 90)
	st.draw(x+70, y+20, 10, 90)
	
	#draw diamonds
	d = s.Diamond(scale, (0,0,0))
	d.setColor("DodgerBlue")
	d.draw(x+70, y+70, 15, 90)
	d.draw(x+15, y+20, 15, 90)


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