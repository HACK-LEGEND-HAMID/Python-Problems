"""Problem:
Write Python code that asks a user how much money they spend at the store sale.
Source: Shopbop

The sale is 15% off $250+, 20% off $500+, 25% off $1000+. 
They will not receive a discount if they order less than $250.
Print the total of the order."""

spend_money=float(input("Enter the Money You spend at Store:"))

if(spend_money>=1000):
    calculation=spend_money-(spend_money*25)/100
    print("You Got 25% Discount:",calculation)
elif(spend_money>=500):
    calculation=spend_money-(spend_money*20)/100
    print("You Got 20% Discount:",calculation)
elif(spend_money>=250):
    calculation=spend_money-(spend_money*15)/100
    print("You Got 15% Discount:",calculation)
else:
    print("You didn't Get Any Discount")

#Ever tried. Ever failed. No matter. Try Again. Fail again. Fail better.


