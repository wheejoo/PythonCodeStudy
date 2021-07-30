n = int(input())
stairs = [int(input()) for _ in range(n)]

dp = [0 for _ in range(301)]
if n == 1:
    print(stairs[0])
elif n == 2:
    print(stairs[0]+stairs[1])
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])
    for i in range(3, n):
        dp[i] = max(stairs[i] + stairs[i-1] + dp[i-3], stairs[i] + dp[i-2])
    print(dp[n-1])
