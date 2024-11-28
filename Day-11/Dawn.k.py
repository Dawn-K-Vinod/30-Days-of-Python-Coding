
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"Set-1: {set1}")
print(f"Set-2: {set2}")

union_set = set1|set2
intersection_set = set1 & set2
difference_set = set1-set2
symmetric_difference_set = set1 ^ set2

print(f"Union: {union_set}")
print(f"Intersection: {intersection_set}")
print(f"Difference: {difference_set}")
print(f"Symmetric difference: {symmetric_difference_set}")


