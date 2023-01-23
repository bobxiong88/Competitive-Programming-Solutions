n=int(input())
lis=[]
for i in range(n):
    lis.append([int(i) for i in input().split()])

for i in lis:
    if i[0]*i[1]==i[2]:
        print("POSSIBLE DOUBLE SIGMA")
    else:
        print("16 BIT S/W ONLY")