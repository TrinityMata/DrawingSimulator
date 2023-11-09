# -*- coding: utf-8 -*-
"""
------------------------------------------------------------------------------
   Name:     TM_Final_Programming_Project
   Author:   Trinity Mata
   Date:     May 2, 2022
   Language: Python
   Purpose:  The purpose of this program is to display a drawing simulator. 
             The user first chooses to draw a rectangle, a circle, or a line. 
             which will be represented by buttons. Then they will choose 
             a color from the choice of red, green, blue, orange, yellow, 
             purple, black, white, or random. The color choices will also be 
             represented by buttons. This repeats until the user pushes the 
             “Done” button at the bottom of the window. The program will then 
             present the user’s final image.

------------------------------------------------------------------------------
   ChangeLog:
   Who:      Trinity Mata            Date:     May 2, 2022
   Desc.:    This is the original version of the code. 
------------------------------------------------------------------------------
   ChangeLog:
   Who:      Trinity Mata            Date:     May 17, 2022
   Desc.:    The process of creating the circle has been changed to allow the 
             user to click where they want the circle to be first instead of 
             entering the radius first through an entry object. Then the user 
             will click how far away from the center point they want their 
             circle to be (AKA the radius). I also adjusted the pickAColor 
             function to allow the user to click places that are not buttons 
             without the program crashing.
------------------------------------------------------------------------------
"""

from graphics import *
import random
import math

def ifClicked(mouse, x1, x2, y1, y2):
    """This function returns true if the mouse is inside the box created by the 
    x's and y's."""
    if mouse.getX() >= x1 and mouse.getX() <= x2:
        if mouse.getY() >= y1 and mouse.getY() <= y2:
            return True
        else:
            return False
    else:
        return False
    
def isWithinCanvas(x, y, radius = None):
    """This function returns true if the point is within the canvas boundries 
    and false if it is not. If the shape has a radius, it will account for that."""
    if radius != None:
        if (x - radius) >= 25 and (x + radius) <= 775:
            if (y - radius) >= 70 and (y + radius) <= 520:
                return True
            else:
                return False
        else:
            return False
    else:
        if x >= 25 and x <= 775:
            if y >= 70 and y <= 520:
                return True
            else:
                return False
        else:
            return False
    
def drawShapes():
    #Drawing the shapes and text in the window
    shapeText.draw(win)
    
    CircleButton.draw(win)
    CircleText.draw(win)
    
    RectButton.draw(win)
    RectText.draw(win)
    
    LineButton.draw(win)
    LineText.draw(win)

def unDrawShapes():
    #Undraw all of the buttons and text 
    shapeText.undraw()
    
    CircleButton.undraw()
    CircleText.undraw()
    
    RectButton.undraw()
    RectText.undraw()
    
    LineButton.undraw()
    LineText.undraw() 

def unDrawColors(rbtn,obtn,ybtn,gbtn,blubtn,pbtn,blkbtn,wbtn,randbtn,randtxt):
    #Undraws the color options
    rbtn.undraw()
    obtn.undraw()
    ybtn.undraw()
    gbtn.undraw()
    blubtn.undraw()
    pbtn.undraw()
    blkbtn.undraw()
    wbtn.undraw()
    randbtn.undraw()
    randtxt.undraw()

