"""Problem:

Write Python code that asks a user how much money they spend at the store sale.

If they spend less than $75, they receive no discount.

If the user spends $75 or more, they receive $15 off. 

If the user spends $100 or more, they receive $25 off. 

If they user spends $150 or more, they receive $50 off. """

usr_spend_cash=int(input("Enter the Money You Spend at Store Sale:"))

if(usr_spend_cash>=75 and usr_spend_cash<100):
    usr_spend_cash=usr_spend_cash-15
    print("You Got 15$ OFF",usr_spend_cash,"$")
elif(usr_spend_cash>=100 and usr_spend_cash<150):
    usr_spend_cash=usr_spend_cash-25
    print("You Got 25$ OFF",usr_spend_cash,"$")
elif(usr_spend_cash>=150):
    usr_spend_cash=usr_spend_cash-50
    print("You Got 50$ OFF",usr_spend_cash,"$")
else:
    print("You Get No Discount")

#But man is not made for defeat. A man can be destroyed but not defeated.
