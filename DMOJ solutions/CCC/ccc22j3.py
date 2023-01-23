import sys
input = sys.stdin.readline
s = input().strip('\n')
inst = ''
oper = ''
turn = ''
for i in s:
    if i.isdigit():
        turn = turn + i
    elif i == '+':
        oper = 'tighten'
    elif i == '-':
        oper = 'loosen'
    else:
        if turn:
            print(inst, oper, turn)
            inst = ''
            oper = ''
            turn = ''
        inst = inst + i
print(inst, oper, turn)