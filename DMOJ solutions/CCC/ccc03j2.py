while True:
    n = int(input())
    if not n: break
    ans = [10000,10000]
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            if n//i+i<sum(ans):
                ans = [i,n//i]
    print("Minimum perimeter is {} with dimensions {} x {}".format(sum(ans)*2, ans[0], ans[1]))