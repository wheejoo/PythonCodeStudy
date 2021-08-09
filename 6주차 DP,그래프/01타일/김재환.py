n = int(input())

dp = [0 for i in range(n)]

for i in range(n):
    if i == 0:
        dp[i] = 1
    elif i==1:
        dp[i] = 2
    else:
        dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[-1])