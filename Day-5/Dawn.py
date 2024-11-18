"""
Author: Dawn K Vinod
Date: 18-11-2024
"""
#looping to print multiplication table
num=int(input("Enter a number for multiplication table:"))
print(f"Multiplication Table for {num}")
for i in range(1,11):
    print(f"{num} x {i} = {i*num}")

#looping through string
string=input("\nEnter a string:")
print(f"Characters in the string '{string}':")
for i in string:
    print(i)
