lis = [int(i) for i in input().split()]

large = max(lis)
lis.remove(large)

if large>=sum(lis):
    print("no")
else:
    print("yes")