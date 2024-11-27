"""
Author:Ann Mariya Tony
Date:25-11-2024
"""
tuple1=tuple(range(1,11))
print("Tuple:",tuple1)
third_element=tuple1[2]
print("Third element:",third_element)
sliced=tuple1[4:9]
print("Sliced tuple (index 4 to 8):",sliced)
tuple2=(11,12,13)
print("Second Tuple:",tuple2)
tuple3=tuple1+tuple2
print("Concatenated Tuple:",tuple3)
print("Does 5 exist in the tuple?",5 in tuple3)
length=len(tuple3)
print("Length of the tuple:",length)
