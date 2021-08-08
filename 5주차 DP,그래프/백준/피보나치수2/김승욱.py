n = int(input())
dp = [0 for _ in range(n+1)]
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if dp[n] != 0:
            return dp[n]
        else:
            dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]
print(fibo(n))