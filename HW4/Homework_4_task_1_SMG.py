#####
# SHAPES!!
#
#By : Sean Gregor
#
# Desc: to display various shapes with label on each mouse click.
##

from graphics import *
import math
#Setup
center=Point(250,250)
win = GraphWin("SHAPES!!!", 500, 500)
#end of setup

def textDescription(label): #label settings
    label.draw(win)
    label.setTextColor('white')
    label.setSize(12)
    label.setStyle('bold')

def removeText(label):
    label.undraw()
    
def main():
    
    # shape definitions
    start = Rectangle(Point(0,0),Point(500,500))
    circle = Circle(Point(250,250),(250/2))
    oval = Oval(Point(100,150),Point(400,350))
    square = Rectangle(Point(500-375,500-375),Point(375,375))
    rectange = Rectangle(Point(100,175),Point(400,325))
    triangle = Polygon(Point(250,100),Point(125,350),Point(375,350))
    polygon = Polygon(Point(250,125),Point(375,175),Point(375,325),Point(250,375),Point(125,325),Point(125,175))
    finish = Rectangle(Point(0,0),Point(500,500)) 

    #label definitions
    label0 = Text(center,"SHAPES!!!")
    label1 = Text(center,"CIRCLE")
    label2 = Text(center,"OVAL")
    label3 = Text(center,'SQUARE')
    label4 = Text(center,'RECTANGLE')
    label5 = Text(center,'TRIANGLE')
    label6 = Text(center,'HEXAGON')
    label7 = Text(center,'End')

    #===============#
    #Start of events
    #===============#
    start.draw(win)
    start.setFill('blue')
    textDescription(label0)
    #textDescription(label)
    win.getMouse()
    start.undraw()
    circle.draw(win)
    circle.setFill('blue')
    textDescription(label1)
    #label
    win.getMouse()
    circle.undraw()
    oval.draw(win)
    oval.setFill('blue')
    textDescription(label2)
    #label
    win.getMouse()
    oval.undraw()
    square.draw(win)
    square.setFill('blue')
    textDescription(label3)
    #label
    win.getMouse()
    square.undraw()
    rectange.draw(win)
    rectange.setFill('blue')
    textDescription(label4)
    #label
    win.getMouse()
    rectange.undraw()
    triangle.draw(win)
    triangle.setFill('blue')
    textDescription(label5)
    #label
    win.getMouse()
    triangle.undraw()
    polygon.draw(win)
    polygon.setFill('blue')
    textDescription(label6)
    win.getMouse()
    polygon.undraw()
    finish.draw(win)
    finish.setFill('blue')
    textDescription(label7)
    #==============#
    #End of Events
    #Click to end program
    #==============#
    win.getMouse()
main()