#######
# OUR HOUSE, IN THE MIDDLE OF THE STREET....
#
# Sean Gregor
#
#Desc: draw a house in five clicks
#######
"""
start
    Setup window with name "house"
    in main function:
        get click in lower left corner of frame
            output text to inform user
            make a point there
        get click in upper right corner
            output text to inform user
            make rectangle with previous point and new click pont!!
        get click on center of the top of the door
            output text to inform user
            make a 'door' rectangle  with new click point and first click point incremented to right
                color red
        get click on center of the window 
            output text to inform user 
            make a square with new click point and first click point incremented up and to the right
        get click on the peak of the roof
            output text to inform user
            make a triangle with previous new click point, current click point, and first click incremented up to the same Y as previous click point
        get click to exit
            output text to inform user  
end
"""
from graphics import *

#setup
win = GraphWin("House", 500, 500)
win.setCoords(0,0,12,12)

text = ['click in the lower left corner.','click for upper right corner of house','click on center of the top of the door','click on center of the window','click on the peak of the roof','click any where to quit']
points = []
clicks = []
color = ['','','','','black']
#end of setup
def main():
    for i in range(0,5):
        descriptionText = Text(Point(6,1),text[len(clicks)])
        descriptionText.draw(win)
        newClickPoint = win.getMouse()
        points.extend([newClickPoint])
        clicks.extend([newClickPoint])
        if len(clicks) == 2: #make rectangle
            points.insert(1,Point(points[1].getX(),points[0].getY()))
            points.append(Point(points[0].getX(),points[2].getY()))
        if len(clicks) == 3:#make rectangle
            redDoor = Rectangle(Point(points[4].getX() - .8,points[0].getY()),Point(points[4].getX()+.8,points[4].getY()))
            redDoor.draw(win)
            redDoor.setFill('red')
            points.pop()
        if len(clicks) == 4:#make square
            window = Rectangle(Point(points[4].getX()+.5,points[4].getY()+.5),Point(points[4].getX()-.5,points[4].getY()-.5))
            window.draw(win)
            points.pop()
        if len(clicks) == 5:#make Triangle
            points.insert(4,Point(points[4].getX(),points[4].getY()))
            points.append(Point(points[2].getX(),points[2].getY()))
            points.append(Point(points[4].getX(),points[4].getY()))
            points.pop(0)
            points.pop(0)
        firstPoint = Polygon(points)
        firstPoint.draw(win)
        firstPoint.setFill(color[i])
        descriptionText.undraw()
    descriptionText = Text(Point(6,1),text[5])
    descriptionText.draw(win)
    win.getMouse()
main() 