#CTI-110
#P4T1A_Green
#Darius Green
#11/20/18

import turtle           #Allows us to use turtle.
wn = turtle.Screen()    #Creates a playground for turtles
blues = turtle.Turtle() #Create a turtle, assign to blues

#Display options
blues.pensize(3)
blues.pencolor("blue")
blues.shape("turtle")


#Have the turtle draw out the shape you want.
#Square first.
#Use for or whole loops to execute.
for i in [0, 1, 2, 3]:
    blues.forward(100)
    blues.left(90)

#Reposition
blues.left (150)
blues.penup()
blues.forward(50)
blues.pendown()
blues.left (90)
#Triangle Second.
for x in [0, 1, 2, 3]:
    blues.forward(100)
    blues.left(120)














