#CTI-110
#P3HW2- Shipping Charges
#Darius Green
#11/13/18

#Prompt the user to enter the weight of a package.
weight= int(input("Enter the weight of the package: "))

#Calulate price
#price= weight * 

#Display the shipping charges based off the weight.
#Refer page 118 exercise for charges.
if weight <= 2:
    print("$1.50")

elif weight >= 2 and weight < 6:
    print("$3.00")

elif weight >= 6 and weight <= 10:
    print("$4.00")

elif weight > 10:
    print("$4.75")