def pickAColor():
    """This function asks the user for what color they want to fill in their 
    shape."""
    #Constructing the color options as buttons (red, orange, yellow, green, blue, 
    #purple, black, white, and random)
    redButton = Circle(Point(100, 575), 25)
    redButton.setFill("red")
    redButton.draw(win)
    orangeButton = Circle(Point(155, 575), 25)
    orangeButton.setFill("orange")
    orangeButton.draw(win)
    yellowButton = Circle(Point(215, 575), 25)
    yellowButton.setFill("yellow")
    yellowButton.draw(win)
    greenButton = Circle(Point(275, 575), 25)
    greenButton.setFill("green")
    greenButton.draw(win)
    blueButton = Circle(Point(335, 575), 25)
    blueButton.setFill("blue")
    blueButton.draw(win)
    purpleButton = Circle(Point(395, 575), 25)
    purpleButton.setFill("purple")
    purpleButton.draw(win)
    blackButton = Circle(Point(455, 575), 25)
    blackButton.setFill("black")
    blackButton.draw(win)
    whiteButton = Circle(Point(515, 575), 25)
    whiteButton.draw(win)
    randomButton = Circle(Point(575, 575), 25)
    randomButton.draw(win)
    randomText = Text(Point(575, 575), "Random")
    randomText.setSize(10)
    randomText.draw(win)
    
    #Text that provides instruction on picking a color
    colorText = Text(Point(400, 55), "Please choose what color to fill the shape")
    colorText.setSize(15)
    colorText.draw(win)
    
    bln = False
    while not bln:
        #Action depending on what button is pressed
        colorClick = win.getMouse()
        #If the red button is clicked
        if ifClicked(colorClick, 75, 125, 550, 600):
            color = "red"
            bln = True
        #If the orange button is clicked
        elif ifClicked(colorClick, 130, 180, 550, 600):
            color = "orange"
            bln = True
        #If the yellow button is clicked
        elif ifClicked(colorClick, 190, 240, 550, 600):
            color = "yellow"
            bln = True
        #If the green button is clicked
        elif ifClicked(colorClick, 250, 300, 550, 600):
            color = "green"
            bln = True
        #If the blue button is clicked
        elif ifClicked(colorClick, 310, 360, 550, 600):
            color = "blue"
            bln = True
        #If the purple button is clicked
        elif ifClicked(colorClick, 370, 420, 550, 600):
            color = "purple"
            bln = True
        #If the black button is clicked
        elif ifClicked(colorClick, 430, 480, 550, 600):
            color = "black"
            bln = True
        #If the white button is clicked
        elif ifClicked(colorClick, 490, 540, 550, 600):
            color = "white"
            bln = True
        #If the random button is clicked
        elif ifClicked(colorClick, 550, 600, 550, 600):
            color = color_rgb(random.randint(0,225), random.randint(0,225), 
                                  random.randint(0,225))
            bln = True
    
    #Undrawing the color buttons and text
    unDrawColors(redButton, orangeButton, yellowButton, greenButton, blueButton, 
                 purpleButton, blackButton, whiteButton, randomButton, randomText)
    colorText.undraw()
    #Returning the color
    return color
    


win = GraphWin("Drawing Simulator", 800, 650)

#Creating the start text that welcomes the user to the drawing simulator
startText = Text(Point(400, 25), "Welcome to the Drawing Simulater.")
startText.setSize(24)
startText.draw(win)

#Creating the canvas that the user will be able to draw on
canvas = Rectangle(Point(25, 70), Point(775, 520))
canvas.setFill("light gray")
canvas.draw(win)

#The following 5 shapes and texts are purposely not drawn
#Telling the user to choose the shape they want to use 
shapeText = Text(Point(400, 55), "Please choose what shape you want to draw.")
shapeText.setSize(15)

#Circle shape button and text
CircleButton = Circle(Point(150,575),30)
CircleButton.setOutline("black")
CircleButton.setWidth(3)
CircleText = Text(Point(150,625), "Circle")

#Rectangle shape button and text
RectButton = Rectangle(Point(300,550),Point(400, 600))
RectButton.setOutline("black")
RectButton.setWidth(3)
RectText = Text(Point(350,625), "Rectangle")

#Line shape button and text
LineButton = Line(Point(515,600), Point(615,550))
LineButton.setWidth(3)
LineText = Text(Point(565,625), "Line")

#Done Button and text
DoneButton = Rectangle(Point(715,545), Point(775,575))
DoneButton.setFill("red")
DoneButton.draw(win)
DoneText = Text(Point(745, 560), "Done")
DoneText.setStyle("bold")
DoneText.draw(win)
    
