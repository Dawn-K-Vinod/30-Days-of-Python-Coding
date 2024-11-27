"""
Author:Ann Mariya Tony
Date:27-11-2024
"""
tuple=(23,54,71,13)
print("The tuple :",tuple) 
print("All the elements in the tuple:")
for i in tuple:
    print(i)
print("All the elements in the tuple in reverse order:")
i = len(tuple)-1
while i>=0:
    print(tuple[i])
    i=i-1
fruits=("apple", "banana", "cherry","Blueberry")
print("The tuple named Fruits:",fruits)
print("Fruits that starts with the letter B:")
for fruit in fruits:
    if fruit.lower().startswith('b'):
        print(fruit)