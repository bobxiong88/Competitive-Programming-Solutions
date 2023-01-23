import sys
def search(a):
    if match[a]==[]:
        return False
    index = len(match[a])-1
    last = len(match[a])-1
    num = match[a][-1]
    c = 0
    while True:
        c+=1
        if c>20:
            for i in match[a]:
                if x<=i<=y:
                    return True
            return False
        if x<=num<=y:
            return True
        last = int(str(index))
        if x>num:
            index = min(index*2,len(match[a])-1)
        elif y<num:
            index = index//2
        num = match[a][index]
        if last==index:
            return False
input = sys.stdin.readline
N, K, Q = map(int,input().split())
prefix = [0]
array = list(map(int,input().split()))
s = 0
match = []
for i in range(-1000, 1001):
    match.append([])

for i in range(N):
    s+=array[i]
    match[array[i]].append(i+1)
    prefix.append(s)
for i in range(Q):
    a,b,x,y = map(int,input().split())
    diff = prefix[y]-prefix[x-1]
    if diff<=K:
        print("No")
        continue
    if search(a) and search(b):
        print("Yes")
    else:
        print("No")