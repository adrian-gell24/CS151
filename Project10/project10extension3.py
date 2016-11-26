# Tony Karalekas
# Spring 2015
# CS 151 Project 10
#
# project10extension3.py
#---------------------------------------------
#imports


import lsystem as ls
import shapes as s
import turtle as t
import turtle_interpreter as it
import tree

#===========================================================
t.tracer(False)


'''goal of this extension is to create a scene
	that incorporates the first and second 
	extensions into a adjusted scene'''

#------------------------------------------------
#set-up code for the museum scene
#wall
def wall():
	t.up()
	t.goto(-800,-200)
	t.down()
	t.begin_fill()
	t.color("LightBlue")
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
	art = s.Square(185, ('Black'))
	art.setStyle('slash')
	art.setJitter(4)
	art.draw(-525, -100, 1, 90)
	
	'''now i will add art to the painting'''
	t1 = tree.Tree(filename= 'project10extension2.txt')
	t1.setIterations(3)
	t1.setColor('LawnGreen')
	t1.draw(-400, -100, 1, 90)
	
	
	# painting number 2
	'''hand drawn with dotted style'''
	art1 = s.Square(185, ('Black'))
	art1.setStyle('slash')
	art1.setDotSize(3)
	art1.draw(-150, -100, 1, 90)
	
	'''now i will add art to the painting'''
	t2 = tree.Tree(filename= 'project10extension2.txt')
	t2.setIterations(3)
	t2.setColor('OliveDrab')
	t2.draw(0, -100, 1, 90)
	
	
	# painting number 3
	'''hand drawn with jitter3 style'''
	art2 = s.Square(185, ('Black'))
	art2.setStyle('slash')
	art2.setJitter(5)
	art2.draw(225, -100, 1, 90)
	
	'''now i will add art to the painting'''
	t3 = tree.Tree(filename= 'project10extension2.txt')
	t3.setIterations(3)
	t3.setColor('Green')
	t3.draw(400, -100, 1, 90)




if __name__ == "__main__":
	floor()
	wall()
	paintings()
	raw_input("Press enter to continue")	