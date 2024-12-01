"""
AUTHOR: Johnson Siby
Date:1-12-2024
"""

list1=[]
for i in  range(5):
    numbers=int(input("Enter a number: "))
    list1.append(numbers)
print("The first set of numbers is : ",list1)
list2=[10,20,30,40,50]
list1.extend(list2)
print("The extended list is: ",list1
)
print("The sum of all numbers: ",sum(list1))
print("Smallest number :",min(list1))
print("Largest number:",max(list1))