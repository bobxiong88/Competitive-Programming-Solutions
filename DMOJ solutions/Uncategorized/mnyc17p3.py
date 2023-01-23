import sys
input = sys.stdin.readline
a, b = input().split()
p = 31
m = 92723947239479
tb = [p]*max(len(a),len(b))
for i in range(1,len(tb)):
    tb[i] *= tb[i-1]
    tb[i] %= m
seen = set()
hs = 0
for i in range(len(b)):
    hs += ord(b[i])*tb[i]
    hs %= m
    seen.add(hs)
ans = 0
hs = 0
for i in range(len(a)):
    hs += ord(a[~i])
    hs *= p
    hs %= m
    if hs in seen:
        ans = max(ans, i+1)
print(a+b[ans:])