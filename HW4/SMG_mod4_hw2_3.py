#######
#Bullseye
#
#Sean Gregor
#
#desc: draw a target
#######

"""
start
    setup window as 'bullseye' with coordinates
    in main function:
        define circle parameters 
        set up list of colors
        for loop in range of [colors]
            define circle
            set color relative to list
            draw circle
end

"""

from graphics import *

#setup
win = GraphWin("Bullseye", 500, 500)
win.setBackground('grey')
win.setCoords(0,0,12,12)
#end of setup

def main():
    color = ['white', 'black', 'blue', 'red', 'yellow']
    radius = 5
    for i in range(0,5):
        circle = Circle(Point(6,6), radius - i)
        circle.setFill(color[0 + i])
        circle.draw(win)
    win.getMouse()
main()