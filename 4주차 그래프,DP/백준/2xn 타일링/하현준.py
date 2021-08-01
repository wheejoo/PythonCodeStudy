"""
2×n 타일링 https://www.acmicpc.net/problem/11726
그냥 피보나치네?
"""
import sys

sys.setrecursionlimit(60000)


def dfs(start):
    if dp[start] != -1:
        return dp[start]
    dp[start] = dfs(start - 1) + dfs(start - 2)
    return dp[start]


n = int(input())
if n == 1:
    print(1)
    exit(0)
dp = [-1 for _ in range(n + 1)]
dp[1] = 1
dp[2] = 2
dfs(n)
print(dp[n] % 10007)
