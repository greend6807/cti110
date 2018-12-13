#CTI-110
#11/28/18
#P4HW2_CelsiusFahrenheit
#Darius Green

#Lay the table format.
print("C\tF")
print("---------------")

#Enter the ranges of numbers were calculating.
for celsius in range (0,21):
    fahrenheit= (9/5*celsius) + 32
    print(celsius, "\t", fahrenheit)
