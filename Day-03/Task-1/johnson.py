"""
AUTHOR: Johnson Siby
Date:15-11-2024
"""
name=input("What is your name ? : ")
age=int(input("How old are you?: "))
height=float(input("What is your height in cms?: "))
print(f"Hello,{name}.You are {age} years old and {height}cms tall.")
height_in_m=(height/100)
print(f"That is {height_in_m}m tall .")
print(f"Data type of age : {type(age)}")
print(f"Data type of name :{type(name)}")
print(f"Data type of height : {type(height)}")