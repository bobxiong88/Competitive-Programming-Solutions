import sys
input = sys.stdin.readline
S = input().strip('\n')
T = input().strip('\n')
p = 31
m = int(1e9)+7
hs = 0
hs2=0
for i in range(len(T)):
    hs += ord(T[i])
    hs *= p
    hs %= m
    hs2 += ord(S[i])
    hs2 *= p
    hs2 %= m
okay = pow(p,len(T),m)
if hs == hs2:
    print(0)
    sys.exit(0)
for i in range(len(S)-len(T)):
    hs2 -= okay*ord(S[i])
    hs2 += ord(S[i+len(T)])
    hs2 *= p
    hs2 %= m
    if hs2 == hs:
        print(i+1)
        sys.exit(0)
print(-1)
