#CTI-110
#P3HW1_Roman_Numerals
#Darius Green
#11/13/18

#Prompt user to enter a number within the range of 1 through 10.
number= int(input("Enter a value between 1 and 10: "))

#Print the values 1 through 10 as Roman numeral if entered.
if number == 1:
    print("I")
elif number == 2:
    print("II")
elif number == 3:
    print("III")
elif number == 4:
    print("IV")
elif number == 5:
    print("V")
elif number == 6:
    print("VI")
elif number == 7:
    print("VII")
elif number == 8:
    print("VIII")
elif number == 9:
    print("IX")
elif number == 10:
    print("X")

#If the number is outside the range of 1 through 10, display error
#message.
elif number > 10:
    print("Error occured.")
elif number < 1:
    print("Error occured.")

