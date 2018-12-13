#CTI 110
#Areas of Rectangles
#Darius Green
#11/10/18

#Input the legnth and width of rectangle A.
lengthA= int(input("Enter the length of rectangle A: "))
widthA= int(input ("Enter the width of rectangle A: "))

#Input the legnth and width of rectangle B.
lengthB= int(input("Enter the length of rectangle B: "))
widthB= int(input ("Enter the width of rectangle B: "))

#Calculate the area of rectangle A.
areaA= lengthA * widthA

#Calculate the area of rectangle B.
areaB= lengthB * widthB

#Layout the three possible results of the processing. 
#Display which has the greatest area.

if areaA> areaB:
    print("Rectangle A has the greatest area.")

elif areaB> areaA:
    print("Rectangle B has the greatest area.")

else:
    print("Both have the same area")
    
