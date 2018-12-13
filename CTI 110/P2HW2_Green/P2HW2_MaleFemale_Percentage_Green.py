#CTI 110
#Male and Female Percentages
#Darius Green
#11/8/18

#Asks user for the number of males and number of females registered in class.
males= int(input("How many males are registered in class? "))
females= int(input("How many females are registered in class? "))

#Identify the total students in the class
students= males + females

#Make a formula to calculate the Percentage of males/females in class.
PercentageM= (males / students)
PercentageF= (females / students)

#Provide the percentage total per males/females in the class.
print ("The percentage of males is %", format(PercentageM, ",.0%"))
print ("The percentage of females is %", format(PercentageF, ",.0%"))


