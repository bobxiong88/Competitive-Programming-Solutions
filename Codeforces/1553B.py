import sys
input = sys.stdin.readline
for _ in range(int(input())):
    s = input().strip("\n")
    t = input().strip('\n')
    ans = "NO"
    for i in range(len(t)+1):
        a = t[:i]
        b = t[i:]
        b = b[::-1]
        #print(a,b)
        for j in range(len(s)-len(a)+1):
            #print(j, s[j:j+len(a)], s[j+len(a)-len(b)-1:j+len(a)-1])
            if s[j:j+len(a)] == a:
                if s[j+len(a)-len(b)-1:j+len(a)-1] == b:
                    ans = "YES"
                    break
    print(ans)
