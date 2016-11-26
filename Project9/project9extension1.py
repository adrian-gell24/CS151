# Tony Karalekas
# Spring 2015
# CS 151 Project 9
#
# Extension 1
#---------------------------------------------
#imports

import lsystem as ls
import shapes as s
import turtle
import turtle_interpreter as it

#===========================================================

def tile(x, y, scale):

	# draw the triangle tiles
	tri = s.Triangle(scale, (0,0,0))
	tri.setColor("SteelBlue")
	tri.draw(x, y, 85, 60)
	tri.setColor("Gold")
	tri.draw(x+135, y+80, 85, 240)
	
 	#draw stars
 	st = s.Star(scale, (0,0,0))
 	st.setColor("Salmon")
 	st.draw(x+40, y+30, 10, 90)
 	
 	#draw diamonds
 	d = s.Diamond(scale, (0,0,0))
 	d.setColor("DodgerBlue")
 	d.draw(x+85, y+55, 15, 60)



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