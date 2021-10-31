import math
n=int(input())
order=len(str(n))
m=n
sum=0
while n>0:
    temp=n%10
    sum=sum+pow(temp,order)
    n=n//10
if sum==m:
    print("true")
else:
    print("false")
    
