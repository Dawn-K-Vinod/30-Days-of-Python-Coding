"""
Author:Ann Mariya Tony
Date:19-11-2024
"""
num=int(input("Enter a positive integer:"))
num1=num
while True:
      if num1<=0:
        print("This is not a natural number")
      else:
         sum=0
         while num1>0:
             sum=sum+num1
             num1=num1-1
         break
print("The sum of natural numbers from 1 to",num,"is:",sum)        
    