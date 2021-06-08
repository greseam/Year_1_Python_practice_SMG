#####
# CONNECT THE DOTS
#
#By; Sean Gregor
#
#Desc:connect ten dots with lines
#####
'''
start
    setup graphics window as "10 dots"
    define shapes(circles) and labels(numbers)
    define a line to be redefined alot 
        for each click till 10 click
            set cirlce to position of click
            and send line to previous circle and new mouse click
        wait for click
end

'''

from graphics import *

#Setup
center=Point(350,300)#place holder value used in defining variables
win = GraphWin("10 Dots", 700, 600)
win.setBackground('white')
#end of setup

def circleSetup(circle,positonx,positony,number): #circle settings
    circle.draw(win)
    circle.setFill('yellow')
    circle.move(positonx-350,positony-300)
    number.draw(win)
    number.setFill('red')
    number.move(positonx-350,positony-300)

def main():
    #shape definitions
    graphCircle0 = Circle(Point(20,20),10)
    graphCircle1 = Circle(center,10)
    graphCircle2 = Circle(center,10)
    graphCircle3 = Circle(center,10)
    graphCircle4 = Circle(center,10)
    graphCircle5 = Circle(center,10)
    graphCircle6 = Circle(center,10)
    graphCircle7 = Circle(center,10)
    graphCircle8 = Circle(center,10)
    graphCircle9 = Circle(center,10)
    graphCircle10 = Circle(center,10)

    #label definitions
    titleLabel = Text(center,'TEN Clicks!!')
    num0 = Text(center,'')
    num1 = Text(center,'1')
    num2 = Text(center,'2')
    num3 = Text(center,'3')
    num4 = Text(center,'4')
    num5 = Text(center,'5')
    num6 = Text(center,'6')
    num7 = Text(center,'7')
    num8 = Text(center,'8')
    num9 = Text(center,'9')
    num10 = Text(center,'10')

    #line definition
    line0 = Line(center,center)
    
    #================#
    #Start of primary Events
    #================#
    titleLabel.draw(win)
    titleLabel.setFill('blue')
    titleLabel.setStyle('bold')
    titleLabel.move(0,-280)
    titleLabel.setSize(17)
    circleSetup(graphCircle0,370,320,num0)

    #1(circle)
    clickPosition = win.getMouse()
    clickPositionx = clickPosition.getX()
    clickPositiony = clickPosition.getY()
    circleSetup(graphCircle1,clickPositionx,clickPositiony,num1)
    line0 = Line(Point(40,40),Point(clickPositionx,clickPositiony))
    line0.draw(win)

    clickPosition1x = clickPositionx
    clickPosition1y = clickPositiony
    #2
    clickPosition = win.getMouse()
    clickPositionx = clickPosition.getX()
    clickPositiony = clickPosition.getY()
    circleSetup(graphCircle2,clickPositionx,clickPositiony,num2)
    line0 = Line(Point(clickPosition1x,clickPosition1y),Point(clickPositionx,clickPositiony))
    line0.draw(win)

    clickPosition1x = clickPositionx
    clickPosition1y = clickPositiony
    #3
    clickPosition = win.getMouse()
    clickPositionx = clickPosition.getX()
    clickPositiony = clickPosition.getY()
    circleSetup(graphCircle3,clickPositionx,clickPositiony,num3)
    line0 = Line(Point(clickPosition1x,clickPosition1y),Point(clickPositionx,clickPositiony))
    line0.draw(win)
    
    clickPosition1x = clickPositionx
    clickPosition1y = clickPositiony
    #4
    clickPosition = win.getMouse()
    clickPositionx = clickPosition.getX()
    clickPositiony = clickPosition.getY()
    circleSetup(graphCircle4,clickPositionx,clickPositiony,num4)
    line0 = Line(Point(clickPosition1x,clickPosition1y),Point(clickPositionx,clickPositiony))
    line0.draw(win)

    clickPosition1x = clickPositionx
    clickPosition1y = clickPositiony
    #5
    clickPosition = win.getMouse()
    clickPositionx = clickPosition.getX()
    clickPositiony = clickPosition.getY()
    circleSetup(graphCircle5,clickPositionx,clickPositiony,num5)
    line0 = Line(Point(clickPosition1x,clickPosition1y),Point(clickPositionx,clickPositiony))
    line0.draw(win)

    clickPosition1x = clickPositionx
    clickPosition1y = clickPositiony
    #6
    clickPosition = win.getMouse()
    clickPositionx = clickPosition.getX()
    clickPositiony = clickPosition.getY()
    circleSetup(graphCircle6,clickPositionx,clickPositiony,num6)
    line0 = Line(Point(clickPosition1x,clickPosition1y),Point(clickPositionx,clickPositiony))
    line0.draw(win)

    clickPosition1x = clickPositionx
    clickPosition1y = clickPositiony
    #7
    clickPosition = win.getMouse()
    clickPositionx = clickPosition.getX()
    clickPositiony = clickPosition.getY()
    circleSetup(graphCircle7,clickPositionx,clickPositiony,num7)
    line0 = Line(Point(clickPosition1x,clickPosition1y),Point(clickPositionx,clickPositiony))
    line0.draw(win)

    clickPosition1x = clickPositionx
    clickPosition1y = clickPositiony
    #8
    clickPosition = win.getMouse()
    clickPositionx = clickPosition.getX()
    clickPositiony = clickPosition.getY()
    circleSetup(graphCircle8,clickPositionx,clickPositiony,num8)
    line0 = Line(Point(clickPosition1x,clickPosition1y),Point(clickPositionx,clickPositiony))
    line0.draw(win)

    clickPosition1x = clickPositionx
    clickPosition1y = clickPositiony
    #9
    clickPosition = win.getMouse()
    clickPositionx = clickPosition.getX()
    clickPositiony = clickPosition.getY()
    circleSetup(graphCircle9,clickPositionx,clickPositiony,num9)
    line0 = Line(Point(clickPosition1x,clickPosition1y),Point(clickPositionx,clickPositiony))
    line0.draw(win)

    clickPosition1x = clickPositionx
    clickPosition1y = clickPositiony
    #10
    clickPosition = win.getMouse()
    clickPositionx = clickPosition.getX()
    clickPositiony = clickPosition.getY()
    circleSetup(graphCircle10,clickPositionx,clickPositiony,num10)
    line0 = Line(Point(clickPosition1x,clickPosition1y),Point(clickPositionx,clickPositiony))
    line0.draw(win)
    win.getMouse()
    win.setBackground('black')

    win.getMouse()
    #================#
    #End of primary Events
    #================#
main() # i know its not pretty but this one gave me the most trouble