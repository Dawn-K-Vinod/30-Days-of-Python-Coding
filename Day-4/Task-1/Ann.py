"""
Author:Ann Mariya Tony
Date:18-11-2024
"""
side1=float(input("Enter the length of the first side:"))
side2=float(input("Enter the length of the second side:"))
side3=float(input("Enter the length of the third side:"))
if side1+side2>side3 and side2+side3>side1 and side1+side3>side2:
    if side1==side2==side3:
       print("Equilateral")
    elif side1==side2 or side2==side3 or side3==side1:
         print("Isosceles")
    elif side1!=side2!=side3:
         print("Scalene")
else:
   print("Not a triangle")
      
 