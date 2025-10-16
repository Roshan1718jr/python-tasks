a=int(input ("Enter your First Number:"))
b=int(input("Enter your Second Number:"))
op=input ("Enter your Operator:")
tot=0
if op=="+":
	tot=(a+b)
elif op=="-":
	tot=(a-b)
elif op=="*":
	tot=(a*b)
elif op=='/':
	tot=(a/b)
else:
    print('Check invalid data')
print(tot)

	

#Task2
a=int(input("Enter the no1:"))
b=int(input("Enter the no2:"))
op=input("Enter the symbol:")
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def division(a,b):
    return a/b 
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    print(a/b)
else:
    print(" try")
    
