import sys
import random
N = int(input())
a = [i for i in range(1,N+1)]
while True:
    random.shuffle(a)
    print(*a)
    sys.stdout.flush()
    if int(input()) == 0:
        break