T, D, P = [int(i) for i in input().split()]

snowday = [T<-40,D>=15,P>50]
c=0

for i in snowday:
    if i==True:
        c+=1
if c>=2:
    print("YES")
else:
    print("NO")