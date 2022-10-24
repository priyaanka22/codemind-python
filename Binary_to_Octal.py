t=int(input())
for _ in range(t):
    n=int(input())
    s=0
    c=0
    while(n):
        r=n%10
        if r!=0:
            s+=pow(2,c)
        c+=1
        n//=10
    res=""
    c=0
    while(s):
        res+=str(s%8)
        s//=8
    res=res[::-1]
    print(res)
