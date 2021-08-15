"""
오르막 수 https://www.acmicpc.net/problem/11057
쉬운 계단 수 https://www.acmicpc.net/problem/10844 하고 비슷하네
"""
n = int(input())
num = 10007
dp = [[0 for _ in range(10)] for _ in range(n + 1)]
dp[1] = [1 for _ in range(10)]
for i in range(2, n + 1):
    for k in range(10):
        dp[i][k] = sum(dp[i - 1][k:])
print(sum(dp[n]) % num)
