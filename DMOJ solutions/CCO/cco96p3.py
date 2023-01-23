import sys
input = sys.stdin.readline
def get(s, x, y, w, arr):
    global p
    k = [(w//2, 0), (0,0), (0,w//2), (w//2,w//2)]
    p += 1
    if s[p] == 'p':
        for i in range(4):
            get(s, x+k[i][0], y+k[i][1], w//2, arr)
    elif s[p] == 'f':
        for i in range(x, x+w):
            for j in range(y, y+w):
                arr[i][j] = 1
for _ in range(int(input())):
    s = input().strip('\n')
    t = input().strip('\n')
    p = -1
    a = [[0 for i in range(32)] for j in range(32)]
    b = [[0 for i in range(32)] for j in range(32)]
    get(s, 0, 0, 32, a)
    p = -1
    get(t, 0, 0, 32, b)
    ans = 0
    for i in range(32):
        for j in range(32):
            ans += a[i][j]|b[i][j]
    print("There are {} black pixels.".format(ans))