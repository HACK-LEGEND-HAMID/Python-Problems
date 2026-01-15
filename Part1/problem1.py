"""Exercise: Write a program that will ask the user for their height in centimeters. Use the input() built-in function to do this. If the height is more than 185 centimeters, print the following line of code:

You are very tall.
otherwise print:
Your height is Normal
"""

height=int(input("Enter Your Height:"))

if(height>=185):
    print("You are very tall")
else:
    print("Your height is Normal")

