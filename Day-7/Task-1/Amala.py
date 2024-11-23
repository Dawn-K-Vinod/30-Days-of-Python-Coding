'''
Author:Amala Manoj
Date:23-11-2024
'''
num1=int(input("Enter a nuber:"))
num2=int(input("Enter a nuber:"))
num3=int(input("Enter a nuber:"))
numbers=[num1,num2,num3]
print("The list after appending 3 numbers:",numbers)
numbers.extend([98,67,37,98])
print("The list after extending [98,67,37,98] is:",numbers)
numbers.insert(3,13)
print("The list after inserting 13 in the 3rd index:",numbers)
numbers.remove(67)
print("The list after removing 67:",numbers)
numbers.pop(6)
print("The list after simply using pop():",numbers)
numbers.pop(0)
print("The list after popping the value at index 0:",numbers)
numbers.count(98)
print("Occurance of value 98:",numbers.count(98))
numbers.index(37)
print("The index of 37:",numbers.index(37))
numbers.reverse()
print("The list after reversing:",numbers)
numbers.sort()
print("The list in ascending order:",numbers)
numbers.sort(reverse=True)
print("The list in decending order:",numbers)


str="python, is ,cool"
sen=str.split(",")
print("Output after applying split() to a string:",sen)

