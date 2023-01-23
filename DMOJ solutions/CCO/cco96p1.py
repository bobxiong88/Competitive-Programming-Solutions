import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        for j in range(i):
            if a[i] < a[j]:
                ans += 1
    print("Optimal train swapping takes {} swaps.".format(ans))