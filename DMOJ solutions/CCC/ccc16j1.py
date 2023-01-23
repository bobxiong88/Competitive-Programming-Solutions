w=0
for i in range(6):
    if input()=="W":
        w+=1

if 6>=w>=5:
    print(1)
elif w>=3:
    print(2)
elif w>=1:
    print(3)
else:
    print(-1)