#CTI-110
#12/6/18
#P4HW3_TuitionIncrease
#Darius Green

#Set the tuition ($8,000) for one student per semester.
tuition= 8,000

#Tuition increase by 3% (.03) for next 5 years.
for tuition in [0, 1, 2, 3, 4]:
    #Calculate the formula
    increased_tuition= tuition * .03
#Display the new total amount per year.
    print("Your total tuition is", tuition, "increased_tuition.")
