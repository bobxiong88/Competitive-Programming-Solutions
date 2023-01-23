import sys
input = sys.stdin.readline
n,d = map(int,input().split())
a = list(map(int,input().split()))
pre = [0]
for i in a: pre.append(pre[-1]+i)
i = 1
j = n
for x in range(d):
    m = int(input())
    s1 = pre[i+m-1]-pre[i-1]
    s2 = pre[j]-pre[i+m-1]
    if s1 < s2:
        print(s2)
        j = i+m-1
    else:
        print(s1)
        i += m