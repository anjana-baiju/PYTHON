n=int(input("Enter the number of terms: "))

a=0
b=1
if n<=0:
    print("Term should be positive number")
elif n==1:
    print("Series is : ",a)
elif n==2:
    print("Series is : ", a,b)
else:
    print("Series is : ")
    print(a)
    print(b)

    for i in range(2,n):
        c=a+b

        print(c)
        a=b
        b=c
