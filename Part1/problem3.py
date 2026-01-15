""" Write a program to ask the user to do the following:

Provide the name of a country that does not contain any lowercase a or e letters. (Use the prompt: The country is: )
If the user provides a correct string (i.e. one with no a or e inside it), print: You won... unless you made this name up!
Otherwise, print: You lost!
"""
country = str(input("Write the Name of a Country that does not contain any lowercase a or e letters:"))

if("a" in country or "e" in country):
    print("You lost")
else:
    print("You won... unless you made this name up!")

#what are you afraid of losing when nothing in this world actually belongs to you
