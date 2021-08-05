n = int(input())
dp = [1,1,2,3]

for i in range(4, n):
    dp.append(dp[i-1]+dp[i-2])

print(dp[n-1])