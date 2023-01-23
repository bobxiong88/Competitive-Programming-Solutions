import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    freq = [0]*10
    for i in a:
        i = str(i)
        freq[int(i[-1])] += 1
    ans = "NO"
    for i in range(10):
        for j in range(10):
            for k in range(10):
                freq[i] -= 1
                freq[j] -= 1
                freq[k] -= 1
                if freq[i] >= 0 and freq[j] >= 0 and freq[k] >= 0:
                    if str(i+j+k)[-1] == '3':
                        ans = "YES"
                freq[i]+=1
                freq[j]+=1
                freq[k]+=1
    print(ans)
