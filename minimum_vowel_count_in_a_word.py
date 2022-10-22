def vowel(s):
    s=s.lower()
    c=0
    for i in s:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            c+=1
    return c
s=input()
m=100
for i in s.split(" "):
    if vowel(i)<m:
        m=vowel(i)
print(m)