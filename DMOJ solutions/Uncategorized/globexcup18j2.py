input()
n=input().split()
n=[float(i) for i in n]
average=sum(n)/len(n)
c=0
for i in n:
    if i>average:
        c+=1
if c/len(n)>0.5:
    print("Winnie should take the risk")
else:
    print("That's too risky")