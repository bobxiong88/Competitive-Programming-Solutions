n=[]
num=0
lis=[]
new=[]
c=0
finalis=[]
inp=input()
goodversion=inp+" "
for i in goodversion:
    if i==" ":
        lis.append(n)
        n=[]
    else:
        n.append(i)
#print(lis)
for i in range(len(lis)):
    new.append(int("".join(lis[i])))
new.insert(0,0)
#print(new)
for i in range(len(new)):
    c=0
    for n in range(i):
        c-=new[n+1]
    re=[]
    for x in range(len(new)):
        c+=new[x]
        re.append(str(abs(c)))
    finalis.append(re)
for i in finalis:
    print(" ".join(i))