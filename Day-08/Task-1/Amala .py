'''
Author:Amala Manoj
Date:24-11-2024
'''
tuple=1,2,3,4,5,6,7,8,9,10
print("Tuple:",tuple)
print("Third element:",tuple[2])
print("Sliced tuple(index 4 to 8):",tuple[4:9])
second_tuple=11,12,13
print("Second Tuple:",second_tuple)
con_tuple=tuple+second_tuple
print("Concentrated Tuple:",con_tuple)
if 5 in con_tuple:
    print("Does 5 exist in the tuple? yes")
else:
    print("no")
print("Length of the tuple:",len(con_tuple))
