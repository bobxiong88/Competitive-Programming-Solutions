d = {
'MG': 'midget girls',
'MB': 'midget boys',
'JG': 'junior girls',
'JB': 'junior boys',
'SG': 'senior girls',
'SB': 'senior boys'
    }
n = input()
if n not in d:
    print('invalid code')
else:
    print(d[n])