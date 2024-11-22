str1=("I Love Python.")
print(str1)
print("Increasing Triangle")
n=int(input("Enter the no.of rows:"))
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print(" ")
print("Decreasing Triangle")
d=int(input("enter the no.of rows"))
for i in range(d):
    for j in range(n-i):
       print("*",end="")
    print(" ")
