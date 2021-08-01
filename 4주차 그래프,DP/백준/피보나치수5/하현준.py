"""
피보나치 수 5 https://www.acmicpc.net/problem/10870
"""
import sys

sys.setrecursionlimit(60000)
input = sys.stdin.readline


def fibo(n):
    if dp[n] != -1:
        return dp[n]
    dp[n] = fibo(n - 1) + fibo(n - 2)
    return dp[n]


n = int(input())
if n == 0:
    print(0)
elif n == 1 or n == 2:
    print(1)
else:
    dp = [-1 for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    fibo(n)
    print(dp[-1])
