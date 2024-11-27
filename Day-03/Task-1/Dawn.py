"""
Author: Dawn K Vinod
Date: 16-11-2024
"""
name=input("Enter your name:")
age=int(input("Enter your age:"))
height=int(input("Enter your height(in cm):"))
height_in_meters=height/100

print(f"Hello, {name}!")
print(f"You are {age} years old and {height} cm tall.")
print(f"That is {height_in_meters} meters tall.")
print(f"Data type of name: {type(name)}")
print(f"Data type of age: {type(age)}")
print(f"Data type of height_in_meters: {type(height_in_meters)}")
