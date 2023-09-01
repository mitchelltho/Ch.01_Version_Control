'''
1.0 Jedi Training (17pts)  Name:Thomas Mitchell


1. Define Forking (1pt): 
Forking is taking a program from a github repository and adding it to your own
2. Define Cloning (1pt): 
cloning is downloading something from your github repository onto your local computer
3. Define Branching (1pt):
branching is making different versions or branches of a program
4. Define Committing (1pt): 
committing saves the current version permanently as a version you can revert back to
5. Define Merging (1pt): 
merging is taking two versions of the program and combining them
6. Define Pushing (1pt):
pushing it taking the usually updated version of a program and replacing the old one with it on your github repositories
7. Define Pull Request (1pt):
pull requesting is asking the creator of a program to merge or accept your version of the program into the original version on their repository

8. TURTORIAL ART (10pts.)

Modify the starter code below to create your own cool drawing. 
Make sure you keep the last two lines of code!!!! 
Your first and last name must be written on your art.
The last line keeps the window open until you click to close.
Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''
import turtle
yoda=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor("white") # colors the screen
yoda.pensize(3) # width of pen line
yoda.speed(10)  # speed of drawing. Go fast to not waste time.
yoda.color("black")
yoda.circle(50)  #head
yoda.penup()
yoda.setpos(0,0)
yoda.pendown()
yoda.goto(0,-150)
yoda.goto(-75,-225)
yoda.penup()
yoda.setpos(0,-150)
yoda.pendown()
yoda.goto(75,-225)
yoda.penup()
yoda.setpos(0,-75)
yoda.pendown()
yoda.setpos(75,0)
yoda.penup()
yoda.setpos(0,-75)
yoda.pendown()
yoda.goto(-75,0)
yoda.penup()
yoda.goto(200,-300)
yoda.pencolor("black")


yoda.write('Thomas Mitchell',font=("Arial", 18, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
