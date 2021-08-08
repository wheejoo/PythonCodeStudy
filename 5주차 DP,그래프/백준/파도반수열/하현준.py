"""
파도반 수열 https://www.acmicpc.net/problem/9461
"""
for _ in range(int(input())):
    n = int(input())
    dp = [-1 for _ in range(n + 1)]
    if n == 1 or n == 2 or n == 3:
        print(1)
    else:
        dp[1], dp[2], dp[3] = 1, 1, 1
        for i in range(4, n + 1):
            dp[i] = dp[i - 2] + dp[i - 3]
        print(dp[n])
