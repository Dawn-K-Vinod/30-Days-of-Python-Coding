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
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end="")
    print()