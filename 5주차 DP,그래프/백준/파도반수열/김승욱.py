t = int(input())
dp = [0 for _ in range(101)]
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2

 
for i in range(t):
    n = int(input())
    for j in range(5, n+1):
        dp[j] = dp[j-1] + dp[j-5]
    print(dp[n])

