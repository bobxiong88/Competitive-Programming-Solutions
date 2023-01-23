N, M, Y = map(float,input().split())
for i in range(int(Y+1)):
    print('{} {:.2f}'.format(i, round(N*(1+M*0.01)**i,2)))