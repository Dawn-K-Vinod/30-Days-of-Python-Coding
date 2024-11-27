'''
Author:Amala Manoj
Date:23-11-2024
'''
first_list=[]
for i in range(5):
    number=float(input(f"Enter a number{i+1}:"))
    first_list.append(number)
second_list=[30.0,35.0,40.0,45.0]
print("The First list of numbers:",first_list)
print("The Second list of numbers:",second_list)

first_list.extend(second_list)
print("The Extended list of numbers:",first_list)
print("Sum of the extended list:",sum(first_list))
print("Smallest number in the extended list:",min(first_list))
print("Largest number:",max(first_list))
