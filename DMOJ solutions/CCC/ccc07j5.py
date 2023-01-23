hotels = [False]*7001
ways = [0]*7001
hotels[0]=True
hotels[990]=True
hotels[1010]=True
hotels[1970]=True
hotels[2030]=True
hotels[2940]=True
hotels[3060]=True
hotels[3930]=True
hotels[4060]=True
hotels[4970]=True
hotels[5030]=True
hotels[5990]=True
hotels[6010]=True
hotels[7000]=True

A = int(input())
B = int(input())
m = int(input())
for i in range(m):
    hotels[int(input())] = True

ways[0]=1

for i in range(1,7001):
    if hotels[i]:
        ways[i]=0
        a = i-B
        if a<0:
            a=0
        for j in range(a,i-A+1):
            ways[i] = ways[i]+ways[j]
print(ways[7000])