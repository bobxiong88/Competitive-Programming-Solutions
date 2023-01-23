import sys
from math import ceil
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = input().strip('\n')
    b = input().strip('\n')
    if '0' not in a and '0' not in b:
        print(0)
    elif '1' not in a and '1' not in b:
        print(n)
    else:
        ans = 0
        nxt = []
        for x in range(n):
            if a[x] != b[x]:
                ans += 2
                k = len(nxt)
                i = 0
                while i < k:
                    if i < k-1:
                        if nxt[i] != nxt[i+1]:
                            ans += 2
                            i += 2
                        else:
                            if nxt[i] == 0:
                                ans += 1
                            i += 1
                    else:
                        if nxt[i] == 0:
                            ans += 1
                        i+=1
                #print(nxt)
                nxt = []
            else:
                nxt.append(int(a[x]))
        if nxt:
            k = len(nxt)
            i = 0
            while i < k:
                if i < k-1:
                    if nxt[i] != nxt[i+1]:
                        ans += 2
                        i += 2
                    else:
                        if nxt[i] == 0:
                            ans += 1
                        i += 1
                else:
                    if nxt[i] == 0:
                        ans += 1
                    i+=1
            #print(nxt)
        print(ans)
                    
