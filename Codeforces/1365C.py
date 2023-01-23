import sys
input = sys.stdin.readline
n = int(input())
a = [0]+list(map(int,input().split()))
b = [0]+list(map(int,input().split()))
c = [0]*(n+1)
count = dict()
for i in range(1,n+1):
    c[a[i]] = i
for i in range(1,n+1):
    cur = (c[b[i]]-i+n)%n
    try:
        count[cur]+=1
    except:
        count[cur] = 1
print(max(count.values()))
