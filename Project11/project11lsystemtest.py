# Tony Karalekas
# Spring 2015
# CS 151 Project 10
#
# project10lsystemtest.py version 1
#---------------------------------------------
#imports

import lsystem as ls
import shapes as s
import turtle as t
import turtle_interpreter as it
import tree

#===========================================================
t.tracer(False)



t1 = tree.Tree(filename= 'project11extension2a.txt')
t1.setIterations(3)
t1.setColor('OliveDrab')
t1.draw(-230, -200, 2, 90)
t2 = tree.Tree(filename= 'project11extension2b.txt')
t2.setIterations(3)
t2.setColor('LawnGreen')
t2.draw(215, -200, 2, 90)



if __name__ == "__main__":
	raw_input("Press enter to continue")	