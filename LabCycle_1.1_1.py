
cr=int(input("Enter the Current Year : "))

fr=int(input("Enter the Final year : "))

leap=[]


for cr in range(cr,fr+1):
       if(cr%4==0 and cr%100!=0 or cr%400==0):
           leap.append(cr)
if len(leap)==0:
    print("No Leap Years in the Range")
else:
    print("Leap Years : ",leap)
    
