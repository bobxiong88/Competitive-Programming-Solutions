import sys
input = sys.stdin.readline
import random
def solve(bot, cap):
    if not cap: return
    x = cap.pop()
    abot = []
    bbot = []
    acap = []
    bcap = []
    m = -1
    for y in bot:
        print(0, x, y)
        sys.stdout.flush()
        res = int(input())
        if res == -1:
            abot.append(y)
        elif res == 0:
            print(1, x, y)
            m = y
            sys.stdout.flush()
        else:
            bbot.append(y)
    for y in cap:
        print(0, y, m)
        sys.stdout.flush()
        res = int(input())
        if res == 1:
            acap.append(y)
        else:
            bcap.append(y)
    solve(abot, acap)
    solve(bbot, bcap)
    
N = int(input())
bot = [i for i in range(1, N+1)]
random.shuffle(bot)
cap = [i for i in range(1, N+1)]
random.shuffle(cap)
solve(bot, cap)
#sys.stdout.flush()