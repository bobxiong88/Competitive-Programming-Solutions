import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
b = []
o = [[] for i in range(80)]
for i in a:
    temp = int(str(i))
    c = 0
    while True:
        if temp%2==0:
            temp/=2
            c+=1
        else:
            break
    o[c].append(i)
f = []
for i in o:
    f = f+sorted(i)[::-1]
print(*f)
