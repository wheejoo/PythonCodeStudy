# https://www.acmicpc.net/problem/2193

n = int(input())
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 1
    else:
        dp[i] = dp[i-2] + dp[i-1]

print(dp[n])

# n = 1 1 - 1
# n = 2 10 - 1
# n = 3 100, 101 - 2
# n = 4 1000, 1001, 1010 - 3
# n = 5 10000, 10001, 10100, 10010, 10101 - 5
