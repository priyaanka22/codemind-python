for _ in range(int(input())):
    n=int(input())
    l=[]
    while(n):
        l.append(str(n%2))
        n//=2
    l.reverse()
    print("".join(l))
    