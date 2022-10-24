s=input()
s=list(s)
i=0
j=len(s)-1
while(i<j):
    if str(s[i]).isalpha()==False:
        i+=1
    elif str(s[j]).isalpha()==False:
        j-=1
    else:
        s[i],s[j]=s[j],s[i]
        i+=1
        j-=1
print("".join(s))