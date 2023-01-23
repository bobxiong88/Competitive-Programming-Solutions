m=int(input(""))
n=int(input(""))
s=0
for i in range(1,m+1):
    for x in range(1,n+1):
        if x+i==10:
            s+=1
if s==1:
    print("There is 1 way to get the sum 10.")
else:
    print("There are",s,"ways to get the sum 10.")