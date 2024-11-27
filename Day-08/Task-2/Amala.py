'''
Author:Amala Manoj
Date:27-11-2024
'''
tuple=23,54,71,13
print("The Tuple:",tuple)
print ("All the elements in the tuple:")
for i in tuple:
    print(i)
print("All the elements in the tuple in reverse order:")
for i in tuple[::-1]:
    print(i)
fruits=("apple","banana","cherry","blueberry")
print("The tuple named Fruits:",fruits)

print("Fruits that start with the letter 'b':")
for fruit in fruits:
    if fruit.startswith('b'):
        print(fruit)
