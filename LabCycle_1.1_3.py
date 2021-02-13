list=[]
n=int(input("Enter the no. of Elememnts : "))

print("Enter the Numners :")

for i in range(n):
      list.append(int(input()))
print("The Elements are : ",list)

for i in list:
    print("Square of ",i," = ",i*i)
