#CTI-110
#11/15/18
#P3Lab
#Darius Green

def main():
    # This program takes a number grade and outputs a letter grade.
    score = float(input("Enter grade: "))

    # system uses 10-point grading scale
    A_score =  90
    B_score =  80
    C_score =  70
    D_score =  60
    F_score =  59

    # Define the rest of the scores

    if score >= A_score:
        print("Your grade is: A")
    elif score >= B_score:
        print("Your grade is: B")
    elif score >= C_score:
        print("Your grade is: C")
    elif score >= D_score:
        print("Your grade is: D")
    elif score <= F_score:
        print("Your grade is: F")







# program start
main()
