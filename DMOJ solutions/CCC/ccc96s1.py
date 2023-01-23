#1996 Problem A
row =int(input())
#writeFile=open("1996.txt","w")
#readFile=open("1996.txt","r")
lis=[]
for i in range(row):
    num=input()
    lis.append(num)
    


for x in range(row):
    factor=[]
    numFile=int(lis[x])

    for i in range(numFile):
        n=i+1
        if numFile%n==0 and n!=numFile:
            factor.append(n)
    sumFactor=sum(factor)
    
    if sumFactor<numFile:
        print(numFile,"is a deficient number.")
    elif sumFactor==numFile:
        print(numFile,"is a perfect number.")
    else:
        print(numFile,"is an abundant number.")