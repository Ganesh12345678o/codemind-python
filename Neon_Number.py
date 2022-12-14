x=int(input())
n=x*x
s=0
while(n):
    r=n%10
    s=s+r
    n=n//10
if x==s:
    print("Neon Number")
else:
    print("Not Neon Number")