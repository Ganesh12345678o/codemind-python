x=int(input())
s=0
p=1
while(x):
    r=x%10
    s=s+r
    p=p*r
    x=x//10
if(s==p):
    print("Spy Number")
else:
    print("Not Spy Number")