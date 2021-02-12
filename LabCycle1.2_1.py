a=input("Enter the string : ")
print(a)
p=[]
p=a.split(" ")
counts = dict()
for i in p:
    if i in counts:
        counts[i]=counts[i]+1
    else:
        counts[i]=1

print(counts)