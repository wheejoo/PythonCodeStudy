n = int(input())
dp = [[0 for i in range(n+1)] for i in range(3)]

for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    dp[0][i] = tmp[0]
    dp[1][i] = tmp[1]
    dp[2][i] = tmp[2]
    if i >= 2: #연산가능
        dp[0][i] = dp[0][i]+ min(dp[1][i-1], dp[2][i-1])
        dp[1][i] = dp[1][i]+ min(dp[0][i-1], dp[2][i-1])
        dp[2][i] = dp[2][i]+ min(dp[0][i-1], dp[1][i-1])
print(min([dp[0][n],dp[1][n],dp[2][n]]))