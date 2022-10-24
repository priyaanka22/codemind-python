n=int(input())
paths=[list(map(str,input().split()))for i in range(n)]
d={}
for i,j in paths:
    d[i]=j
for i in d:
    while d.get(i)!=None:
        i=d[i]
    print(i)
    break