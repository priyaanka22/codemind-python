for _ in range(int(input())):
    n=int(input())
    s=0
    c=0
    while(n):
        r=n%10
        if(r!=0):
            s+=pow(2,c)
        n//=10
        c+=1
    print(s)
    
    