#This starts a loop that only stops when the done button is pressed
blnDone = False
while not blnDone:
    drawShapes()
    
    click = win.getMouse()
    #If the circle was clicked
    if ifClicked(click,120,180,545,605) == True:
        #Get input to create circle (mouse click and entry box)
        unDrawShapes()       
        
        #The user will click where they want the center of the circle to be
        circleShapeText = Text(Point(400, 55), "Please click where you want to" 
                               + " put the circle.")
        circleShapeText.setSize(15)
        circleShapeText.draw(win)
        
        #Making sure the first click is within the canvas and drawing a point 
        #for the user to have as a reference
        bln = False
        while not bln:
            circleClick = win.getMouse()
            if isWithinCanvas(int(circleClick.getX()), int(circleClick.getY())) == False:
                circleShapeText.setText("That was not within the canvas, please " 
                                  + "click again")
            else:
                bln = True
                center = Circle(Point(int(circleClick.getX()), 
                                      int(circleClick.getY())), 5)
                center.setFill("black")
                center.draw(win)
        
        #Asking for the radius
        circleShapeText.setText("Now click how far out you want the circle to " 
                                + "be from the current point.")
        
        #Loops until the radius click is inside the canvas and the radius will 
        #not make the circle go off the canvas
        bln = False
        while not bln:
            radClick = win.getMouse()
            if isWithinCanvas(int(radClick.getX()), int(radClick.getY())) == False:
                circleShapeText.setText("That was not within the canvas, please " 
                                        + "click again")
            else:
                #Distance formula: sqrt((x1-x2)**2 + (y1-y2)**2)
                radius = math.sqrt((int(circleClick.getX()) 
                                    - int(radClick.getX()))**2 
                                   + (int(circleClick.getY()) 
                                      - int(radClick.getY()))**2)
                #Checking if the radius will cause the circle to be outside of 
                #the canvas
                if isWithinCanvas(int(circleClick.getX()), int(circleClick.getY()), 
                                  radius) == False:
                    circleShapeText.setText("The circle not within the canvas," 
                                            + " please click again")
                else:
                    bln = True
                    center.undraw()
        
        #Constructing the circle
        circleShape = Circle(Point(int(circleClick.getX()), 
                                   int(circleClick.getY())), radius)
        circleShape.draw(win)
        
        #Undrawing the instructions text
        circleShapeText.undraw()
        
        #Picking the color of the shape
        circleColor = pickAColor()
        circleShape.setFill(circleColor)
        
    #If the Rectangle is clicked
    elif ifClicked(click,300,400,550,600) == True:
        #Get input to create Rectangle (two mouse clicks)
        unDrawShapes()
        
        #Prompting the user to click where they would like their rectangle to be
        rectShapeText = Text(Point(400,55), "Please click where you would like" 
                             + " one corner of the rectangle.")
        rectShapeText.setSize(15)
        rectShapeText.draw(win)
        
        #Making sure the first click was inside the canvas
        bln = False
        while not bln:
            p1 = win.getMouse()
            if isWithinCanvas(int(p1.getX()), int(p1.getY())) == False:
                rectShapeText.setText("That was not within the canvas, please " 
                                  + "click again")
            else:
                bln = True
                corner1 = Circle(Point(int(p1.getX()), int(p1.getY())), 5)
                corner1.setFill("black")
                corner1.draw(win)
        
        rectShapeText.setText("Please click where you would like the opposite " 
                              +"corner of your current corner. \n(top-right to" 
                              +" botton-left or top-left to bottom-right)")
        rectShapeText.setSize(10)
        
        #Making sure the second click was inside the canvas
        bln = False
        while not bln:
            p2 = win.getMouse()
            if isWithinCanvas(int(p2.getX()), int(p2.getY())) == False:
                rectShapeText.setText("That was not within the canvas, please " 
                                  + "click again")
            else:
                bln = True
                corner1.undraw()
                #Constructing the shape
                rectShape = Rectangle(Point(int(p1.getX()), int(p1.getY())), 
                                      Point(int(p2.getX()), int(p2.getY())))
                rectShape.draw(win)
        
        #Undrawing the instructions text
        rectShapeText.undraw()
        
        #Picking the color of the shape
        rectColor = pickAColor()
        rectShape.setFill(rectColor)
    
    #If the line is clicked
    elif ifClicked(click,515,615,550,600) == True:
        #Get input to create Line (two mouse clicks)
        unDrawShapes()
        
        #Prompting the user to click where they would like their line to be
        lineShapeText = Text(Point(400,55), "Please click where you would like" 
                             + " one point of the line.")
        lineShapeText.setSize(15)
        lineShapeText.draw(win)
        
        #Making sure the first click was inside the canvas
        bln = False
        while not bln:
            p1 = win.getMouse()
            if isWithinCanvas(int(p1.getX()), int(p1.getY())) == False:
                lineShapeText.setText("That was not within the canvas, please " 
                                  + "click again")
            else:
                bln = True
                point1 = Circle(Point(int(p1.getX()), int(p1.getY())), 5)
                point1.setFill("black")
                point1.draw(win)
        
        #Giving instructions for second point
        lineShapeText.setText("Please click where you would like the end point" 
                              + " of our line to be.")
        
        #Making sure the first click was inside the canvas
        bln = False
        while not bln:
            p2 = win.getMouse()
            if isWithinCanvas(int(p2.getX()), int(p2.getY())) == False:
                lineShapeText.setText("That was not within the canvas, please " 
                                  + "click again")
            else:
                bln = True
                point1.undraw()
                #Constructing the line
                lineShape = Line(Point(int(p1.getX()), int(p1.getY())), 
                                 Point(int(p2.getX()), int(p2.getY())))
                lineShape.draw(win)
        
        #Undrawing the instructions text
        lineShapeText.undraw()
        
        #Picking the color of the shape
        lineColor = pickAColor()
        lineShape.setOutline(lineColor)
        
        
    #If Done button is clicked
    elif ifClicked(click, 715, 775, 545, 575) == True:
        blnDone = True
    #The following else statement prevents the program from crashing if the 
    #user does not click any of the above buttons
    else:
        unDrawShapes()
        
