#task1
a=("adam")
b=("100")
c=("ad@email.com")
name=input("enter your name")
password=input("enter your password")
email=input("enter your email")
if (name==a and password==b and email==c):
    print("sucess")
else:
    print("invaild") 
#task2
    
tamil=int(input("enter your mark"))
english=int(input("entre your mark"))
math=int(input("enter your mark"))
science=int(input("enter your mark"))
social=int(input("enter your mark"))
subject=(tamil+english+math+science+social)
total=subject/5
if total<25:
    print("grade is fail")
elif total>25 and total<45:
    print("grade is e")
elif total>45 and total<50:
    print("grade is d")
elif total>50 and total<60:
    print("grade is c")
elif total>60 and total<80:
    print("grade is b")
elif total>80:
    print("grade is A")
else:
    print("uncountable") 
#task 3
a=int(input("number of class are held:"))
b=int(input("numnber of class are attend:"))
print(a)
print(b)
n=b/a*100
print(n)
if n<75:
    print("the person not allow to exam")
else:
    print("the person allow to exam ")
