s=input()
s=list(set(s))
res=[]
flag=0
for i in s:
    if i.isnumeric():
        res.append(int(i))
for i in res:
    if i%2==0:
        flag=1
res.sort(reverse=True)
ch=0
for i in range(len(res)-1,-1,-1):
    if res[i]%2==0:
        ch=res[i]
        flag=1
        break
if(flag==0):
    print(-1)
else:
    for i in res:
        if i!=ch:
            print(i,end="")
    print(ch)