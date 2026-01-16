"""Problem:Write Python code that asks the user for a number in the range of 1 through 7. Display the corresponding day of the week where 

1 for Monday

2 for Tuesday 

3 for Wednesday 

4 for Thursday

5 for Friday

6 for Saturday

7 for Sunday. 

If the user enters a number outside the range of 1 - 7, print “error, out of range”."""


days=str(input("Enter the Number in the range of 1 to 7:"))

if days=="1":
    print("Monday")
elif days=="2":
    print("Tuesday")
elif days=="3":
    print("Wednesday")
elif days=="4":
    print("Thursday")
elif days=="5":
    print("Friday")
elif days=="6":
    print("Saturday")
elif days=="7":
    print("Sunday")
else:
    print("Out of Range:(")
