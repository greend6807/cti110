#CTI-110
#11/28/18
#P4T2_Bug_Collector
#Darius Gren

#Initialize the accumulator.
total=0

#Bugs collected for each day.
for day in range(1, 6):
    #Prompt user.
    print("Enter the bugs collected on day", day)
    #Input number of bugs.
    bugs= int(input())
    #Add bugs to total.
    total += bugs

#Display the total bugs.
    print("You collected a total of", total, "bugs.")
    
