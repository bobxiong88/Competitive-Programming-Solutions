lis=[]
tNum=0
sNum=0
num=int(input(""))
for i in range(num):
    inp=input("")
    lis.append(inp)
for x in lis:
    for i in x:
        if i=="t" or i=="T":
            tNum+=1
        elif i=="s" or i=="S":
            sNum+=1
if tNum>sNum:
    print("English")
elif tNum<sNum:
    print("French")
elif tNum==sNum:
    print('French')