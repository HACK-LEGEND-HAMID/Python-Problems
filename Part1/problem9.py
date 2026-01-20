"""Problem:
Write a C program to accept a coordinate point in an XY coordinate system and determine in which quadrant the coordinate point lies.
Test Data : 7 9
Expected Output :
The coordinate point (7,9) lies in the First quadrant.
"""

X=int(input("Enter The X Axis:"))
Y=int(input("Enter The Y Axis:"))

if(X>0 and Y>0):
    print(f"The Coordinate Point {X,Y} lies in the I Quadrant")
elif(X<0 and Y>0):
    print(f"The Coordinate Point {X,Y} lies in the II Quadrant")
elif(X<0 and Y<0):
    print(f"The Coordinate Point {X,Y} lies in the III Quadrant")
elif(X>0 and Y<0):
    print(f"The Coordinate Point {X,Y} lies in the IV Quadrant")
elif(X==0 and Y==0):
    print("The Point Lies At Origin")
elif(X==0):
    print("The Point Lies on the Y Axis")
elif(Y==0):
    print("The Point Lies on the X Axis")

#Always remember that you are absolutely unique. Just like everyone else.
