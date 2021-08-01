"""
피보나치 함수 https://www.acmicpc.net/problem/1003
"""


def fibo(n):
    global zero, one, dp, zodp
    if n in dp:
        zero += zodp[n][0]
        one += zodp[n][1]
        return dp[n]
    if n == 0:
        zero += 1
        return 0
    elif n == 1:
        one += 1
        return 1
    dp[n] = fibo(n - 1) + fibo(n - 2)
    zodp[n] = [zero, one]
    return dp[n]


for _ in range(int(input())):
    dp = dict()
    zodp = dict()
    zero = 0
    one = 0
    n = int(input())
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        fibo(n)
        print(zodp[n][0], zodp[n][1])
