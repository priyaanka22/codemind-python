for _ in range(int(input())):
    s=input()
    l=[]
    flag=0
    for i in s:
        if i=='(' or i=='[' or i=='{':
            l.append(i)
        else:
            if len(l)==0:
                flag=1
                break
            elif i==')' and l[-1]!='(':
                flag=1
                break
            elif i==']' and l[-1]!='[':
                flag=1
                break
            elif i=='}' and l[-1]!='{':
                flag=1
                break
            l.pop()
    print(flag==0)