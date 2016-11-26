# Tony Karalekas
# Spring 2015
# CS 151 Project 10
#
# indoorscene.py version 2
#---------------------------------------------
#imports

import lsystem as ls
import shapes as s
import turtle as t
import turtle_interpreter as it
import tree

#===========================================================
t.tracer(False)

#------------------------------------------------
#set-up code for the museum scene
#wall
def wall():
	t.up()
	t.goto(-800,-200)
	t.down()
	t.begin_fill()
	t.color("Beige")
	t.forward(1600)
	t.left(90)
	t.forward(1600)
	t.left(90)
	t.forward(1600)
	t.left(90)
	t.forward(1600)
	t.left(90)
	t.end_fill()
	
#floor
def floor():
	t.up()
	t.goto(-600, -200)
	t.down()
	for i in range(20):
		t.begin_fill()
		t.color("Black")
		t.forward(50)
		t.right(90)
		t.forward(50)
		t.right(90)
		t.forward(50)
		t.right(90)
		t.forward(50)
		t.right(90)
		t.forward(50)
		t.end_fill()
		t.begin_fill()
		t.color("White")
		t.forward(50)
		t.right(90)
		t.forward(50)
		t.right(90)
		t.forward(50)
		t.right(90)
		t.forward(50)
		t.right(90)
		t.forward(50)
		t.end_fill()
	t.up()
	t.down()
	t.goto(-1000, -250)
	for i in range(20):
		t.begin_fill()
		t.color("White")
		t.forward(50)
		t.right(90)
		t.forward(50)
		t.right(90)
		t.forward(50)
		t.right(90)
		t.forward(50)
		t.right(90)
		t.forward(50)
		t.end_fill()
		t.begin_fill()
		t.color("Black")
		t.forward(50)
		t.right(90)
		t.forward(50)
		t.right(90)
		t.forward(50)
		t.right(90)
		t.forward(50)
		t.right(90)
		t.forward(50)
		t.end_fill()
	t.up()
	t.goto(-600, -300)
	t.down()
	for i in range(20):
		t.begin_fill()
		t.color("Black")
		t.forward(50)
		t.right(90)
		t.forward(50)
		t.right(90)
		t.forward(50)
		t.right(90)
		t.forward(50)
		t.right(90)
		t.forward(50)
		t.end_fill()
		t.begin_fill()
		t.color("White")
		t.forward(50)
		t.right(90)
		t.forward(50)
		t.right(90)
		t.forward(50)
		t.right(90)
		t.forward(50)
		t.right(90)
		t.forward(50)
		t.end_fill()


#------------------------------------------
# now this is where we put to use our new line styles 
# in order to make the paintings look more handdrawn 

# painting function with new code
def paintings():
	# painting number 1
	'''hand drawn with jitter style'''
	art = s.Square(300, ('Black'))
	art.setStyle('jitter3')
	art.setJitter(4)
	art.draw(-600, -100, 1, 90)
	'''now i will add art to the painting'''
	#pentagon with jitter3 style
	p = s.Pentagon(75, (0,0,0))
 	p.setColor('DarkOrchid')
 	p.setStyle('jitter3')
 	p.setJitter(4)
 	p.draw(-100, -50, 1, 90)
 	#normal star
 	st = s.Star(50, (0,0,0))
	st.setColor('Red')
	st.draw(50, 120, 1, 90)
	#normal diamond
	d = s.Diamond(50, (0,0,0))
	d.setColor('Blue')
	d.draw(-100, 125, 1, 90)
	
	
	# painting number 2
	'''hand drawn with dotted style'''
	art1 = s.Square(300, ('Black'))
	art1.setStyle('dotted')
	art1.setDotSize(3)
	art1.draw(-150, -100, 1, 90)
	
	'''now i will add art to the painting'''
	#diamond with jitter style
	d = s.Diamond(50, (0,0,0))
	d.setColor('CadetBlue')
	d.setStyle('jitter')
	d.setJitter(3)
	d.draw(-400, 125, 1, 90)
	#cross with dotted style
	c = s.Cross(30, (0,0,0))
	c.setColor('LightCoral')
	c.setStyle('dotted')
	c.setDotSize(3)
	c.draw(-500, 45, 1, 90)
	
	
	# painting number 3
	'''hand drawn with jitter3 style'''
	art2 = s.Square(300, ('Black'))
	art2.setStyle('jitter3')
	art2.setJitter(5)
	art2.draw(300, -100, 1, 90)
	
	'''now i will add art to the painting'''
	#normal cross
	c = s.Cross(15, (0,0,0))
	c.setColor('LightCoral')
	c.draw(350, 110, 1, 90)
	#pentagon with dotted style
	p = s.Pentagon(75, (0,0,0))
 	p.setColor('OliveDrab')
 	p.setStyle('dotted')
	p.setDotSize(3)
 	p.draw(370, -65, 1, 90)
 	#star with jitter3 style
 	st = s.Star(50, (0,0,0))
	st.setColor('Goldenrod')
	st.setStyle('jitter3')
 	st.setJitter(4)
	st.draw(500, 120, 1, 90)
	


	#trees for museum decoration
	t1 = tree.Tree(filename= 'project10lsystem.txt')
	t1.setIterations(3)
	t1.setColor('OliveDrab')
	t1.draw(-230, -200, 1, 90)
	t2 = tree.Tree(filename= 'project10lsystem.txt')
	t2.setIterations(3)
	t2.setColor('LawnGreen')
	t2.draw(215, -200, 1, 90)






  	







if __name__ == "__main__":
	floor()
	wall()
	paintings()
	raw_input("Press enter to continue")	