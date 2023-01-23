a = 'aeiouy'
while True:
    s = input().strip('\n')
    if s=='quit!': break
    s = list(s)
    if len(s)>3:
        if s[-1]=='r' and s[-2]=='o' and s[-3] not in a:
            s.insert(-1, 'u')
    print(''.join(s))