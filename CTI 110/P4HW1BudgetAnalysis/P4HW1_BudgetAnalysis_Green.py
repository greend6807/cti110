#CTI-110
#11/28/18
#P4HW1_BudgetAnalysis
#Darius Green

#Initialize the amount.
total=0

#Input the amount.
budget= int(input("What is the amount budgeted for the month? "))

#Input amount budgeted in a month.
for expenses in [0,1, 2, 3, 4]:
    #Prompt user
    print("Enter the expenses for the month", expenses)
    #Input the amount.
    amount= int(input("What are the expenses for the month? "))
    #Add amount to starting total.
    total= total + amount

#Display the total amount.
    print("Your total amount is", total, "amount.")
    print("Enter your expense as 0 to end")
