a=int(input("enter a num"))
d=a
b=len(str(a))
c=0
answer=0
while a>=1:
    c=a%10
    answer+=c**b
    a//=10
a-=1
if d==answer:
    print(answer ,"is a armstrong num")
else:
    print(answer,"is a not armstrong num")


    
