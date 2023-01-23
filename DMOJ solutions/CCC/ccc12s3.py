import sys
input = sys.stdin.readline
n = int(input())
freq = [[i, 0] for i in range(1001)]
for i in range(n):
    x = int(input())
    freq[x][1]+=1
freq.sort(key = lambda x: x[1], reverse = True)
ans = 0
if freq[0][1] == freq[1][1]:
    l = []
    for a,b in freq:
        if b == freq[0][1]:
            l.append(a)
        else:
            break
    ans = max(l)-min(l)
elif freq[1][1] == freq[2][1]:
    for a,b in freq[1:]:
        if b == freq[1][1]:
            ans = max(ans, abs(freq[0][0]-a))
        else:
            break
else:
    ans = abs(freq[0][0]-freq[1][0])
print(ans)