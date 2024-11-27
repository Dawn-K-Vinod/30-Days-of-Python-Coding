"""
Author:Ann Mariya Tony
Date:21-11-2024
"""
list1=[] 
for i in range(5):
    while True:
              num=float(input("Enter a number:"))
              list1.append(num)
              break
print( "The first list of numbers is:",list1)
list2=[30.0,35.0,40.0,45.0]
print("The second list of numbers is:",list2)
list1.extend(list2)
print("The extended list of numbers is:",list1)
print("Sum of all numbers:",sum(list1))
print("Smallest number:",min(list1))
print("Largest number:",max(list1))
