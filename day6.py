n=0
while True:
    n+=1
    print(n)
    if n==10:
        break
print()   
#task While usee List
n=0
odd=[]
even=[]
while True:
    n+=1
    if n==100:
        break
    if n%2==0:
        even.append(n)
    else:
        odd.append(n)
print(odd)
print(even)
