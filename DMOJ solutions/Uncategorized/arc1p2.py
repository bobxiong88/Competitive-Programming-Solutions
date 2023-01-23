import sys
input = sys.stdin.readline
N, Q = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
psa = [0]
psb = [0]
for i in range(N):
    psa.append(psa[-1]+A[i])
    psb.append(psb[-1]+B[i])
def get(arr, i, j):
    return arr[j]-arr[i-1]
for i in range(Q):
    L, R = map(int,input().split())
    l = L
    r = R-1
    ans = float('inf')
    while l <= r:
        k = (l+r)//2
        a = get(psa, L, k)
        b = get(psb, k+1, R)
        if a <= b:
            l = k+1
        else:
            r = k-1
        ans = min(ans, max(get(psa, L, k), get(psb, k+1, R)))
    print(ans)