import sys
input = sys.stdin.readline
N = int(input())
freq = [0]*55
a = list(map(int,input().split()))
for i in a: freq[i]+=1
ans = 0
curr = 0
for i in range(55):
    if i*freq[i]>curr:
        curr = i*freq[i]
        ans = i
print(ans)