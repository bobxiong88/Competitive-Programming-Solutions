import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    freq = [0]*(max(a)+1)
    for i in a:
        freq[i] += 1
    cnt = []
    for i in freq:
        if i:
            cnt.append(i)
    rem = sum(cnt)-len(cnt)
    if rem%2:
        print(len(cnt)-1)
    else:
        print(len(cnt))
