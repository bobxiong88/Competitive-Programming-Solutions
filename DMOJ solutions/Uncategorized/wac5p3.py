import sys
input = sys.stdin.readline
N = int(input())
b = list(map(int,input().split()))
ans = N
sizes = [i**2 for i in range(2, int(N**0.5)+1)]
for size in sizes:
    freq = [0]*(N+1)
    for i in range(size): freq[b[i]]+=1
    tar = int(size**0.5)
    nt, nd = 0, 0
    for i in freq:
        if i:
            if i == tar: nt+=1
            nd+=1
    if nt==nd: ans+=1
    #print("size:",size)
    for i in range(N-size):
        x,y = b[i], b[i+size]
        freq[x]-=1
        freq[y]+=1
        if not freq[x]: nd-=1
        if x!=y and freq[y] == 1: nd+=1
        if x!=y and freq[x]+1 == tar: nt-=1
        if x!=y and freq[y]-1 == tar: nt-=1
        if x!=y and freq[x] == tar: nt+=1
        if x!=y and freq[y] == tar: nt+=1
        if nt==nd: ans+=1
        #print(freq, nt, nd)
    #print(ans)
print(ans)