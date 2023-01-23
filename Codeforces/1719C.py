# numbers after n can never win
# n = max(0,k-pos)
# number can only win if everyone on its left is smaller
#   in that case its number of wins is the number of numbers in between until
#   until there is someone bigger
# binary search on prefix max array?
# if k >= pos+1 and i not n: then q = number of numbers on the right i guess
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, q = map(int,input().split())
    a = list(map(int,input().split()))
    pre = []
    curr = a[0]
    pos = [0]*(n+1)
    for i in range(n):
        curr = max(a[i],curr)
        pre.append(curr)
        pos[a[i]] = i
    for _ in range(q):
        i, k = map(int,input().split())
        i = a[i-1]
        if i == n:
            if pos[n] == 0:
                print(k)
            else:
                print(max(0, k-pos[n]+1))
            continue
        if i < pre[pos[i]]:
            print(0)
            continue
        if k <= pos[i]-1:
            print(0)
            continue
        if k >= pos[n]:
            k = pos[n]
        l = pos[i]
        r = k
        ed = l
        while l <= r:
            m = (l+r)//2
            if pre[m] <= i:
                ed = max(m, ed)
                l = m+1
            else:
                r = m-1
        print(ed-pos[i]+(pos[i]!=0))
