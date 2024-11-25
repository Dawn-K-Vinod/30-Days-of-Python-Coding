"""
Author:Ann Mariya Tony
Date:23-11-2024
"""
list=[]
for i in range(3):
    num=int(input("Enter a number:"))
    list.append(num) 
print("The list after appending 3 numbers:",list)  
list1=[98,67,37,98]
list.extend(list1)
print("The list after extending [98,67,37,98] is:",list)
list.insert(3,13)
print("The list after inserting 13 in the 3rd index:",list)
list.remove(67)
print("The list after removing 67:",list)
list.pop()
print("The list after simply using pop():",list)
list.pop(0)
print("The list after popping the value at index 0: ",list)
count=list.count(98)
print("Occurence of value 98:",count)
index=list.index(37)
print("The index of 37:",index)
list.sort()
print("The list in ascending order:",list)
list.sort(reverse=True)
print("The list in descending order:",list)
list.reverse()
print("The list after reversing:",list)
str="python is cool"
string=str.split()
print("Output after appliying split() to a string:",string)
   