"""Is Sydney the capital of Australia?
If the user answers yes, print: Wrong! Canberra is the capital!
If the user answers no, print: Correct!
If the user answers anything else, print: I do not understand your answer!"""

Answer=str(input("Is Sydney the capital of Australia (yes or No):")).lower()

if(Answer=="yes"):
    print("Wrong! Canberra is the capital!")
elif(Answer=="no"):
    print("Correct!")
else:
    print("I do not understand your Answer")
#"PEOPLE" don't want truth; they want comfort dressed as truth."

