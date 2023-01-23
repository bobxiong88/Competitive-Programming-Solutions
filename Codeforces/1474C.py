import sys
input = sys.stdin.readline
freq = [0]*int(2e6+5)
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse = True)
    final = False
    for x in range(1,2*n):
        for i in a:
            freq[i] = 0
        for i in a:
            freq[i]+=1
        ans = [(a[0], a[x])]
        freq[a[0]]-=1
        freq[a[x]]-=1
        curr = a[0]
        pos = True
        for i in range(1,2*n):
            if freq[a[i]] > 0:
                freq[a[i]]-=1
                if freq[curr-a[i]] > 0:
                    freq[curr-a[i]]-=1
                    ans.append((a[i], curr-a[i]))
                    curr = a[i]
                else:
                    pos = False
                    break
        if pos:
            final = True
            print("YES")
            print(a[0]+a[x])
            for i in ans:
                print(*i)
            break
        for i in a:
            freq[i] = 0
    if not final:
        print("NO")
    for i in a:
        freq[i] = 0
