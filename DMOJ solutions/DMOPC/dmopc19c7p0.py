def average(l):
    return sum(l)/len(l)


A, B, C, D = map(int,input().split())
a = [(A,B),(A,C),(A,D),(B,C),(B,D),(C,D),(A,B,C),(A,B,D),(A,C,D),(B,C,D),(A,B,C,D)]
for i in a:
    print("{0:.6f}".format(average(i)))