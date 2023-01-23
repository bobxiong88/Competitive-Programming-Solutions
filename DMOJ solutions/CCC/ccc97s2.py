lis=[]
inp=int(input())
for i in range(inp):
    n=int(input())
    lis.append(n)
for i in lis:
    nasty=False
    factors=[]
    if i==1:
        factors.append([1,1])
    for x in range(1,i):
        nut=[]
        
        if i%x==0:
            if(x>(i/x)):
                break
            nut.append(x)
            nut.append(i/x)
            factors.append(nut)
    for s in factors:

        for a in factors:
            if s!=a and (abs(s[0]-s[1])==a[0]+a[1] or abs(a[0]-a[1])==s[0]+s[1]):
                nasty=True
    if nasty==True:
        print(str(i)+" is nasty")
    else:
        print(str(i)+" is not nasty")