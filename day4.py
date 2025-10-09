#for
for i in range(1,10,1):
    print(i)
#table
x=2    
for i in range(1,10,1):
    print(i,"*",x,"=",i*x)
#table2
n=int(input("enter the number"))
for i in range(1,10,1):
    print(i,"*",n,"=",i*n)
#table with list     
n=int(input("enter the number"))
li=[]
for i in range(1,10,1):
    print(i,"*",n,"=",i*n)
    li.append(i*n)
print(li)
