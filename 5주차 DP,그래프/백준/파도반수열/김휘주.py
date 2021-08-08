# https://www.acmicpc.net/problem/9461

t = int(input())
dp = [1,1,1,2,2]

for i in range(5,101):
    dp.append(dp[i-1] + dp[i-5])

for _ in range(t):
    n = int(input())
    print(dp[n-1])

# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9
