n = int(input())
dp = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        dp[i][j] = tmp[j]
for i in range(1, n):
    for j in range(0,i+1):
        dp[i][j] = dp[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[-1]))