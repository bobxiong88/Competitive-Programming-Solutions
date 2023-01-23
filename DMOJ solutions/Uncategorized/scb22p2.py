import sys
input = sys.stdin.readline
def get(l, r):
    k = (min(r, -1)-l+1)%2
    if l < 0 and k: return -1
    return 1
l, r = map(int,input().split())
d, u = map(int,input().split())
if l >= d and r <= u:
    print("burnt chicken nugget")
    sys.exit(0)
elif l <= 0 <= r and not (d <= 0 <= u):
    print(0)
    sys.exit(0)
d = max(l, d)
u = min(r, u)
if d > u:
    res = get(l, r)
else:
    res = get(l,r)*get(d, u)
if res == 1:
    print("CHICKEN STRIP!!!")
else:
    print("-1")