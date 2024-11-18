"""
Author: Dawn K Vinod
Date: 18-11-2024
"""
n1 = int(input("Enter a natural number upto which you want to find sum:"))
n2=n1
while True:
    if n2<=0:
        print("This is not a natural number")
    else:
        sum_n=0
        while n2>0:
            sum_n += n2
            n2-=1
        break
print(f"The sum of natural numbers from 1 to {n1} is {sum_n}.")