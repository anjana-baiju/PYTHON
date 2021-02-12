n=int(input("Enter the Number : "))
fact=1
if n==0:
    fact=1
elif n<0:
    print("Cant Find Factorial for a Negative number")
else:
    for i in range(2,n+1):
        fact=fact*i
print("Factorial is ",fact)

