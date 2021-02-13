list=[]
n=int(input("Enter the no. of Elememnts : "))

print("Enter the Numners :")

for i in range(n):
      list.append(int(input()))
print("The Elements are : ",list)
print("The Postitive Integers are : ")

for i in list:
      if(i>0):
          print(i)
