"""
2×n 타일링 2 https://www.acmicpc.net/problem/11727
(n-3) -> (2*2 , 2*1) & (2*1 두개, 2*1)
(n-2) -> (2*2) & (1*2 두개) & (2*1 두개)
"""
n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    dp = [-1 for _ in range(n + 1)]
    dp[1] = 1
    dp[2] = 3
    dp[3] = 5
    for i in range(4, n + 1):
        dp[i] = 2 * dp[i - 3] + 3 * dp[i - 2]

    print(dp[n] % 10007)
