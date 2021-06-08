#######
# bar graph
#
# Sean Gregor
#
# a bar graph that will display the input prompt than tha graph
#######

from graphics import *

def main():
    # Creating graph window1
   
    win2 = GraphWin("Investment Growth Chart", 600, 500)
    win2.setCoords(-2, -200, 12, 10400)

    textDescription = Text(Point(6,7000),'Plotting a 10 year investment\nEnter the info below and click anywhere to graph it')
    textP = Text(Point(1,5000),'Initial Principle: ')
    textR = Text(Point(1,4000),'Annual Intrest: ')
    initialPrincipal = Entry(Point(4,5000),10)
    initialPrincipal.setText("0")
    initialPrincipal.draw(win2)
    textP.draw(win2)
    annualIntrest = Entry(Point(4,4000),10)
    annualIntrest.setText("0.0")
    annualIntrest.draw(win2)
    textR.draw(win2)
    textDescription.draw(win2)


    win2.getMouse()
    user_initial = eval(initialPrincipal.getText())
    user_annual = eval(annualIntrest.getText())
    win2.close()

    win = GraphWin("Investment Growth Chart", 600, 500)
    win.setCoords(-2, -200, 12, 10400)

    # Setting text for the graph

    Text(Point(-1, 0), "0.0K").draw(win)
    Text(Point(-1, 2500), "2.5K").draw(win)
    Text(Point(-1, 5000), "5.0K").draw(win)
    Text(Point(-1, 7500), "7.5K").draw(win)
    Text(Point(-1, 10000), "10.0K").draw(win)
    # Creating initial prinicpal bar
    bar = Rectangle(Point(0, 0), Point(1, user_initial))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
    # Creating the rest of the bars

    for year in range(1,11):

        # Calculate the value for next year

        user_initial = user_initial * (1 + user_annual)

        # Draw bar for this value

        bar = Rectangle(Point(year, 0), Point(year + 1, user_initial))

        bar.setFill("green")

        bar.setWidth(2)

        bar.draw(win)

    # Waiting for user to click before closing

    win.getMouse()
main()