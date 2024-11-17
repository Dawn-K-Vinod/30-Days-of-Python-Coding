"""
Author: Dawn K Vinod
Date: 17-11-2024
"""
side1=float(input("Enter the length of side 1: "))
side2=float(input("Enter the length of side 2: "))
side3=float(input("Enter the length of side 3: "))

if side1+side2>side3 and side2+side3>side1 and side1+side3>side2:
    if side1==side2==side3:
        print("Equilateral")
    elif side1==side2 or side2==side3 or side3==side1:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not a Triangle.")