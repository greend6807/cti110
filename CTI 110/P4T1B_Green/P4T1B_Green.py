#CTI-110
#P4TB_Green
#Darius Green
#11/20/18

import turtle           #Allows us to use turtle.
wn = turtle.Screen()    #Creates a playground for turtles
blues = turtle.Turtle() #Create a turtle, assign to blues

#Display options
blues.pensize(3)
blues.pencolor("purple")
blues.shape("turtle")

#Do first initial (D)
blues.left(90)
blues.forward(110)
blues.right(90)

for x in range(180):
    blues.forward(1)
    blues.right(1)

#Letter G
blues.penup()
blues.right(180)
blues.forward(100)
blues.left(90)
blues.forward(70)
blues.right(90)
blues.forward(90)
blues.pendown()
blues.left(110)

for i in range(325):
    blues.forward(1)
    blues.left(1)

blues.left(110)
blues.forward(50)


