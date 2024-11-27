"""
Author:Ann Mariya Tony
Date:16-11-2024
"""
name = input("Enter your name:")
age = int(input("How old are you?"))
height = float(input("What is your height in centimeters?"))
Height = height/100 
print("\n Hello,",name,"!")
print ("You are",age,"years old and",height,"cm tall")
print("That is ",Height,"meters tall")
print("Data type of name:",type(name))
print("Data type of age:",type(age))
print("Data type of converted height:",type(Height))
