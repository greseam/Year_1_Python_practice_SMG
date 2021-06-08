#####
# Area of a Circle
#
# By: Sean Gregor
#
# Desc: to find and show the area of a circle
######

from graphics import *
import math

#Setup
center=Point(11,8)
win = GraphWin("Area of a Circle", 700, 500)
win.setBackground('pink')
win.setCoords(0,0,22,16)
#end of setup

def calculate(radius):
    area = math.pi * (int(radius) ** 2) #formula for area
    return area
def calculateDiameter(radius):
    diameter = int(radius) * 2
    return diameter


def textSetup(label,color,size,coordX,coordY):
    label.draw(win)
    label.setTextColor(color)
    label.setSize(size)
    label.setStyle('bold')
    label.move(coordX-11,coordY-8)

def createArrow(line,arrow,color):
    line.setArrow(arrow)
    line.draw(win)
    line.setFill(color)



def main():
    #shape definitions
    graphCircle = Circle(Point(15,8),5)
    radiusLine = Line(Point(15,8),Point(15,13))
    diameterLine = Line(Point(10,8),Point(20,8))
    userInputRadius = Entry(Point(5.7,10),6)
    submitBox = Rectangle(Point(4,8.5),Point(6,7.5))

    #label definitions
    titleLabel = Text(center,'Area of A Circle')
    radiusLabel = Text(center,'radius= ' + str(userInputRadius.getText()))
    diameterLabel = Text(center,'diameter= ')#+str(round(calculateDiameter(input)))
    userInputLabel = Text(center, 'Enter a Radius: ')
    submitLabel = Text(center,'Submit')
    quitLable = Text(center,'Quit')
    areaLabel = Text(center,'Area of a Circle is: ')
    areaAwnser = Text(center,'placeholder')#round(calculate(userInputRadius.getText()),2)

    #================#
    #Start of primary Events
    #================#
    textSetup(titleLabel,'red',18,11,15)
    graphCircle.draw(win)
    graphCircle.setFill('yellow')
    textSetup(userInputLabel,'red',11,3,10)
    submitBox.draw(win)
    submitBox.setFill('black') 
    textSetup(submitLabel,'white',10,5,8)   
    userInputRadius.draw(win)
    win.getMouse()

    radiusLabel.setText('radius= '+str(userInputRadius.getText()))
    diameterLabel.setText('diameter= '+ str(calculateDiameter(userInputRadius.getText())))
    areaAwnser.setText(round(calculate(userInputRadius.getText()),2))
    submitLabel.undraw()
    textSetup(radiusLabel,'red',7,16,11)
    createArrow(radiusLine,'last','red')
    textSetup(diameterLabel,'blue',7,17,8.5)
    createArrow(diameterLine,'both','blue')
    textSetup(quitLable,'white',10,5,8)
    textSetup(areaLabel,'red',9,4,5)
    textSetup(areaAwnser,'black',9,7,5)
    win.getMouse()
    #================#
    #End of primary Events
    #================#

main()