"""Write a program to accept percentage from the user and display the grade according to the following criteria:
Marks          |Grade
>90            | A  
>80 and <=90   | B
>=60 and <= 80 | C
>=50 and <60   | D
>50            | F
"""
percentage=int(input("Enter Your Percentage:"))
if(percentage>90):
    print("A")
elif(percentage>80 and percentage <=90):
    print("B")
elif(percentage>=60 and percentage <=80):
    print("C")
elif(percentage>=50 and percentage <60):
    print("D")
else:
    print("F")

#Let us sacrifice our today so that our children can have a better tomorrow.