"""After the user has drawn all of the shapes they want to and have pressed the 
done button, all of the buttons and text will be undrawn and the canvas will 
turn white to show the user their finished image. The user will then be able 
to sign their art."""
unDrawShapes()
startText.undraw()
DoneButton.undraw()
DoneText.undraw()
canvas.setFill("white")

#Creating the instructions, the entry box, and the entry button
signText = Text(Point(400, 55), "Please sign your name.")
signText.setSize(15)
signText.draw(win)
signBox = Entry(Point(680, 505), 20)
signBox.draw(win)
signButton = Rectangle(Point(680, 546), Point(714, 560))
signButton.setFill("green")
signButton.draw(win)
signButtonLabel = Text(Point(697, 553), "Sign")
signButtonLabel.setSize(10)
signButtonLabel.draw(win)

#When the user clicks the button, the program will get the signature
bln = False
while not bln:
    signClick = win.getMouse()
    if ifClicked(signClick, 680, 714, 546, 560):
        signature = signBox.getText()
        bln = True
    else:
        signText.setText("Please click the 'sign' button when done.")

#undrawing the instructions, the entry box, and the entry button
signText.undraw()
signBox.undraw()
signButton.undraw()
signButtonLabel.undraw()

#Signature text
signatureText = Text(Point(680, 505), signature)
signatureText.draw(win)

#Once they are done signing their art, they will click the 'Done' button to 
#close the window
signText.setText("Please click the 'Done' button to close the window.")
signText.draw(win)
DoneButton.draw(win)
DoneText.draw(win)

#The following will loop until the 'Done' button is clicked
bln = False
while not bln:
    doneClick = win.getMouse()
    if ifClicked(click, 715, 775, 545, 575):
        bln = True
        win.close()    
    