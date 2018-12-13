#CTI 110
#Area of Rectangle excercise
#Darius Green
#13NOV18

#Ask user to input legth and width of two rectangles.
#Split into A and B.

lengthA= int(input("Enter the length of rectangleA: "))
widthA= int(input("Enter the length of rectangleB: "))

lengthB= int(input("Enter the length of rectangle B: "))
widthB= int(input("Enter the legnth of rectangle B: "))

#Process the area of rectangle A and B.
areaA= lengthA * widthA

areaB= lengthB * widthB

#Three possible outcomes, produce the layout.
#Display which has the greatest area.

if areaA> areaB:
    print("Rectangle A has the greatest area.")

elif areaB> areaA:
    print("Rectangle B has the greatest area.")

else:
    print("Both have the same area")
    
