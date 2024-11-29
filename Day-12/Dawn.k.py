"""
Author: Dawn K Vinod
Date: 29-11-2024
"""
string = input("Enter the numbers separated by space:")
list1 = [int(i) for i in string.split()]
unique_set = set(list1)
print(f"Unique: {unique_set}")
duplicates = {num for num in unique_set if list1.count(num)>1}
print(f"Duplicates: {duplicates}" if duplicates!=set() else "There is no duplicate elements in the given set of numbers")

