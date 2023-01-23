import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int,input().split()))
freq = [0]*(int(1e6)+5)
for i in a:
    freq[i]+=1
ans = []
for i in range(1,max(a)+1):
    ans.append(i)
for x in range(max(a),0,-1):
    for i in range(freq[x]-1):
        ans.append(x)
print(*ans)