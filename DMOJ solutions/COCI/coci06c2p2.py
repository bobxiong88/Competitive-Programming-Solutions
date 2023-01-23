a = list(map(int,input().split()))
a.sort()
s = input()
d = {'A':0,'B':1,'C':2}
for i in s:
    print(a[d[i]], end = ' ')