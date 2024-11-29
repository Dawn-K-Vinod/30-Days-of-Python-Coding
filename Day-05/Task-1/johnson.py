"""
AUTHOR: Johnson Siby
Date:18-11-2024
"""

number=int(input("Enter a number for the multiplication table:"))
for i in range(1,11):
    multiplication_table=number*i
    print(f"{number} * {i}= {multiplication_table}")

str1=input("Enter a string: ")
for alphabets in str1:
    print(alphabets)