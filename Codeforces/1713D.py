# if two people are equal, they are definitely not winenrs
# if one is greater than the other, then one is winner, the other is not
# if 
import sys
import random
input = sys.stdin.readline
def query(a,b):
    print('? {} {}'.format(a,b))
    sys.stdout.flush()
    return int(input())
def win(x):
    print('! {}'.format(x))
    sys.stdout.flush()
for _ in range(int(input())):
    n = int(input())
    curr = [i for i in range(1,pow(2,n)+1)]
    for x in range(0,n,2):
        if len(curr)==2:
            win(curr[query(curr[0],curr[1])-1])
            break
        nxt = []
        #print(curr, x, pow(2,n-x))
        for i in range(0,pow(2, n-x), 4):
            res = query(curr[i], curr[i+3])
            if res == 1:
                if query(curr[i], curr[i+2]) == 1:
                    nxt.append(curr[i])
                else:
                    nxt.append(curr[i+2])
            elif res == 2:
                if query(curr[i+3], curr[i+1]) == 1:
                    nxt.append(curr[i+3])
                else:
                    nxt.append(curr[i+1])
            else:
                nxt.append(curr[i+query(curr[i+1],curr[i+2])])
        curr = nxt[:]
    if len(curr)==1: win(curr[0])
