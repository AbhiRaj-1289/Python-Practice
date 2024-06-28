#Code to calculate distance between two points in co-ordinate geometry
#Author : Abhinav Raj

import math

x1 = int(input("Enter value of x1: "))
x2 = int(input("Enter value of x2: "))
y1 = int(input("Enter value of y1: "))
y2 = int(input("Enter value of y2: "))

#Formula to calculate distance between two points

distance = math.sqrt(((x2-x1)**2 + (y2-y1)**2))
print("Distance between two points is: ",distance)