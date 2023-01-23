import sys
input = sys.stdin.readline
def pos(st):
    return ord(st)-97
N = input().strip('\n')
H = input().strip('\n')
n = len(N)
h = len(H)
if n>h:
    print(0)
    sys.exit(0)
freq = [0]*26
for i in range(n):
    freq[pos(N[i])]+=1
f = [0]*26
s = H[h-n:]
#print(s)
for i in range(h-n,h):
    f[pos(H[i])]+=1
hs = 0
p = 13
m = 100000020271
for i in range(n):
    hs += (ord(s[i])-96)*pow(p, i, m)
hs %= m
a = set()
if f == freq:
    a.add(hs)
for i in range(h-1, n-1, -1):
    hs -= ((ord(H[i])-96)*pow(p, n-1, m))
    hs *= p
    hs %= m
    hs += ord(H[i-n])-96
    hs %= m
    f[pos(H[i])]-=1
    f[pos(H[i-n])]+=1
    if f == freq:
        a.add(hs)
print(len(a))