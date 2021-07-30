n  = int(input())
dp = [[5000,5000] for i in range(n+1)]
if n>=3:
    dp[3] = [1,0]
if n >= 5:
    dp[5] = [0,1]
for i in range(6, n+1):
    for j in range(1,i):
        if dp[j] != [-1,-1] and dp[i-j] !=[-1,-1]:#둘다 존재하면
            a = dp[j][0] + dp[i-j][0]
            b = dp[j][1] + dp[i-j][1]
            if sum(dp[i]) >sum([a,b]):
                dp[i][0]= a
                dp[i][1]= b
if sum(dp[n])!=5000*2:
    print(sum(dp[n]))
else:
    print(-1)