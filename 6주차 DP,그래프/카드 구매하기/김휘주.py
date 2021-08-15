# https://www.acmicpc.net/problem/11052

n = int(input())
p = [0] + list(map(int,input().split()))

dp = [0 for _ in range(n+1)]

# dp[1] = p[1]
# dp[2] = max(p[1]*2, p[2])

for i in range(1,n+1):
    for k in range(1,i+1):
        dp[i] = max(dp[i], dp[i-k] + p[k])
print(dp[n])


# 1 - 1  2 - 1+1, 2  3 - 1+2, 3  4 - 1+3, 4
# 1 + (n-1), 2 + (n-2) ... n
# p[1] + dp[i-1]
# p[2] + dp[i-2]
# p[3] + dp[i-3]
