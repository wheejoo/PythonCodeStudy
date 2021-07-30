n = int(input())
dp = [0,1,2,3]

for i in range(4, n+1):
    dp.append(dp[i-1] + dp[i-2])
print(dp[n]%10007)
