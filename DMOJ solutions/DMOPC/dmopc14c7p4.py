n = int(input())
r = 1
while True:
    k = r*(r+1)//2
    if k >= n:
        print(k*(k+1)//2-(k-r)*(k-r+1)//2)
        break
    r+=1