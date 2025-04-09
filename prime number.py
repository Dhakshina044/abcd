a=int(input("enter a num"))
b=1
count=0
while a>=b:
    if a%b==0:
        count+=1
    b+=1
if count==2:
    print("prime number")
else:
    print("not prime number")
