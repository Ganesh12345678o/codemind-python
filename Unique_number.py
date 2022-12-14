n=int(input())#123
e=[]
while(n>0):
    r=n%10#123%10=3 2
    e.append(r)#32
    n=n//10#12 0
m=len(e)
g=set(e)
x=len(g)
if m==x:
    print("Unique Number")
else:
    print("Not Unique Number")