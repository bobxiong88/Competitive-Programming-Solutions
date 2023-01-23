from math import ceil
for _ in range(int(input())):
    b = bin(int(input()))[2:]
    print(' '.join([str('0'*(ceil(len(b)/4)*4-len(b))+b)[i*4:(i+1)*4] for i in range(ceil(len(b)/4))]))