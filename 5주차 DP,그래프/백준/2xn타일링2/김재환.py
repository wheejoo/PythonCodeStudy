n=int(input())
dp = [1,3,5]
for i in range(3,n):
    if i %2 == 0:
        dp.append(dp[i-1]*2-1)
    else:
        dp.append(dp[i-1]*2+1)
print(dp[n-1]%10007)