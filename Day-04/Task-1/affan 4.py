
'''
Author:Affan muhammed
Date:18-11-2024
'''
first_side=float(input("Enter the length of the first side:"))
second_side=float(input("Enter the length of the second side:"))
third_side=float(input("Enter the length of the third side:"))
if (first_side+first_side>third_side and second_side+third_side>first_side and first_side+third_side>second_side) :
    if (first_side==second_side==third_side):
        print("Equilateral")
    elif (first_side==second_side or second_side==third_side or third_side== first_side):
     print("Isoceles")
    elif (first_side!=second_side!=third_side):
        print("Scalene")
else:
        print("Not a triangle")
