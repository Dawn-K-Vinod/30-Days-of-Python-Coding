"""
Author:Ann Mariya Tony
Date:19-11-2024
"""
num=int(input("Enter a number for the multiplication table")) 
string=input("Enter a string")
print("Multiplication Table for",num)
for i in range(1,11):
     print(num,"×",i,"=",num*i)
print("Characters in the string:",string)
for i in string:
    print(i)