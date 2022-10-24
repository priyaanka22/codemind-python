for _ in range(int(input())):
    n=int(input())
    s=input()
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    flag=0
    for i in s:
        if d[i]==1:
            print(i)
            flag=1
            break
    if(flag==0):
        print(-1)