X = int(input())
Y = int(input())
c=0
while True:
    if c+X>Y:
        break
    print("All positions change in year",X+c)
    c+=60