s = 91
for i in range(3):
    if i%2: s += int(input())*3
    else: s += int(input())
print('The 1-3-sum is {}'.format(s))