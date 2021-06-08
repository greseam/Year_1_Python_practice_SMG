#######
# CLOCK!!!
#
# Sean Gregor
#
# Desc: Show 12 positions on a clock
#######
'''
start                                         Check list
    setup graphics window as 'clock'                !
    define lines and set as arrows                  !
    define other shapes and labels                  !
    wait for click                                  !
        display clock with no arms                  !
        wait for click in range of 13               !
            display arm relative to click           !
            display label relative to arm           !
        wait for ending click                       !
end
'''
from graphics import *

#setup
win = GraphWin("Clock", 500, 500)
win.setBackground('black')
center = Point(250,250)
#end of setup

def shapeSetup(shape,color):
    shape.draw(win)
    shape.setOutline(color)

def lineSetup(line,arrow,color):
    line.draw(win)
    line.setArrow(arrow)
    line.setOutline(color)

def labelSetup(label,style,size,color):
    label.draw(win)
    label.setStyle(style)
    label.setSize(size)
    label.setTextColor(color)

def main():
    #shape definitions
    clock = Circle(center,175)

    #line definition
    arrow_1 = Line(center,Point(300,150))
    arrow_2 = Line(center,Point(350,200))
    arrow_3 = Line(center,Point(400,250))
    arrow_4 = Line(center,Point(350,300))
    arrow_5 = Line(center,Point(300,350))
    arrow_6 = Line(center,Point(250,400)) 
    arrow_7 = Line(center,Point(200,350))
    arrow_8 = Line(center,Point(150,300))
    arrow_9 = Line(center,Point(100,250))
    arrow_10 = Line(center,Point(150,200))
    arrow_11 = Line(center,Point(200,150))
    arrow_12 = Line(center,Point(250,100))


    #label definitions
    clockTitle = Text(center,'CLOCK')
    arm_1 = Text(Point(300,150),'1')
    arm_2 = Text(Point(350,200),'2')
    arm_3 = Text(Point(400,250),'3')
    arm_4 = Text(Point(350,300),'4')
    arm_5 = Text(Point(300,350),'5')
    arm_6 = Text(Point(250,400),'6')
    arm_7 = Text(Point(200,350),'7')
    arm_8 = Text(Point(150,300),'8')
    arm_9 = Text(Point(100,250),'9')
    arm_10 = Text(Point(150,200),'10')
    arm_11 = Text(Point(200,150),'11')
    arm_12 = Text(Point(250,100),'12')

    #===============#
    #Start of Events
    #===============#
    labelSetup(clockTitle,'bold',16,'yellow')
    clockTitle.move(0,-200)
    win.getMouse()
    shapeSetup(clock,'yellow')
    win.getMouse()
    lineSetup(arrow_1,'last','yellow')
    labelSetup(arm_1,'bold',12,'red')
    win.getMouse() 
    lineSetup(arrow_2,'last','yellow')
    labelSetup(arm_2,'bold',12,'red')
    win.getMouse()
    lineSetup(arrow_3,'last','yellow')
    labelSetup(arm_3,'bold',12,'red')
    win.getMouse()
    lineSetup(arrow_4,'last','yellow')
    labelSetup(arm_4,'bold',12,'red')
    win.getMouse()
    lineSetup(arrow_5,'last','yellow')
    labelSetup(arm_5,'bold',12,'red')
    win.getMouse()
    lineSetup(arrow_6,'last','yellow')
    labelSetup(arm_6,'bold',12,'red')
    win.getMouse()
    lineSetup(arrow_7,'last','yellow')
    labelSetup(arm_7,'bold',12,'red')
    win.getMouse()
    lineSetup(arrow_8,'last','yellow')
    labelSetup(arm_8,'bold',12,'red')
    win.getMouse()
    lineSetup(arrow_9,'last','yellow')
    labelSetup(arm_9,'bold',12,'red')
    win.getMouse()
    lineSetup(arrow_10,'last','yellow')
    labelSetup(arm_10,'bold',12,'red')
    win.getMouse()
    lineSetup(arrow_11,'last','yellow')
    labelSetup(arm_11,'bold',12,'red')
    win.getMouse()
    lineSetup(arrow_12,'last','yellow')
    labelSetup(arm_12,'bold',12,'red')
    win.getMouse()
    #===============#
    #End of Events
    #===============#
main()
