import sys
input = sys.stdin.readline
t = int(input())
letter = 'abcdefghijklmnopqrstuvwxyz'
def good(n,s,c):
    if n==1 and s[0]==letter[c]:
        return 0
    elif n==1 and s[0]!=letter[c]:
        return 1
    first = s[:n//2]
    second = s[n//2:n]
    a = n//2-first.count(letter[c])+good(n//2, second, c+1)
    b = n//2-second.count(letter[c])+good(n//2, first, c+1)
    return min(a,b)
for _ in range(t):
    n = int(input())
    s = list(input())[:n]
    ans = min(good(n,s,0),good(n,s[::-1],0))
    print(int(ans))
        
